# Generated by Django 4.1.3 on 2022-11-19 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("developer", "Developer"),
                    ("manager", "Manager"),
                    ("admin", "Admin"),
                ],
                default="developer",
                max_length=255,
            ),
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=50)),
                ("date_created", models.DateField()),
                ("date_modified", models.DateField()),
                ("date_completed", models.DateField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("new task", "New Task"),
                            ("in development", "In Development"),
                            ("in qa", "In Qa"),
                            ("in code review", "In Code Review"),
                            ("ready for release", "Ready For Release"),
                            ("released", "Released"),
                            ("archived", "Archived"),
                        ],
                        default="new task",
                        max_length=20,
                    ),
                ),
                (
                    "task_creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creators",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "task_performer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="performers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("task", models.ManyToManyField(to="main.task")),
            ],
        ),
    ]
