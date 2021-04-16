from django.test import TestCase
from social.forms import CreatePostForm

class TestCreatePostForm(TestCase):

    def test_invalid_data_to_form(self):

        data = {
            'content': "This is a new post!"
        }

        form = CreatePostForm(data=data)
        result = form.is_valid()

        self.assertFalse(result)


    def test_valid_data_to_form(self):

        data = {
            'content': "This is a new post!"
        }

        form = CreatePostForm(data=data)
        result = form.is_valid()

        self.assertTrue(result)

        instance = form.save()
        self.assertIsNotNone(instance)
        self.assertEqual(instance.content, data['content'])

