from django.urls import path
from .views import hotel_list, hotel_detail, hotel_create, hotel_update, hotel_delete, room_create, room_update, room_delete

urlpatterns = [
    path('list/',            hotel_list,   name='hotel_list'),
    path('<int:pk>/',        hotel_detail, name='hotel_detail'),
    path('create/',          hotel_create, name='hotel_create'),
    path('<int:pk>/update/', hotel_update, name='hotel_update'),
    path('<int:pk>/delete/', hotel_delete, name='hotel_delete'),

    path('<int:hotel_id>/rooms/create/', room_create, name='room_create'),
    path('rooms/<int:room_id>/update/',  room_update, name='room_update'),
    path('rooms/<int:room_id>/delete/',  room_delete, name='room_delete'),
]