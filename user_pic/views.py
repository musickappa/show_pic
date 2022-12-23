from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Piclist,Myprofile
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import register_profile


class show_piclist(ListView):
    template_name = 'user_pic/list.html'
    model = Piclist
    
class show_picdetail(DetailView):
    template_name = 'user_pic/detail.html'
    model = Piclist
    
class register_pic(CreateView):
    form = register_profile
    context = {'form': form,}
    template_name = 'user_pic/register.html'
    model = Myprofile
    fields = ('first_name', 'family_name','career', 'feature','location','profile_img')
    success_url = reverse_lazy('list')
    
class delete_pic(DeleteView):
    template_name = 'user_pic/delete.html'
    model = Piclist
    success_url = reverse_lazy('list')  
    
class update_pic(UpdateView):
    template_name = 'user_pic/update.html'
    model = Piclist
    fields = ('first_name','last_name')
    success_url = reverse_lazy('list')
    
class profile(DetailView):
    template_name = 'user_pic/profile.html'
    model = Myprofile
    