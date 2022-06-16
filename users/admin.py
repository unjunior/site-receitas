from django.contrib import admin
from .models import User

"""
Arquivo de admin criado por Bruno Cristiano
"""

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'email', 'cpf')
    list_filter = ('firstName', 'cpf')
    list_display_links = list_display
    search_fields = (
        'firstName',
        'cpf',
        'email',
    )

