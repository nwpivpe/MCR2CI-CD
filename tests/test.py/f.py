# app/tests/test_models.py
from django.test import TestCase
from .models import Course

class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(name="Python", description="Basic Python")
        self.assertEqual(course.name, "Python")
