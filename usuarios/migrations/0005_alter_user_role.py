# Generated by Django 4.1.4 on 2022-12-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('client', 'client'), ('assistant', 'assistant'), ('administrator', 'administrator')], default='client', max_length=13),
        ),
    ]
