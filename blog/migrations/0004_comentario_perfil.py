# Generated by Django 4.0.2 on 2022-10-01 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_alter_perfil_foto'),
        ('blog', '0003_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='perfil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contas.perfil'),
        ),
    ]
