# Generated by Django 4.0.4 on 2022-05-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_alter_receita_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='descricao',
            field=models.CharField(max_length=200, unique_for_month='data'),
        ),
    ]
