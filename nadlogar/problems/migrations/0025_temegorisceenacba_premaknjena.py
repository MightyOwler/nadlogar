# Generated by Django 3.2.16 on 2022-12-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0024_preseciscakroznic_temegorisceenacba'),
    ]

    operations = [
        migrations.AddField(
            model_name='temegorisceenacba',
            name='premaknjena',
            field=models.BooleanField(choices=[(True, 'Da'), (False, 'Ne')], default=False, help_text='Ali je elipsa premaknjena iz izhodišča?', verbose_name='premaknjena elipsa'),
        ),
    ]
