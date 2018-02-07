from django import forms
from django.core.urlresolvers import reverse_lazy
from django.template import Template, Context
from django.test import TestCase

from related_select.fields import RelatedChoiceField


class ClsTestForm(forms.Form):
    foo = forms.ChoiceField(choices=[('foo', 'foo')])
    bar = RelatedChoiceField(related_dependent='foo', related_url=reverse_lazy('test-view'))


class FieldTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        from . import configure
        configure()
        super().setUpClass()

    def test_field(self):
        template = Template('{{ form.bar }}')
        context = Context({'form': ClsTestForm()})
        self.assertTrue('data-related-dependent="foo"' in template.render(context))
        self.assertTrue('data-related-url="/"' in template.render(context))
