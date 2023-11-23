from django.contrib import admin
from .models import LastName, FirstName, MiddleName, Street, Contact

admin.site.register(LastName)
admin.site.register(FirstName)
admin.site.register(MiddleName)
admin.site.register(Street)
admin.site.register(Contact)
