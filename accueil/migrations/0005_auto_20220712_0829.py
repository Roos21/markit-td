# Generated by Django 3.2.13 on 2022-07-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0004_partenaire_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.TextField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.AlterField(
            model_name='partenaire',
            name='contact',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='partenaire',
            name='designation',
            field=models.TextField(max_length=150),
        ),
    ]
