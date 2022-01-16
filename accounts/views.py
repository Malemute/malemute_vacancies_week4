from django.contrib.auth.views import LoginView
from django.http import HttpResponseBadRequest, HttpResponseForbidden,  \
    HttpResponseNotFound, HttpResponseServerError
from django.views.generic import CreateView

from accounts.forms import SignupForm


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'


class MySignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super(MySignupView, self).form_valid(form)


def custom_handler400(request, exception):
    # Call when SuspiciousOperation raised
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    # Call when PermissionDenied raised
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')
