from vacancies import data
from vacancies.models import Company, Specialty, Vacancy


def import_data():
    Vacancy.objects.all().delete()
    Specialty.objects.all().delete()
    Company.objects.all().delete()

    for speciality in data.specialties:
        Specialty.objects.create(
            code=speciality['code'],
            title=speciality['title'],
            # picture=f'media/speciality_images/specty_{speciality["code"]}.png',
            picture=f'specty_{speciality["code"]}.png',
        )

    for company in data.companies:
        Company.objects.create(
            name=company['title'],
            location=company['location'],
            description=company['description'],
            employee_count=company['employee_count'],
            # logo=f'media/company_images/logo{company["id"]}.png',
            logo=f'logo{company["id"]}.png',
        )

    for job in data.jobs:
        specialty = Specialty.objects.get(code=job['specialty'])
        id_comp = int(job['company']) - 1
        company = Company.objects.get(name=data.companies[id_comp]['title'])
        Vacancy.objects.create(
            title=job['title'],
            specialty=specialty,
            company=company,
            description=job['description'],
            salary_min=int(job['salary_from']),
            salary_max=int(job['salary_to']),
            published_at=job['posted'],
        )


if __name__ == '__main__':
    import_data()
