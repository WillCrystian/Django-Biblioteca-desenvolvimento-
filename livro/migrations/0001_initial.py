# Generated by Django 4.0.6 on 2022-07-19 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autenticacao', '0002_alter_usuario_senha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_livro', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('co_autor', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('data_cadastro', models.DateField()),
                ('emprestado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_anonimo', models.CharField(max_length=50)),
                ('data_emprestimo', models.DateField()),
                ('data_devolucao', models.DateField()),
                ('nome_livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livro')),
                ('usuario_cadastrado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.usuario')),
            ],
        ),
    ]
