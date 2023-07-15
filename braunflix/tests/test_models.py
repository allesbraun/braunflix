from django.test import TestCase

from braunflix.models import Program


class ProgramModelTestCase(TestCase):
    
    def setUp(self):
        self.program = Program(
            title = 'Fight Club',
            release_date = '1999-10-29'
        )
        
    def test_verify_program_atributes(self):
        """Test that verifies the atributes of a program with default values"""
        self.assertEqual(self.program.title, 'Fight Club')
        self.assertEqual(self.program.kind, 'F')
        self.assertEqual(self.program.release_date, '1999-10-29')
        self.assertEqual(self.program.likes, 0)
        self.assertEqual(self.program.dislikes, 0)
        