# Generated by Django 3.0.7 on 2020-11-10 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("testi", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Naloga",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("predloga_besedila_naloge", models.TextField(blank=True)),
                ("predloga_besedila_resitve", models.TextField(blank=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="naloge",
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="naloge",
                        to="testi.Test",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "naloge",
                "default_related_name": "naloge",
            },
        ),
        migrations.CreateModel(
            name="IskanjeNicelPolinoma",
            fields=[
                (
                    "naloga_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="naloge.Naloga",
                    ),
                ),
                ("stevilo_nicel", models.PositiveSmallIntegerField()),
                ("velikost_nicle", models.PositiveSmallIntegerField()),
            ],
            bases=("naloge.naloga",),
        ),
        migrations.CreateModel(
            name="KrajsanjeUlomkov",
            fields=[
                (
                    "naloga_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="naloge.Naloga",
                    ),
                ),
                ("najvecji_stevec", models.PositiveSmallIntegerField()),
                ("najvecji_imenovalec", models.PositiveSmallIntegerField()),
                ("najvecji_faktor", models.PositiveSmallIntegerField()),
            ],
            bases=("naloge.naloga",),
        ),
    ]
