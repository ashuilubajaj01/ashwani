# Generated by Django 3.2 on 2021-06-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0003_promocodemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='discount',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
