from django.test import TestCase, override_settings


# Sample - you can override any settings you require for your tests
# @override_settings(ROOT_URLCONF='django_view_models.tests.urls')
class MyTestCase(TestCase):
    def test_things_import_okay(self):
        import django_view_models.models
        import django_view_models.utils
