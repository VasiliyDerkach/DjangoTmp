from django.shortcuts import render
def main(request):
    return render(request,"third_task/mainpage.html")
def price(request):
    return render(request,"third_task/price.html")
def card(request):
    return render(request,"third_task/card.html")

# Create your views here.
