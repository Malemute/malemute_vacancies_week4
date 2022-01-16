"""malemute_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import MyLoginView
from accounts.views import MySignupView

from vacancies.views import CompanyView
from vacancies.views import MainView
from vacancies.views import MyCompanyCreateView
from vacancies.views import MyCompanyLetsStartView
from vacancies.views import MyCompanyVacancyCreateView
from vacancies.views import MyCompanyVacancyEditView
from vacancies.views import MyCompanyVacanciesView
from vacancies.views import MyCompanyView
from vacancies.views import ResumeEditView
from vacancies.views import ResumeView
from vacancies.views import SearchView
from vacancies.views import VacancyCatView
from vacancies.views import VacancyListView
from vacancies.views import VacancyInfoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main_page'),
    path('vacancies/', VacancyListView.as_view(), name='vacancies_page'),
    path('vacancies/cat/<str:category_name>', VacancyCatView.as_view(), name='category_page'),
    path('companies/<int:id>', CompanyView.as_view(), name='company_page'),
    path('vacancies/<int:id>', VacancyInfoView.as_view(), name='vacancy_info'),
    # path('vacancies/<int:id>', VacancyView.as_view(), name='vacancy_info'),

    path('mycompany/letsstart/', MyCompanyLetsStartView.as_view(), name='my_company_letsstart'),
    path('mycompany/create/', MyCompanyCreateView.as_view(), name='my_company_create'),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),

    path('mycompany/vacancies', MyCompanyVacanciesView.as_view(), name='my_company_vacancies'),

    path('mycompany/vacancies/<int:pk>', MyCompanyVacancyEditView.as_view(), name='my_company_vacancy_edit'),
    path('mycompany/vacancies/create/', MyCompanyVacancyCreateView.as_view(), name='my_company_vacancy_create'),

    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', MySignupView.as_view(), name='signup'),

    path('search/', SearchView.as_view(), name='search'),
    path('myresume/', ResumeView.as_view(), name='resume'),
    path('myresume/create/', ResumeEditView.as_view(), name='edit_resume'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
