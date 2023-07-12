# Generated by Django 4.2 on 2023-07-12 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=20)),
                ('address2', models.CharField(max_length=20)),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=60)),
                ('website', models.CharField(max_length=20)),
                ('logo', models.ImageField(upload_to='logos')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry_source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquirysourcename', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Follow_up_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followupstatusname', models.CharField(max_length=30)),
                ('followupstatus', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Master_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('enquirysourcename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.enquiry_source')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=60)),
                ('address', models.CharField(max_length=25)),
                ('street', models.CharField(max_length=25)),
                ('pincode', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=20)),
                ('alternative_email', models.EmailField(max_length=25)),
                ('alternative_address', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.district')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.state')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.state'),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=25)),
                ('branchcode', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=60)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.district')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.state')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer', models.CharField(choices=[('trainer1', 'trainer1'), ('trainer2', 'trainer2'), ('trainer3', 'trainer3')], max_length=25)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.course')),
            ],
        ),
        migrations.CreateModel(
            name='Academic_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=25)),
                ('year_of_pass', models.CharField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2008'), ('2009', '2010'), ('2011', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], max_length=15)),
                ('roll_no', models.CharField(max_length=20)),
                ('registration_no', models.CharField(max_length=20)),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.qualification')),
            ],
        ),
    ]