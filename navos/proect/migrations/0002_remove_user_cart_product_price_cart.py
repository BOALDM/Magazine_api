# Generated by Django 5.0.6 on 2024-05-14 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proect', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cart',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proect.user')),
                ('products', models.ManyToManyField(to='proect.product')),
            ],
        ),
    ]
