# Generated by Django 4.1.6 on 2023-03-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
