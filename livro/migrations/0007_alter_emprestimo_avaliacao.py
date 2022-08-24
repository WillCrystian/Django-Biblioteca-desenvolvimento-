# Generated by Django 4.0.6 on 2022-08-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0006_alter_emprestimo_options_emprestimo_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='avaliacao',
            field=models.CharField(choices=[('B', 'Bom'), ('M', 'Médio'), ('R', 'Ruim')], default='', max_length=1),
        ),
    ]
