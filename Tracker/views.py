from django.shortcuts import render,redirect
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request,"User already exists")
            return redirect('signup')

        
        user=User.objects.create_user(
        username=username,
        email=email,
        password=password
        )    
        user.save()

        messages.success(request,"Account created Succeessfully")

        return redirect('login')
        
    return render(request, 'Tracker/signup.html')
    
def login_view(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"Incorrect password or username")
            return redirect('login')
        
    return render(request,'Tracker/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request,'Tracker/home.html')

@login_required
def add(request):
    form = TransactionForm()

    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  # for testing
            transaction.save()
            return redirect('transactionlist')

    context={ 'form': form}

    return render(request, 'Tracker/add.html',context)

@login_required
def update(request,pk):
    pkey = Transaction.objects.get(pk=pk, user=request.user)
    form=TransactionForm(instance=pkey)

    if request.method=='POST':
        form=TransactionForm(request.POST,request.FILES,instance=pkey)

        if form.is_valid():
            form.save()
            return redirect('transactionlist')

    context={ 'form': form}

    return render(request, 'Tracker/add.html',context)

@login_required
def delete(request,pk):
    pkey = Transaction.objects.get(pk=pk, user=request.user)

    if request.method=='POST':
        pkey.delete()
        return redirect('transactionlist')

    context={ 'pkey': pkey}

    return render(request, 'Tracker/delete.html',context)    

      
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    context={'transactions':transactions}

    return render(request,'Tracker/show.html',context)


@login_required
def dashboard(request):
    transaction = Transaction.objects.filter(user=request.user).order_by('-date')
    total_income=0
    total_expense=0

    for t in transaction:
        if t.category=='income':
            total_income+=t.amount
        else:
            total_expense+=t.amount

    balance=total_income-total_expense

    context={'Income':total_income,'Expense':total_expense,'Balance':balance}

    return render(request,'Tracker/dashboard.html',context)            
    




        





    
   