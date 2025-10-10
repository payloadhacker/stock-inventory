from django.shortcuts import render, redirect, get_object_or_404
from .forms import StockForm
from .models import stock
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#checks if user is the admin to access the add stock page
def superuser_required(view_func):
    def check_user(user):
        return user.is_superuser
    return user_passes_test(check_user, login_url='login')(view_func)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('list_stock')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_stock')
        else:
            messages.error(request, 'Username OR password does not exist')

    
    context = {}
    return render(request, 'collection/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@superuser_required
def home(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must log in first.")
        return redirect("login")

    # Check if user has the right permission
    if not request.user.is_superuser:
        messages.error(request, "You don't have permission to add stocks.")
        return redirect("list_stock")
    
    form = StockForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("list_stock")
    
    return render(request, "collection/home.html", {"form": form})


def list_stock(request):
        #q is for the search query

    q = request.GET.get('q') 
    if q:
        stocks = stock.objects.filter(name__icontains=q)
    else:
        stocks = stock.objects.all()

    context = {
        "stocks": stocks,
        "q": q

    }
    return render(request, "collection/viewstock.html", context)


@staff_member_required(login_url='login')
def edit_stock(request, pk):
    Stock = get_object_or_404(stock, pk=pk)
    form = StockForm(request.POST or None, instance=Stock)

    if form.is_valid():
        form.save()
        return redirect("list_stock")

    context = {"form": form, "stock": Stock}
    return render(request, 'collection/editstock.html', context)


@staff_member_required(login_url='login')
def delete_stock(request, pk):
    Stock = get_object_or_404(stock, pk=pk)
    if request.method == "POST":
        Stock.delete()
        return redirect("list_stock")
    return render(request, 'collection/deletestock.html', {'stock': Stock})
