# Generated by Django 4.0.2 on 2022-04-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantooapi', '0003_interesttag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesttag',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
