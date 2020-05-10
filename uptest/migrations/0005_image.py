# Generated by Django 3.0.3 on 2020-05-07 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uptest', '0004_remove_projectinfo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='media/images/%Y/%m/%d')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uptest.Project')),
            ],
        ),
    ]