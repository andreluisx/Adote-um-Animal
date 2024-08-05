# Generated by Django 5.0.7 on 2024-08-03 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0003_animal_idade'),
        ('user', '0002_alter_user_id_alter_user_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favoritos',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorited_by', to='adoptions.animal'),
        ),
    ]
