from django.shortcuts import render, redirect
from .models import User
from .models import DataUser
from .models import payment

def hotel(request):
    return render(request, 'hotels/hotel.html')

def hotels(request):
    return render(request, 'hotels/hotels.html')

def signup_view(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('emaill')
        p = request.POST.get('passwordd')
       
         
        
        
        
        data = User(username=n, email=e, password=p)
        data.save()

       
    return render(request, 'signup.html')
def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
    
        user = User.objects.filter(email=email, password=password).first()

        if user:
            return redirect('hotels') 
        else:
            return render(request, 'signin.html', {'error': 'Email or password is incorrect!'})

    return render(request, 'signin.html')
def book_view(request):
    if request.method == 'POST':
        try:
            rooms = int(request.POST.get('rooms', 1))
        except ValueError:
            rooms = 1
        price_per_room = 1000 
        total_price = rooms * price_per_room
        return render(request, 'booking_result.html', {
            'rooms': rooms,
            'total_price': total_price
        })
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        number_of_rooms = request.POST.get('number_of_rooms')
        number_of_individuals = request.POST.get('number_of_individuals')
        print("POST data:", request.POST)
   

        
        number_of_rooms = request.POST.get('number_of_rooms')
        number_of_individuals = request.POST.get('number_of_individuals')

        if number_of_rooms:
            number_of_rooms = int(number_of_rooms)
        else:
             number_of_rooms = 0  

        if number_of_individuals:
                number_of_individuals = int(number_of_individuals)
        else:
                number_of_individuals = 0  
                if not checkin:
                    return render(request, 'book.html', {'error': 'Check-in date is required.'})

        data = DataUser(
            fullname=fullname,
            email=email,
            phone_number=phone_number,
            checkin=checkin,
            checkout=checkout,
            number_of_rooms=number_of_rooms,
            number_of_individuals=number_of_individuals
        )
 
        data.save()
       

    return render(request, 'book.html')
def details_view(request):
     

     return render(request, 'details.html')


def payment_view(request):
    if request.method == 'POST':
       
        Cardholder_Name = request.POST.get('Cardholder_Name')
        Card_Number = request.POST.get('Card_Number')
        Expiration_Date = request.POST.get('Expiration_Date')
        cvv = request.POST.get('cvv')

       
        if not Card_Number or not Cardholder_Name or not Expiration_Date or not cvv:
            
            return render(request, 'payment.html', {'error': 'All fields are required.'})

        
        data = payment(
            Cardholder_Name=Cardholder_Name,
            Card_Number=Card_Number,
            Expiration_Date=Expiration_Date,
            cvv=cvv,
        )
        data.save()

       
        return render(request, 'payment_success.html')

    return render(request, 'payment.html')  

      


def one_view(request):
     

     return render(request, 'pages/cairo-details/one.html') 
def tow_view(request):
     

     return render(request, 'pages/cairo-details/tow.html')  


def three_view(request):
     

     return render(request, 'pages/cairo-details/three.html')
def four_view(request):
     

     return render(request, 'pages/cairo-details/four.html')
def aone_view(request):
     

     return render(request, 'pages/alx-details/aone.html')
def atow_view(request):
     

     return render(request, 'pages/alx-details/atow.html')
def athree_view(request):
     

     return render(request, 'pages/alx-details/athree.html')
def afour_view(request):
     

     return render(request, 'pages/alx-details/afour.html')
def home_view(request):
    
    return render(request, 'pages/home.html')







   