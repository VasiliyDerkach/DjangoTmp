from django.shortcuts import render
def main(request):
    context = {'pagename': 'Главная страница'}
    return render(request,"fourth_task/mainpage.html", context)
def price(request):
    context = {'games': ['Atomic Heart', "Cyberpunk 2077",'Monopolya'], 'pagename': 'Игры'}
    return render(request,"fourth_task/price.html", context)
def card(request):
    context = {'pagename': 'Корзина'}
    return render(request,"fourth_task/card.html", context)

# Create your views here.
