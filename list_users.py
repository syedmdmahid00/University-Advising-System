import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advising_system.settings')
django.setup()

from django.contrib.auth.models import User

print("All users:")
for u in User.objects.all():
    print(f"Username: '{u.username}', PK: {u.pk}")
