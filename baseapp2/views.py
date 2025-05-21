import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from baseapp2.models import  AboutUs, Feedback, ItemList, Items
from baseapp2.models import BookTable

# Create your views here.

def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html', {'items' : items, 'list' : list, 'review' : review})

def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html', {'data' : data})

def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items' : items, 'list' : list})

def BookTableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')

        if name and email and total_person and booking_date:
            data = BookTable(
                Name=name,
                Phone_number=phone_number,
                Email=email,
                Total_person=total_person,
                Booking_date=booking_date
            )
            data.save()

            # ✅ Yahan SMS bhejne ka function call karo:
            send_booking_sms(phone_number, name, booking_date, total_person)

            # ✅ Confirmation message ke liye Django messages framework use karo
            messages.success(request, "Table booked successfully! SMS Sent.")
            
            return redirect('Book_Table')  # Redirect after POST (Best Practice)
        
    return render(request, 'book_table.html')


def send_booking_sms(phone_number, name, booking_date, total_person):
    api_key = "XkArcF3UKOxXwxjm0EOQQlova1AqF3OdZqkRpsqRr0jATg6OVAUanCpxSQrK"
    url = "https://www.fast2sms.com/dev/bulkV2"

    headers = {
        'authorization': api_key,
    }

    message = f"Hello {name}, your table for {total_person} person(s) has been booked for {booking_date}. Thank you!"

    payload = {
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'q',
        'numbers': phone_number
    }

    response = requests.post(url, data=payload, headers=headers)
    print("Fast2SMS API Response:")
    print(response.text)
  


def FeedbackView(request):
    return render(request, 'feedback.html')
