# Generated by Django 4.0.6 on 2022-08-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0007_alter_emprestimo_avaliacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimo',
            options={'ordering': ['-data_emprestimo']},
        ),
        migrations.AddField(
            model_name='livro',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='capa_livro'),
        ),
    ]
