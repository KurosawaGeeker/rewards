from django.contrib import admin
from users.models import User,Campus,School
# Register your models here.
admin.site.register(User)
admin.site.register(Campus)
admin.site.register(School)