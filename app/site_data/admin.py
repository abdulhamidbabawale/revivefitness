from django.contrib import admin
from .models import User,Classes,Plans,PlanDuration,UserProfile,Benefits
# Register your models here.

admin.site.register(User)
admin.site.register(Classes)
admin.site.register(Plans)
admin.site.register(PlanDuration)
admin.site.register(UserProfile)
admin.site.register(Benefits)
