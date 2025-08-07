from django.urls import path
from django.views.generic import TemplateView
from . import views
from core.views import ProcessarCartoesView


urlpatterns = [
    path('', views.getRoutes, name='home'),
     path('upload/', views.upload_view, name='upload'),
    path('processar-cartoes/', ProcessarCartoesView.as_view(), name='processar-cartoes'),
]
