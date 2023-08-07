from django.shortcuts import render, redirect
from .models import Biryani, Biryani_Type
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'index.html')


def show_biryani_type(request):
    btype = Biryani_Type.objects.all()
    return render(request, 'biryani_type.html', {'btypes': btype})


def add_biryani_type(request):
    btn = request.POST.get('name')
    Biryani_Type(name=btn).save()
    messages.success(request, 'Biryani Type is saved !!!')
    return redirect('/show_btype/')


def show_biryani(request):
    biryani_data = Biryani.objects.all()
    btype = Biryani_Type.objects.all()
    return render(request, 'biryani.html', {'biryani': biryani_data, 'btypes': btype})


def add_biryanis(request):
    bn = request.POST.get('name')
    bp = request.POST.get('price')
    b_id = request.POST.get('id')
    biryani = Biryani_Type.objects.get(name=b_id)
    result = Biryani(name=bn, price=bp, biryani_Type=biryani)
    result.save()
    messages.success(request, 'Biryani is saved !!!')
    return redirect('/show_biryani/')


