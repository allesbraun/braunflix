from django.test import TestCase

from braunflix.models import Program


class FixturesDataTestCase(TestCase):
    
    fixtures = ['initial_programs']
    
    def test_verify_fixture_load(self):
        """Test that verifies the loading of the fixture"""
        stranger_program = Program.objects.get(pk=1)
        all_programs = Program.objects.all()
        self.assertEqual(stranger_program.title, 'Stranger Things')
        self.assertEqual(len(all_programs), 8)
        