from django.contrib import admin

# Register your models here.
from django.contrib import admin
import inspect
import profele.models


get_all_members = inspect.getmembers(profele.models, inspect.isclass)
for model in get_all_members: print(model[0])
for model in get_all_members: admin.site.register(model[1])