from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('add', views.add),
    path('<int:thought_id>', views.thought_detail),
    path('<int:thought_id>/delete', views.delete),
    path('<int:thought_id>/like', views.like),
    path('<int:thought_id>/unlike', views.unlike),
]