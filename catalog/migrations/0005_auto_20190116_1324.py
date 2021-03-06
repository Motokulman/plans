# Generated by Django 2.1.4 on 2019-01-16 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('catalog', '0004_auto_20190116_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a consumer name', max_length=200)),
                ('register_date', models.DateField(blank=True, null=True)),
                ('visits', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Visit')),
            ],
            options={
                'ordering': ['register_date', 'name'],
            },
        ),
        migrations.RenameModel(
            old_name='Author',
            new_name='Architect',
        ),
        migrations.RenameModel(
            old_name='CompanyUser',
            new_name='Contractor',
        ),
        migrations.RemoveField(
            model_name='privateuser',
            name='visits',
        ),
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ['approve_date'], 'permissions': (('can_mark_approved', 'Set plan as approved'),)},
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='release_date',
            new_name='apply_date',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='author',
            new_name='architect',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='company_user',
            new_name='contractor',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='finalized',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='private_user',
        ),
        migrations.AddField(
            model_name='plan',
            name='approve_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='approved',
            field=models.BooleanField(default=False, help_text='True, if this is moderated approved plan'),
        ),
        migrations.DeleteModel(
            name='PrivateUser',
        ),
        migrations.AddField(
            model_name='plan',
            name='consumer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Consumer'),
        ),
    ]
