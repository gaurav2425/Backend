# Generated by Django 3.1.7 on 2021-03-19 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0071_auto_20210318_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='description',
        ),
        migrations.RemoveField(
            model_name='trending',
            name='description',
        ),
        migrations.AddField(
            model_name='hot',
            name='dateint',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='hot',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=20),
        ),
        migrations.AddField(
            model_name='hot',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='hot',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='March', max_length=20),
        ),
        migrations.AddField(
            model_name='hot',
            name='now',
            field=models.TimeField(default='00:10:39'),
        ),
        migrations.AddField(
            model_name='hot',
            name='para1',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='hot',
            name='para2',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='hot',
            name='para3',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='hot',
            name='para4',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='hot',
            name='para5',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='hot',
            name='para6',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='hot',
            name='para7',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='hot',
            name='subtitle',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='hot',
            name='videosrc',
            field=models.CharField(default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300),
        ),
        migrations.AddField(
            model_name='hot',
            name='youtubevideo',
            field=models.CharField(default='null', max_length=300),
        ),
        migrations.AddField(
            model_name='new',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='new',
            name='dateint',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='new',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=20),
        ),
        migrations.AddField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='new',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='March', max_length=20),
        ),
        migrations.AddField(
            model_name='new',
            name='now',
            field=models.TimeField(default='00:10:39'),
        ),
        migrations.AddField(
            model_name='new',
            name='para1',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='new',
            name='para2',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='new',
            name='para3',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='new',
            name='para4',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='new',
            name='para5',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='new',
            name='para6',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='new',
            name='para7',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='new',
            name='subtitle',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='new',
            name='videosrc',
            field=models.CharField(default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300),
        ),
        migrations.AddField(
            model_name='new',
            name='youtubevideo',
            field=models.CharField(default='null', max_length=300),
        ),
        migrations.AlterField(
            model_name='hot',
            name='name',
            field=models.CharField(default='trending', max_length=120),
        ),
        migrations.AlterField(
            model_name='new',
            name='name',
            field=models.CharField(default='trending', max_length=120),
        ),
        migrations.AlterField(
            model_name='trending',
            name='now',
            field=models.TimeField(default='00:10:39'),
        ),
    ]
