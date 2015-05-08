from django.contrib import admin
from map.models import Cotter, Slope, Radiation

# Register your models here.

class CotterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cotter, CotterAdmin)



class SlopeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slope, SlopeAdmin)


class RadiationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Radiation, RadiationAdmin)

