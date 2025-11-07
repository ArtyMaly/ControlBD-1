from django.contrib import admin
from .models import User, Genres, Movies, WatchHistory, Subscriptions, Payments

# Register your models here.
admin.site.register(User)
admin.site.register(Genres)
admin.site.register(Movies)
admin.site.register(WatchHistory)
admin.site.register(Subscriptions)
admin.site.register(Payments)
