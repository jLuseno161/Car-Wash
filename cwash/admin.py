from cwash.models import Booking, Profile, Washplan, services
from django.contrib import admin

class WashplanAdmin(admin.ModelAdmin):
    filter_horizontal =('service',)

admin.site.register(Profile)
admin.site.register(Booking)
admin.site.register(Washplan,WashplanAdmin)
admin.site.register(services)


