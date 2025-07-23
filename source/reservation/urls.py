from django.urls import path
from .views import reservation_create, reservation_list, reservation_detail, reservation_delete

urlpatterns = [
    path('create/<int:room_id>/', reservation_create, name='reservation_create'),
    path('list/',                 reservation_list,   name='reservation_list'),
    path('<int:pk>/',             reservation_detail, name='reservation_detail'),
    path('<int:pk>/delete/',      reservation_delete, name='reservation_delete'),
]