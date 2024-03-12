# Generated by Django 4.0.2 on 2022-02-22 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("label_types", "0006_auto_20220222_0512"),
        ("examples", "0002_alter_example_project"),
        ("labels", "0006_rename_relation_relationold"),
    ]

    operations = [
        migrations.CreateModel(
            name="RelationNew",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("prob", models.FloatField(default=0.0)),
                ("manual", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "direction",
                    models.CharField(
                        choices=[("left", "left"), ("right", "right"), ("undirected", "undirected")],
                        default="undirected",
                        max_length=10,
                    ),
                ),
                (
                    "example",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="relations", to="examples.example"
                    ),
                ),
                (
                    "from_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="from_relations", to="labels.span"
                    ),
                ),
                (
                    "to_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="to_relations", to="labels.span"
                    ),
                ),
                ("type", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="label_types.relationtype")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
