from django.contrib import admin

# Register your models here.

from .models import *

class Listingadmin(admin.ModelAdmin):
	list_display=['name','user','available','startbid','time']

class Bidadmin(admin.ModelAdmin):
	list_display=['listing','user','amount']

class Commentadmin(admin.ModelAdmin):
	list_display=['comment','listing','user','time']

class Winneradmin(admin.ModelAdmin):
	list_display=['user','listing','amount']
admin.site.register(Listing,Listingadmin)
admin.site.register(Bid,Bidadmin)
admin.site.register(Comment,Commentadmin)
admin.site.register(Winner,Winneradmin)