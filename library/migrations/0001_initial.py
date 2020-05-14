# Generated by Django 3.0.5 on 2020-05-02 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name="author's name")),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name="book's title")),
                ('has_been_read', models.BooleanField(default=False, verbose_name="book's status")),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Author', verbose_name="book's author")),
            ],
        ),
    ]