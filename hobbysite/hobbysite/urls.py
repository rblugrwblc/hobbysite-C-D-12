"""
URL configuration for hobbysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

# THIS IS NOT SAFE BUT JUST FOR TESTING: 

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create(
        username="admin",
        password=make_password("123"),
        is_superuser=True,
        is_staff=True,
        is_active=True
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("wiki/", include("wiki.urls", namespace="wiki")),
    path('commissions/', include("commissions.urls")),
    path('forum/', include('forum.urls')),
    path('blog/', include('blog.urls', namespace="blog")),
    path('merchstore/', include("merchstore.urls")),
    path('', include('user_management.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)