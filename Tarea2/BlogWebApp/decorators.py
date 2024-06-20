from functools import wraps
from .models import UserActionLog

def log_user_action(action):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                UserActionLog.objects.create(user=request.user, action=action)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
