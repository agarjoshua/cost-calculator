from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from index.forms import Calculate, Calculate2
from django import forms

# Create your views here.
def index(request): 
    '''
     Input:
     String Integer:
     Output:
     Returns the ammount in dollars you need to put in receive the ammount you want without changing it to kenyan shillings

    '''

    total_ammount = []
    total_cost = []
    form = Calculate(request.POST)
    context = {}

    # total_ammount2 = []
    # total_cost2 = []
    # form2 = Calculate2(request.POST)
    
    if request.method == 'POST': 

        form = Calculate(request.POST) 
        x = int(form['ammount'].value())

        print(x)

        commission = (0.02 * x)
        print(commission)

        paypal_to_offshore = (0.03 * x)
        print(paypal_to_offshore)

        offshore_to_local = paypal_to_offshore * 0.15
        print(offshore_to_local)

        Local_to_mpesa = 0.62 #This is in kenyan shillings

        total_cost = commission + paypal_to_offshore + offshore_to_local + Local_to_mpesa
        print(total_cost)

        total_ammount = total_cost + x
        print(total_ammount)

    context = {
        'form': form,
        'total_ammount' : total_ammount,
        'total_cost' : total_cost
    }


    return render( request, 'index/norates.html' , context)



def rates(request):  # sourcery skip: extract-method

    '''
     Input:
     String Integer:
     Output:
     Returns the ammount in Kenyan Shillings you need to put in receive the ammount you want also in kenyan shillings

    '''

    total_ammount = []
    total_cost = []
    form = Calculate(request.POST)

    if request.method == 'POST':   # accept the information

        form22 = Calculate(request.POST) # "populate" a form with that data
        x = int(form['ammount'].value())

        print(x)

        commission = (0.02 * x) 
        print(commission)

        paypal_to_offshore = (0.03 * x) 

        offshore_to_local = (paypal_to_offshore * 0.15) 
        print(offshore_to_local)

        Local_to_mpesa = 62 #This is in kenyan shillings

        offshore_cost = (commission + paypal_to_offshore + offshore_to_local) * 100
        print(offshore_cost)

        total_cost = offshore_cost + Local_to_mpesa

        total_ammount = total_cost + (x * 100)
        print(total_ammount)

    context = {
        'form': form,
        'total_ammount' : total_ammount,
        'total_cost' : total_cost
    }

    # form = Calculate()

    return render(request, 'index/rates.html' , context)

def result(request):

    return render(request, 'index/home.html')




