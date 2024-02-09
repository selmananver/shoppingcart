from django.contrib import admin
from .models import Order,OrderedItem

# Register your models here.

class MyAdmin(admin.ModelAdmin):
    list_filter=[
        "owner",
        "order_status",
    ]
    search_fields=(
        "owner",
        "id"
    )
admin.site.register(Order,MyAdmin)

