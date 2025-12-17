import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advising_system.settings')
django.setup()

from django.contrib.auth.models import User
from advising_app.models import Student

username = '@mahid'
try:
    user = User.objects.get(username=username)
    print(f"User found: {user}")
    try:
        student = Student.objects.get(user=user)
        print(f"Student found for user {username}:")
        print(f"  ID: {student.student_id}")
        print(f"  Dept: {student.department}")
    except Student.DoesNotExist:
        print(f"No student found for user {username}")
except User.DoesNotExist:
    print(f"User {username} not found")
