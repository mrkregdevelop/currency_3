# Generated by Django 4.2.7 on 2023-12-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0007_alter_rate_currency_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('email', models.EmailField(max_length=128, verbose_name='Email')),
                ('subject', models.CharField(max_length=256, verbose_name='Subject')),
                ('body', models.CharField(max_length=2048, verbose_name='Body')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name': 'Rate', 'verbose_name_plural': 'Rates'},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'verbose_name': 'Source', 'verbose_name_plural': 'Sources'},
        ),
        migrations.AlterField(
            model_name='rate',
            name='buy',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Buy'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='currency_type',
            field=models.SmallIntegerField(choices=[(2, 'Dollar'), (1, 'Euro')], default=2, verbose_name='Currency type'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='sell',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sell'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.CharField(max_length=255, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Source'),
        ),
    ]