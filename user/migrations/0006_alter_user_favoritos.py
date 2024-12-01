# Generated by Django 5.0.7 on 2024-08-03 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0003_animal_idade'),
        ('user', '0005_alter_profileimage_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favoritos',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='adoptions.animal'),
        ),
    ]