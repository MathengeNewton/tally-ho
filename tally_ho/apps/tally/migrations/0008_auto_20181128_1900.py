# Generated by Django 2.1.1 on 2018-11-28 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tally', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ballot',
            name='available_for_release',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ballot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='tally.Ballot'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='center',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='tally.Center'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='tally.Station'),
        ),
    ]
