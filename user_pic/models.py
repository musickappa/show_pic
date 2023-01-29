from tabnanny import verbose
from tokenize import blank_re
from django.db import models
from django.core.validators import FileExtensionValidator
# https://djangobrothers.com/blogs/django_null_blank/
# blank ,nullの考え方
# MySQL 起動　en
# sudo mysql -u root
# Create your models here.

# genie install https://qiita.com/sakai00kou/items/0b401faf6dd72ad63d87
# systemd install https://snowsystem.net/other/windows/wsl2-ubuntu-systemctl/

class Myprofile(models.Model):
    user_id = models.IntegerField(verbose_name='ユーザ番号', unique=True,null=True,blank=True)
    first_name  = models.CharField(max_length=50, null=True,blank=True)
    family_name = models.CharField(max_length=50, null=True,blank=True)
    career = models.CharField(max_length=50, null=True,blank=True)
    feature = models.CharField(max_length=50, null=True,blank=True)
    location = models.CharField(max_length=50, null=True,blank=True)
    profile_img = models.ImageField(upload_to='user_pic/img',validators=[FileExtensionValidator(['pdf', 'png', 'jpeg', 'jpg', 'mp4'])],null=True, blank=False, default='user_pic/img/kappa_icon.jpg')
    
    class Meta:
        verbose_name_plural ="プロフィール"
    

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.family_name, self.first_name)
    


SEASON = (("danger","spring"),("info","summer"),("warning","Autumn"),("light","winter"),("dark","other"))
class Piclist(models.Model):
    user = models.ForeignKey(Myprofile, on_delete=models.CASCADE, verbose_name="投稿者",  to_field="user_id", null=True,blank=True)
    place = models.CharField(max_length=200,null=True,blank=True)
    season = models.CharField(max_length=50,choices=SEASON,null=True,blank=True)
    image = models.ImageField(upload_to='user_pic/img',null=True, blank=True,validators=[FileExtensionValidator(['pdf', 'png', 'jpeg', 'jpg', 'mp4'])],)
    birth_date = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    deleted = models.BooleanField('論理削除フラグ', default=False)

    class Meta:
        verbose_name_plural ="写真一覧"

    

    
    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.family_name)
    

    