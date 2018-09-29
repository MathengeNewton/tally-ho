# Generated by Django 2.1.1 on 2018-09-27 22:46

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import tally_ho.libs.models.enums.disable_reason


class Migration(migrations.Migration):

    dependencies = [
        ('tally', '0002_auto_20180913_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tally',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('disable_reason', enumfields.fields.EnumIntegerField(enum=tally_ho.libs.models.enums.disable_reason.DisableReason, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ballot',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ballot',
            name='disable_reason',
            field=enumfields.fields.EnumIntegerField(default=None, enum=tally_ho.libs.models.enums.disable_reason.DisableReason, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='center',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='center',
            name='disable_reason',
            field=enumfields.fields.EnumIntegerField(enum=tally_ho.libs.models.enums.disable_reason.DisableReason, null=True),
        ),
        migrations.AddField(
            model_name='quarantinecheck',
            name='percentage',
            field=models.FloatField(default=100),
        ),
        migrations.AddField(
            model_name='resultform',
            name='clearance_printed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resultform',
            name='intake_printed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='station',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='station',
            name='disable_reason',
            field=enumfields.fields.EnumIntegerField(enum=tally_ho.libs.models.enums.disable_reason.DisableReason, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='resultform',
            name='barcode',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='resultform',
            name='serial_number',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ballot',
            name='tally',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ballots', to='tally.Tally'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='tally',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='candidates', to='tally.Tally'),
        ),
        migrations.AddField(
            model_name='center',
            name='tally',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='centers', to='tally.Tally'),
        ),
        migrations.AddField(
            model_name='office',
            name='tally',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='offices', to='tally.Tally'),
        ),
        migrations.AddField(
            model_name='resultform',
            name='tally',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='result_forms', to='tally.Tally'),
        ),
        migrations.AddField(
            model_name='subconstituency',
            name='tally',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sub_constituencies', to='tally.Tally'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='administrated_tallies',
            field=models.ManyToManyField(blank=True, default=None, related_name='administrators', to='tally.Tally'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tally',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='tally.Tally'),
        ),
        migrations.AlterUniqueTogether(
            name='center',
            unique_together={('code', 'tally')},
        ),
        migrations.AlterUniqueTogether(
            name='office',
            unique_together={('name', 'tally')},
        ),
        migrations.AlterUniqueTogether(
            name='resultform',
            unique_together={('barcode', 'tally'), ('serial_number', 'tally')},
        ),
    ]
