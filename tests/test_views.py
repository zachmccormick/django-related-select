try:
    from django.urls import reverse_lazy
except:
    from django.core.urlresolvers import reverse_lazy
from django.test import TestCase, Client

from related_select.views import RelatedSelectView


class ClsTestRelatedSelectView(RelatedSelectView):
    @staticmethod
    def filter(value, **kwargs):
        assert kwargs.get('user') is not None
        assert value == 'xyz'
        return ['example']

    @staticmethod
    def to_value(obj):
        return 'value'


class ViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        from . import configure
        configure()
        super().setUpClass()

    def test_foo(self):
        c = Client()
        r = c.get(reverse_lazy('test-view'), data={'value': 'xyz'})
        self.assertEqual(r.status_code, 200)
        options = r.json()
        self.assertEqual(len(options), 1)
        self.assertEqual(options[0]['key'], 'example')
        self.assertEqual(options[0]['value'], 'value')
