from django.forms import ChoiceField


class RelatedChoiceField(ChoiceField):
    related_url = None
    related_dependent = None
    empty_label = None

    def __init__(self, related_url=None, related_dependent=None, empty_label=None):
        self.related_url = related_url
        self.related_dependent = related_dependent
        self.empty_label = empty_label if empty_label is not None else '--------'
        super(RelatedChoiceField, self).__init__()

    def widget_attrs(self, widget):
        return {
            'data-related-url': self.related_url,
            'data-related-dependent': self.related_dependent,
            'data-empty-label': self.empty_label
        }

    def validate(self, value):
        # we can't do real validation here.
        return True
