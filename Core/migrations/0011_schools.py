# Generated by Django 4.2.4 on 2023-12-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0010_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Image', models.ImageField(null=True, upload_to='Partners')),
            ],
        ),
    ]
