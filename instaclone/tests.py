from django.test import TestCase
from .models import Image, Comment, Profile, Follow, Like

# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.image_test = Image(image_name='image', image_caption='caption')
        self.comment = Comment(comment_text='comment')

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.save_image()
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_caption(self):
        self.image_test.save_image()
        self.image_test.update_caption('new caption')
        self.assertTrue(self.image_test.image_caption == 'new caption')

class CommentTestClass(TestCase):
    def setUp(self):
        self.comment = Comment(comment_text='comment')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comment(self):
        self.comment.save_comment()
        self.comment.delete_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 0)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(profile_photo='profile', profile_bio='bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile('new profile')
        self.assertTrue(self.profile.profile_bio == 'new profile')

class FollowTestClass(TestCase):
    def setUp(self):
        self.follow = Follow(follow_user='user')

    def test_instance(self):
        self.assertTrue(isinstance(self.follow, Follow))

    def test_save_follow(self):
        self.follow.save_follow()
        follows = Follow.objects.all()
        self.assertTrue(len(follows) > 0)

    def test_delete_follow(self):
        self.follow.save_follow()
        self.follow.delete_follow()
        follows = Follow.objects.all()
        self.assertTrue(len(follows) == 0)

class LikeTestClass(TestCase):
    def setUp(self):
        self.like = Like(like_user='user')

    def test_instance(self):
        self.assertTrue(isinstance(self.like, Like))

    def test_save_like(self):
        self.like.save_like()
        likes = Like.objects.all()
        self.assertTrue(len(likes) > 0)

    def test_delete_like(self):
        self.like.save_like()
        self.like.delete_like()
        likes = Like.objects.all()
        self.assertTrue(len(likes) == 0)


    

