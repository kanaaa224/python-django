from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from account.decorators import login_required
from .models import ReservationManager
from hotel.models import RoomManager

@login_required
@csrf_protect
def reservation_create(request, room_id):
    room = RoomManager.get_room_by_id(room_id)

    if not room:
        return redirect('hotel_list')

    if request.method == 'POST':
        price     = request.POST.get('price')
        stay_date = request.POST.get('stay_date')

        if not (price and stay_date):
            return render(request, 'reservation_create.html', {
                'room': room, 'error': '全ての項目は必須です。',
            })

        try:
            user_id = request.session.get('user_id')

            ReservationManager.create_reservation(
                room_id=room_id, price=price,
                user_id=user_id, stay_date=stay_date
            )

            return redirect('hotel_list')
        except Exception as e:
            return render(request, 'reservation_create.html', {
                'room': room,
                'error': f'予約の作成に失敗しました: {str(e)}',
            })

    return render(request, 'reservation_create.html', { 'room': room }) # GETリクエスト時は予約フォームを表示

@login_required
def reservation_list(request):
    user_id = request.session.get('user_id')

    reservations = ReservationManager.get_reservations_by_user_id(user_id)

    return render(request, 'reservation_list.html', {
        'reservations': reservations
    })

@login_required
def reservation_detail(request, pk):
    user_id = request.session.get('user_id')

    reservation = ReservationManager.get_reservation_by_id(pk)

    if not reservation or reservation['user_id'] != user_id: # 予約が存在しない or ログインユーザが予約申込者でない場合
        return redirect('reservation_list')

    return render(request, 'reservation_detail.html', {
        'reservation': reservation
    })

@login_required
@csrf_protect
def reservation_delete(request, pk):
    user_id = request.session.get('user_id')

    reservation = ReservationManager.get_reservation_by_id(pk)

    if not reservation or reservation['user_id'] != user_id:
        return redirect('reservation_list')

    if request.method == 'POST':
        try:
            ReservationManager.delete_reservation(pk)

            return redirect('reservation_list')
        except Exception as e:
            return render(request, 'reservation_delete.html', {
                'reservation': reservation,
                'error': f'予約の削除に失敗しました: {str(e)}',
            })

    # GETリクエスト時は削除確認ページを表示
    return render(request, 'reservation_delete.html', {
        'reservation': reservation
    })