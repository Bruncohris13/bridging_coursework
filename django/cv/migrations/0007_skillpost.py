# Generated by Django 2.2.12 on 2020-06-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_qualificationpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
            ],
        ),
    ]
