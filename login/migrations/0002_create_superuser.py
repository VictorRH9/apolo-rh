from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='admin').exists():
        User.objects.create(
            username='admin',
            email='admin@example.com',
            is_staff=True,
            is_superuser=True,
            password=make_password('admin123'),
        )

class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0001_initial'),
        ('login', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_admin),
    ]
