from django.contrib import admin
from auth_app.models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Events)
admin.site.register(Vendors)
