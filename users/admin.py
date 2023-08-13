from django.contrib import admin

from .models import Links, ResumeUser, User

admin.site.register(Links)
admin.site.register(ResumeUser)
admin.site.register(User)