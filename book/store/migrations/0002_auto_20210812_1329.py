# Generated by Django 3.2.6 on 2021-08-12 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='photos',
        ),
        migrations.AddField(
            model_name='image',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.book'),
            preserve_default=False,
        ),
    ]
