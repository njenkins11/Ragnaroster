from django.contrib import admin
from .models import Roster
from .models import Player
from .models import Spell
from .models import Class

# Register your models here.
admin.site.register(Roster)
admin.site.register(Player)
admin.site.register(Spell)
admin.site.register(Class)
