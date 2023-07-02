# Generated by Django 4.2.1 on 2023-06-11 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MetaGamificada', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metagamificada',
            name='id_usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='possui', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]