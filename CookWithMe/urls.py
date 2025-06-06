"""
URL configuration for CookWithMe project.

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
from django.urls import path
from django.urls.conf import include
from accounts.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("api/register/", RegisterView.as_view(),name='register'),
    path("api/login/", LoginView.as_view(), name='login'),
    path("api/logout/",LogoutView.as_view(), name='logout'),
    path("categories/",include("categories.urls")),
    path("recipes/", include("recipes.urls")),
    # path("favorites/", include("favorites.urls")),
    path("ingredients/", include("ingredients.urls")),
    # path("reviews/", include("reviews.urls")) not needed as reviews are included in recipes.urls
]
