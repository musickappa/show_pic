from .models import Myprofile,Piclist
from django import forms

class register_profile(forms.ModelForm):
    class Meta:
        model = Myprofile
        fields = ('first_name', 'family_name','career', 'feature','location','profile_img')
        labels = {'first_name':'名前 ', 'family_name':'苗字','career':'職種','feature':'専門','location':'活動地','profile_img':'プロフィール画像'}