# Generated by Django 2.2 on 2019-04-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20190413_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='ISBN',
            new_name='isbn',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Publisher',
            new_name='publisher',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='DateRegistered',
            new_name='regdate',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='BookName',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='book',
            name='DatePublished',
        ),
        migrations.RemoveField(
            model_name='book',
            name='FrontPage',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Introduction',
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='images/2019-03-14.png', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='cover_url',
            field=models.URLField(default='images/2019-03-14.png'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='pubdate',
            field=models.CharField(default='unknown', max_length=20),
            preserve_default=False,
        ),
    ]
