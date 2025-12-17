import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advising_system.settings')
django.setup()

from django.contrib.auth.models import User
from advising_app.models import Student

username = '@mahid'
try:
    user = User.objects.get(username=username)
    try:
        student = Student.objects.get(user=user)
        print(f"Deleting existing student for {username}: ID={student.student_id}, Dept={student.department}")
        student.delete()
        print("Successfully deleted. You can now add the new student.")
    except Student.DoesNotExist:
        print(f"No conflicting student found for {username}. You should be able to add it.")
except User.DoesNotExist:
    print(f"User {username} not found")
