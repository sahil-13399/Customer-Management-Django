# Generated by Django 2.2.14 on 2020-07-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]
