from django.contrib import admin
from .models import Animal
from .models import Equipement
from .forms import MoveForm

admin.site.register(Animal)
admin.site.register(Equipement)
