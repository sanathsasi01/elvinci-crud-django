# Generated by Django 4.0.3 on 2022-03-30 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_alter_studentinstruments_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinstruments',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instruments', to='Student.students'),
        ),
    ]
