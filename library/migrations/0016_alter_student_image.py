# Generated by Django 5.0 on 2024-09-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(upload_to='student_images'),
        ),
    ]
