
# manejo de rutas 
from django.shortcuts import render, redirect
from users.models import Administrator, Company

# registro y autenticacion de usuarios 
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# proteccion de rutas 
from django.contrib.auth.decorators import login_required

# registro
def signup(request):
    if request.method=="GET":
        return render(request,"users/register.html")
    else:
        # verificamos que las contraseñas coincidan
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # registramos al empresa 
                new_company = Company.objects.create(
                    name = request.POST["name_company"]
                )
                # registramos el usuario nuevo 
                new_user = Administrator.objects.create(
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    email=request.POST["email"],
                    username=request.POST["username"], 
                    password=request.POST["password1"],
                    company = new_company
                )
                new_user.save()
                # le damos un login automantico al usuario 
                login(request,new_user)
                print("registrado")
                return redirect("inventario:home")
            # en caso de que el usuario o empresa ya esten registrado elevamos el error de integridad 
            except IntegrityError: 
                print("ya existe")
                return render(request,"users/register.html",{
                    "mensaje":"username o empresa ya existente "
                })
        print("contraseñas erroneas ")
        return render(request,"users/register.html",{
            "mensaje":"las contraseñas no coinciden "
        })

# autenticacion y login
def login_(request):
    if request.method=="GET":
        return render(request,"users/login.html")
    else:
        user = authenticate(
            request, 
            username = request.POST["username"], 
            password = request.POST["password"])
        if user == None:
            return render(request,"users/login.html",{
            "mensaje":" Credenciales incorrectas"
        })
        else:
            login(request,user)
            return redirect("inventario:home")






@login_required
def end_sesion(request):
    logout(request)
    return redirect("users:signin")
