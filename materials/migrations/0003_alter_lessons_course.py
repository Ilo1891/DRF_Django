# Generated by Django 5.1.2 on 2024-11-05 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_lessons_course_lessons_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lessons",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to="materials.course",
                verbose_name="course",
            ),
        ),
    ]
