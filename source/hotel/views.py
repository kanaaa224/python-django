from django.shortcuts import render, redirect
from .models import HotelManager, RoomManager
from account.decorators import login_required

def hotel_list(request):
    hotels = HotelManager.get_all_hotels()

    is_authenticated = 'user_id' in request.session

    return render(request, 'hotel_list.html', { 'hotels': hotels, 'is_authenticated': is_authenticated })

@login_required
def hotel_detail(request, pk):
    hotel = HotelManager.get_hotel_by_id(pk)

    return render(request, 'hotel_detail.html', { 'hotel': hotel })

def hotel_create(request):
    if request.method == 'POST':
        name       = request.POST.get('name')
        prefecture = request.POST.get('prefecture')

        if not name or not prefecture:
            return render(request, 'hotel_create.html', {
                'error': '名前と都道府県を入力してください。',
                'name': name, 'prefecture': prefecture
            })

        hotel_id = HotelManager.create_hotel(name, prefecture)

        return redirect('hotel_detail', pk=hotel_id)

    return render(request, 'hotel_create.html') # GETリクエストの場合はフォームを表示

def hotel_update(request, pk):
    if request.method == 'POST':
        name       = request.POST.get('name')
        prefecture = request.POST.get('prefecture')

        if not name or not prefecture:
            hotel = HotelManager.get_hotel_by_id(pk)

            return render(request, 'hotel_update.html', {
                'error': '名前と都道府県を入力してください。',
                'hotel': hotel,
                'name': name or hotel['name'],
                'prefecture': prefecture or hotel['prefecture']
            })

        HotelManager.update_hotel(pk, name, prefecture)

        return redirect('hotel_detail', pk=pk)

    hotel = HotelManager.get_hotel_by_id(pk)

    return render(request, 'hotel_update.html', { 'hotel': hotel }) # GETリクエストの場合は編集フォームを表示

def hotel_delete(request, pk):
    if request.method == 'POST':
        HotelManager.delete_hotel(pk)

        return redirect('hotel_list')

    hotel = HotelManager.get_hotel_by_id(pk)

    return render(request, 'hotel_delete.html', { 'hotel': hotel }) # GETリクエストの場合は確認画面を表示


def room_create(request, hotel_id):
    if request.method == 'POST':
        name = request.POST.get('name')

        if not name:
            return render(request, 'room_create.html', {
                'error': '部屋名を入力してください。',
                'name': name,
                'hotel_id': hotel_id
            })

        room_id = RoomManager.create_room(name, hotel_id)

        return redirect('hotel_detail', pk=hotel_id)

    hotel = HotelManager.get_hotel_by_id(hotel_id)

    return render(request, 'room_create.html', { 'hotel': hotel }) # GETリクエストの場合はフォームを表示

def room_update(request, room_id):
    room = RoomManager.get_room_by_id(room_id)

    if not room:
        return redirect('hotel_list')

    if request.method == 'POST':
        name = request.POST.get('name')

        if not name:
            return render(request, 'room_update.html', {
                'error': '部屋名を入力してください。',
                'room': room,
                'name': name or room['name']
            })

        RoomManager.update_room(room_id, name)

        return redirect('hotel_detail', pk=room['hotel_id'])

    return render(request, 'room_update.html', { 'room': room }) # GETリクエストの場合は編集フォームを表示

def room_delete(request, room_id):
    room = RoomManager.get_room_by_id(room_id)

    if not room:
        return redirect('hotel_list')

    if request.method == 'POST':
        RoomManager.delete_room(room_id)

        return redirect('hotel_detail', pk=room['hotel_id'])

    return render(request, 'room_delete.html', { 'room': room }) # GETリクエストの場合は確認画面を表示