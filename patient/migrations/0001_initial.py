# Generated by Django 4.2.11 on 2024-03-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'Female'), ('other', 'Other')], default='male')),
                ('mobile', models.IntegerField(null=True)),
                ('address', models.TextField(null=True)),
                ('Detail', models.TextField(null=True)),
                ('medicine_detail', models.TextField(null=True)),
                ('note', models.TextField(null=True)),
                ('next_visit', models.TextField(default=0)),
            ],
        ),
    ]
