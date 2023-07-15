from django.test import TestCase

from braunflix.models import Program
from braunflix.serializers import ProgramSerializer


class ProgramSerializerTestCase(TestCase):
    
    def setUp(self):
        self.program = Program(
            title = 'Fight Club',
            release_date = '1999-10-29',
            kind = 'F',
            likes = 12345,
            dislikes = 23
        )
        self.serializer = ProgramSerializer(instance = self.program)
        
    def test_verify_serialized_fields(self):
        """Test that verifies the fields being serialized"""
        
        data = self.serializer.data
        
        self.assertEqual(set(data.keys()), set(['title', 'kind', 'release_date', 'likes']))
        
    def test_verify_content_of_serialized_fields(self):
        """Test that verifies the content of the serialized fields"""
        
        data = self.serializer.data
        
        self.assertEqual(self.program.title, data['title'])
        self.assertEqual(self.program.kind, data['kind'])
        self.assertEqual(self.program.release_date, data['release_date'])
        self.assertEqual(self.program.likes, data['likes'])

        