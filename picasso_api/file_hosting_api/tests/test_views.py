"""Views test module."""
import shutil

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.test import APITestCase
from rest_framework.test import override_settings


class FileUploaderViewTestCase(APITestCase):
    """Tests."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.file = SimpleUploadedFile(
            'test_file.mp4', content=b'test_content', content_type='audio/ogg'
        )
        cls.wrong_data = {'test_key': 'wrong_data'}
        cls.path = reverse('upload')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree('TEST_MEDIA_ROOT')
        super().tearDownClass()

    def test_wrong_data_responce_status(self):
        """Tests response status after sending wrong data."""
        response = self.client.post(path=self.path, data=self.wrong_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    @override_settings(MEDIA_ROOT='TEST_MEDIA_ROOT')
    def test_right_data_response_status(self):
        """Tests response status after sending clean data."""
        data = {'file': self.file}
        response = self.client.post(path=self.path, data=data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
