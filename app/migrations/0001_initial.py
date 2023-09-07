# Generated by Django 4.2.3 on 2023-09-05 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('ScName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ScPrincipal', models.CharField(max_length=100)),
                ('ScLocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Sname', models.CharField(max_length=100)),
                ('Sid', models.IntegerField(primary_key=True, serialize=False)),
                ('ScName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
    ]
