from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request,name):
    return HttpResponse(f"bem vindo {name}")

def soma(request,num1,num2):
    sum = num1 + num2
    return HttpResponse(f"A soma dos numeros é {sum}")