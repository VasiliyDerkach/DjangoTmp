from django.shortcuts import render

# Create your views here.
def class_tmpl(request):
    return render(request,"second_task/class_template.html")
def func_tmpl(request):
    return render(request,"second_task/func_template.html")