from datetime import timedelta

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        future_question = Question(pub_date=timezone.now() + timedelta(days=30))
        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        old_question = Question(pub_date=timezone.now() - timedelta(days=30))
        self.assertFalse(old_question.was_published_recently())

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        recent_question = Question(pub_date=timezone.now() - timedelta(hours=1))
        self.assertTrue(recent_question.was_published_recently())
