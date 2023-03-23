from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from .forms import MoviePickerModel, MoviePickerForm
import requests
import json
from bs4 import BeautifulSoup


# Create your views here.
def MoviePicker_home(request):
    return render(request, "MoviePicker/MoviePicker_home.html")

def MoviePicker_generate(request):
    form = MoviePickerForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../')
    content = {'form': form}
    return render(request, 'MoviePicker/MoviePicker_generate.html', content)

def MoviePicker_view(request):
    entry = MoviePickerModel.objects.all()
    content = {'entry': entry}
    return render(request, 'MoviePicker/MoviePicker_view.html', content)

def MoviePicker_details(request, pk):
    entrys = get_object_or_404(MoviePickerModel, pk=pk)
    content = {'entrys': entrys}
    return render(request, 'MoviePicker/MoviePicker_details.html', content)

def update(request, pk):
    item = get_object_or_404(MoviePickerModel, pk=pk)
    form = MoviePickerForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../view')
    content = {'item': item, 'form': form}
    return render(request, 'MoviePicker/MoviePicker_update.html', content)

def delete(request, pk):
        item = get_object_or_404(MoviePickerModel, pk=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('../../view')
        content = {'item': item}
        return render(request, 'MoviePicker/MoviePicker_delete.html', content)

def MoviePicker_bs(request):
    page = requests.get("https://www.rottentomatoes.com/critics")
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all('li', class_='critics-home-spotlight__li')[0].get_text()
    print(info)
    content = {"info": info}
    return render(request, 'MoviePicker/MoviePicker_bs.html', content)
