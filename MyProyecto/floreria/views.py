from django.shortcuts import render

# Create your views here. Crea los controladores
#Para las paginas webs
def home(request):
    return render(request,'core/index.html') 
    #Retorna la pagina renderizada
