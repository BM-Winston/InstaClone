from django.test import TestCase
from .models import Image, Comment, Profile, Follow

# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.image = Image(image_name='image', image_caption='caption')
        self.comment = Comment(comment_text='comment')

    def test_instance(self):
        self.assertTrue(isinstance(self.testUser, Image))

