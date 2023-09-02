# Generated by Django 4.2.4 on 2023-09-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camisas_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalhes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('tamanho', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=5)),
            ],
        ),
        migrations.RenameModel(
            old_name='Expecificacoes',
            new_name='Camisa',
        ),
        migrations.DeleteModel(
            name='Atributos',
        ),
    ]