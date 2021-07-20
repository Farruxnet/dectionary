from django.contrib import admin
from django.urls import path
from bot.views import web_hook
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', csrf_exempt(web_hook)),
]
