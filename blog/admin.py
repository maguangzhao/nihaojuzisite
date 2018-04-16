from django.contrib import admin
from .models import JuZi,Book
# Register your models here.

class JuZiAdmin(admin.ModelAdmin):
    list_display = ('body','author','publish')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish')

admin.site.register(JuZi,JuZiAdmin)
admin.site.register(Book,BookAdmin)