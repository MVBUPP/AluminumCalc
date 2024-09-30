from django.shortcuts import render
from AluminumCalcApp.models import UserTolerances12_2Model
from django.contrib import messages
from AluminumCalcApp.forms import ToleranceForms
# Create your views here.
def home(request): 
    return render(request, "home.html")

def create(request): 
    return render(request, "create.html")

def update(request): 
    return render(request, "update.html")

def show12_2UserTolerances(request):
    showall=UserTolerances12_2Model.objects.all()
    return render(request, 'home.html', {"data":showall})

def insert12_2UserTolerance(request):
    if request.method=="POST":
        if request.POST.get('name') and request.POST.get('alloy') and request.POST.get('diameter') and request.POST.get('tolerance1'):
            saveTolerance= UserTolerances12_2Model()
            saveTolerance.name=request.POST.get('name')
            saveTolerance.alloy=request.POST.get('alloy')
            saveTolerance.diameter=request.POST.get('diameter')
            saveTolerance.tolerance1=request.POST.get('tolerance1')
            saveTolerance.save()
            messages.success(request, 'UserTolerances12_2'+saveTolerance.name+ ' is saved successfully!')
            return render(request, 'create.html')
        else:
            return render(request, 'create.html')

def update12_2UserTolerance(request, id):
    toleranceToUpdate=UserTolerances12_2Model.objects.get(id=id)
    return render(request, 'update.html', {"UserTolerances12_2Model":toleranceToUpdate})

def saveUpdateChanges(request, id):
    toleranceToUpdate=UserTolerances12_2Model.objects.get(id=id)
    form=ToleranceForms(request.POST, instance=toleranceToUpdate)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record updated successfully')
        return render(request, 'update.html', {"UserTolerances12_2Model":toleranceToUpdate})

def deleteUserTolerance(request, id):
    toleranceToDelete= UserTolerances12_2Model.objects.get(id=id)
    toleranceToDelete.delete()
    showData=UserTolerances12_2Model.objects.all()
    return render(request, "home.html", {"data":showData}) 