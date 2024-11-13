from django.contrib import admin
from .models import User, Order

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age')  #
    search_fields = ('name', 'email')
    list_filter = ('age',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'user')  #
    search_fields = ('title', 'user')
    list_filter = ('user',)


admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)