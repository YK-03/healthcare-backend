from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patients", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="created_by",
            field=models.ForeignKey(
                on_delete=models.CASCADE,
                related_name="patients",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]