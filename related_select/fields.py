import json

from django.core.urlresolvers import resolve
from django.forms import ChoiceField


class RelatedChoiceField(ChoiceField):
    related_url = None
    related_dependent = None
    empty_label = None

    def __init__(self, related_url=None, related_dependent=None, empty_label=None, **kwargs):
        self.related_url = related_url
        self.related_dependent = related_dependent
        self.empty_label = empty_label if empty_label is not None else '--------'
        super(RelatedChoiceField, self).__init__(**kwargs)

    def widget_attrs(self, widget):
        return {
            'data-related-url': self.related_url,
            'data-related-dependent': self.related_dependent,
            'data-empty-label': self.empty_label
        }

    def init_bound_field(self, obj, request_user=None):
        class FakeRequest(object):
            method = 'GET'
            GET = {'value': obj}
            user = request_user
        resolver_match = resolve(self.related_url)
        response = resolver_match.func(FakeRequest())
        choices = []
        content = response.content.decode()
        for item in json.loads(content):
            choices.append((item['value'], item['key']))
        self.choices = choices

    def validate(self, value):
        # we can't do real validation here.
        return True
