from django.shortcuts import render,redirect
from .models import Transaction,Category
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def add(request):

    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
           form.save(user=request.user)
           ''' transaction = form.save(commit=False)
            transaction.user = User.objects.first()  # for testing
            transaction.save()'''
           return redirect('transactionlist')

    else:
        form = TransactionForm()

    return render(request, 'Tracker/add.html', {'form': form})

'''@login_required
def add(request):

    if request.method=='POST':
        form=TransactionForm(request.POST)#,user=request.user)

        if form.is_valid():
            transaction=form.save(commit=False)
            transaction.user=User.objects.first()#request.user
            transaction.save()
            return redirect('transaction_list')

        #else:
            
            form=TransactionForm(user=request.user)
        form = TransactionForm()
        context={'form':form}    

        return render(request,'Tracker/add.html',context)  '''
      

def transaction_list(request):
    transactions=Transaction.objects.filter(user=request.user).order_by('-date')

    context={'transactions':transactions}

    return render(request,'Tracker/show.html',context)


@login_required
def dashboard(request):
    transaction=Transaction.objects.filter(user=request.user)
    total_income=0
    total_expense=0

    for t in transaction:
        if t.category.category=='income':
            total_income+=t.amount
        else:
            total_expense+=t.amount

    balance=total_income-total_expense

    context={'Income':total_income,'Expense':total_expense,'Balance':balance}

    return render(request,'Tracker/dashboard.html',context)            
    




        





    
   