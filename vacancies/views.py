from django.contrib.auth.views import LoginView
from django.db.models import Count, Q
from django.http import HttpResponseBadRequest, HttpResponseForbidden,  \
    HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from vacancies.forms import SignupForm
from vacancies.models import Company, Specialty, Vacancy


class MainView(View):
    def get(self, request, *args, **kwargs):
        specialties = Specialty.objects.all().annotate(number_of_vacancies=Count('vacancies'))
        companies = Company.objects.all()
        return render(request, 'vacancies/index.html', context={'specialties': specialties, 'companies': companies})


class CompanyView(View):
    def get(self, request, id, *args, **kwargs):
        company = get_object_or_404(Company, pk=id)
        vacancies = Vacancy.objects.filter(company=company)

        return render(
            request,
            'vacancies/company.html',
            context={'vacancies': vacancies, 'company': company})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'vacancies/login.html'


class MySignupView(CreateView):
    form_class = SignupForm
    template_name = 'vacancies/signup.html'
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super(MySignupView, self).form_valid(form)


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        return context


class VacancyCatView(View):
    def get(self, request, category_name):
        category_name = get_object_or_404(Specialty, code=category_name)
        vacancies = Vacancy.objects.filter(specialty=category_name)
        return render(
            request,
            'vacancies/vacancies.html',
            context={'category': category_name, 'vacancies': vacancies})


class SearchView(View):
    def get(self, request):
        search = request.GET.get('s', '')
        vacancies = Vacancy.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if vacancies:
            return render(request, 'vacancies/vacancy-list.html', context={'vacancies': vacancies})
        else:
            return render(request, 'not-found404.html')

class VacancyView(View):
    def get(self, request, id):
        vacancy = get_object_or_404(Vacancy, id=id)
        company = Company.objects.get(id=vacancy.company.id)
        return render(
            request,
            'vacancies/vacancy.html',
            context={
                'vacancy': vacancy,
                'company': company
            }
        )


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
