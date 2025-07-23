def auth_context(request):
    return {
        'is_authenticated': 'user_id' in request.session
    }