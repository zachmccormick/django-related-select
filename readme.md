# django-related-select

The django-related-select module is designed to make ajax-powered select fields easy using Django forms.

## Installation

Install using pip:

    pip install django-related-select

Add to INSTALLED_APPS

     INSTALLED_APPS = [
         ...
         'related_select',
         ...
     ]

## Usage

### Form

    class MyForm(forms.Form):
        foo = forms.ChoiceField(choices=[('foo', 'foo')])
        bar = RelatedModelChoiceField(related_dependent='foo', related_url=reverse_lazy('my-related-select-view'))

### View

    class MyRelatedSelectView(RelatedSelectView):
        @staticmethod
        def filter(value, **kwargs):
            return SomeModel.objects.filter(related_model_id=value)
        
        @staticmethod
        def to_value(obj):
            # uses obj.id by default, but can return any valid value
            return obj.uuid
        
        @staticmethod
        def to_text(obj):
            # uses str(obj) by default, but can return any string
            return '({}) {}'.format(obj.id, obj.name)

### Template

    <html>
    ...
    {{ form.bar }}
    ...
    <script src='{% static "django-related-select.js" %}'></script>
    ...
    </html>
