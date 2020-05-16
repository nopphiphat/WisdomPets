from django.contrib import admin

# Register models
# Import Pet model
from .models import Pet

# Register PetAdmin class; Create an admin interface class for Pet model, and register this class with the admin to tell it which model it's associated with.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
	list_display = ['name', 'species', 'breed', 'age', 'sex']
	