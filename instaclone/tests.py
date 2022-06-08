from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.image = Image(image_name='image', image_caption='caption')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))
