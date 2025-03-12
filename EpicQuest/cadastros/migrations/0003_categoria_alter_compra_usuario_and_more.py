# Generated by Django 5.1.3 on 2025-03-12 11:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_compra_itemcompra'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.compra'),
        ),
        migrations.AlterField(
            model_name='itemcompra',
            name='jogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.jogo'),
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')])),
                ('comentario', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.jogo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jogo',
            name='categorias',
            field=models.ManyToManyField(to='cadastros.categoria'),
        ),
    ]
