# Generated by Django 4.0 on 2022-01-07 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('location', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company_images')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('employee_count', models.IntegerField(blank=True, default=0, null=True)),
                ('owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=20, unique=True)),
                ('title', models.CharField(default='', max_length=40)),
                ('picture', models.ImageField(upload_to='specialty_images')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('skills', models.TextField(blank=True, default='', null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('salary_min', models.IntegerField(blank=True, null=True)),
                ('salary_max', models.IntegerField(blank=True, null=True)),
                ('published_at', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancies.company')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancies.specialty')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=40)),
                ('status', models.CharField(choices=[('NOT_LOOKING_FOR_JOB', 'Не ищу работу'), ('CONSIDERING_PROPOSALS', 'Рассматриваю предложения'), ('LOOKING_FOR_JOB', 'Ищу работу')], max_length=21)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('specialty', models.CharField(blank=True, max_length=40, null=True)),
                ('grade', models.CharField(blank=True, choices=[('TRAINEE', 'Стажер'), ('JUNIOR', 'Джуниор'), ('MIDDLE', 'Миддл'), ('SENOR', 'Сеньор'), ('LEAD', 'ЛИД')], max_length=7, null=True)),
                ('education', models.CharField(blank=True, max_length=250, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('portfolio', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resume', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=20)),
                ('written_phone', models.CharField(max_length=12)),
                ('written_cover_letter', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to='auth.user')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='vacancies.vacancy')),
            ],
        ),
    ]
