# Generated by Django 4.0 on 2022-02-10 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0016_alter_comentarios_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='comentario',
            field=models.TextField(),
        ),
    ]
