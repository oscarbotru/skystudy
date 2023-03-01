from django.contrib import admin

from users.models import Payment, User, Subscription

admin.site.register(Payment)
admin.site.register(User)
admin.site.register(Subscription)
