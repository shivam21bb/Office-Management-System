from django.contrib import admin

# Register your models here.
from .models import Post,Contact
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']
@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['name','email','message']