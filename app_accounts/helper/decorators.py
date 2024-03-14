from django.shortcuts import redirect


def logout_required(redirect_to):
    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper


def create_view_logout_required(redirect_to):
    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(classBaseView, *args, **kwargs):
            if classBaseView.request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(classBaseView, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper