# Generated by Django 4.2.6 on 2023-10-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='Images/None/sampleimg.png', upload_to='Images'),
        ),
    ]