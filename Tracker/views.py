from django.shortcuts import render,redirect
from .models import Transaction
from .forms import TransactionForm


# Create your views here.

def add(request):
    form = TransactionForm()

    if request.method == 'POST':
        form = TransactionForm(request.POST,request.FILES)

        if form.is_valid():
           form.save()
           ''' transaction = form.save(commit=False)
            transaction.user = User.objects.first()  # for testing
            transaction.save()'''
           return redirect('transactionlist')

    context={ 'form': form}

    return render(request, 'Tracker/add.html',context)

def update(request,pk):
    pkey=Transaction.objects.get(pk=pk)
    form=TransactionForm(instance=pkey)

    if request.method=='POST':
        form=TransactionForm(request.POST,request.FILES,instance=pkey)

        if form.is_valid():
            form.save()
            return redirect('transactionlist')

    context={ 'form': form}

    return render(request, 'Tracker/add.html',context)

def delete(request,pk):
    pkey=Transaction.objects.get(pk=pk)

    if request.method=='POST':
        pkey.delete()
        return redirect('transactionlist')

    context={ 'pkey': pkey}

    return render(request, 'Tracker/delete.html',context)    

      

def transaction_list(request):
    transactions=Transaction.objects.all().order_by('-date')

    context={'transactions':transactions}

    return render(request,'Tracker/show.html',context)



def dashboard(request):
    transaction=Transaction.objects.all()
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
    




        





    
   