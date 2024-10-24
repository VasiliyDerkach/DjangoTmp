from django.shortcuts import render
def main(request):
    return render(request,"third_task/mainpage.html")
def price(request):
    context = {'1': 'Atomic Heart', '2': "Cyberpunk 2077", '3': 'Monopolya' }
    return render(request,"third_task/price.html", context)
def card(request):
    return render(request,"third_task/card.html")

# Create your views here.
