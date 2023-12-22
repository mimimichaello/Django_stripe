"""
URL configuration for django_stripe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from stripe_app.views import buy_item, get_item_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>', buy_item, name='buy-item'),
    path('item/<int:item_id>', get_item_page, name='get-item-page'),
]
