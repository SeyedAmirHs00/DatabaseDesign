# Generated by Django 4.2.8 on 2024-02-02 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_address_options_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]