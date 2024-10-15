# Generated by Django 5.0.7 on 2024-08-04 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0004_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='department',
            field=models.CharField(choices=[('Cardiology', 'Cardiology'), ('Orthopedics', 'Orthopedics'), ('Neurology', 'Neurology'), ('Radiology', 'Radiology'), ('Surgery', 'Surgery'), ('Other', 'Other')], default='Other', max_length=50),
        ),
    ]