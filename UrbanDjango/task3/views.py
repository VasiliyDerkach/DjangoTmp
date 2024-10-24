from django.shortcuts import render
def main(request):
    return render(request,"third_task/mainpage.html")
def price(request):
    context = {'p1': 'Atomic Heart', 'p2': "Cyberpunk 2077", 'p3': 'Monopolya' ,}
    return render(request,"third_task/price.html", context)
def card(request):
    return render(request,"third_task/card.html")

# Create your views here.
