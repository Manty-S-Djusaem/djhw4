"""djcars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from brands.views import *
from models.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('brands/<int:brand_id>/', one_brand),
    path('brands/<int:brand_id>/models/<int:model_id>', one_brand_series)

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)