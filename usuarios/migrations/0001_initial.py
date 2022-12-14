# Generated by Django 4.1.4 on 2022-12-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('client', 'client'), ('assistant', 'assistant'), ('administrator', 'administrator')], default='client', max_length=15)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
