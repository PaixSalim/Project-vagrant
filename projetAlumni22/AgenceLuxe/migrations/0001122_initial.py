# Generated by Django 5.0.7 on 2024-07-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('date_nais', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('date_empl', models.CharField(max_length=20)),
                ('poste', models.CharField(choices=[('manager', 'Manager'), ('developer', 'Developer'), ('designer', 'Designer'), ('analyst', 'Analyst')], max_length=20)),
            ],
        ),
    ]
