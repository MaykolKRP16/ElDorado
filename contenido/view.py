from django.shortcuts import render
def inicio(request):
    return render(request,"inicio.html")
def curso(request):
    return render(request,"CursoLaravel.html")

