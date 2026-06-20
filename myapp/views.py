from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def expense_list(request):
    expenses = Expense.objects.all()

    total = 0
    for expense in expenses:
        total += expense.amount

    return render(
        request,
        'myapp/expense_list.html',
        {
            'expenses': expenses,
            'total': total
        }
    )

def add_expense(request):

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ExpenseForm()

    return render(
        request,
        'myapp/add_expense.html',
        {
            'form': form
        }
    )

def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()

    return redirect('/')