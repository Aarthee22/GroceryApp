# Generated by Django 4.1.7 on 2023-03-24 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("groceries_new", "0002_registereduser_profilepic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registereduser",
            name="profilePic",
            field=models.ImageField(default="default.jpg", upload_to="profile_pics"),
        ),
    ]
