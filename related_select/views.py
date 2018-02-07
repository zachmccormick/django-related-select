from django.http import JsonResponse
from django.views.generic import View


class abstractstatic(staticmethod):
    __slots__ = ()

    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True

    __isabstractmethod__ = True


class RelatedSelectView(View):
    """
    AJAX GET view for related select form fields.  Expects a GET request to some URL similar to
    '/autocomplete-view/?value=123', where 123 will be passed into `filter()` to generate the list
    returned to populate the dependent select field
    """

    @abstractstatic
    def filter(value, **kwargs):
        return []

    @staticmethod
    def to_text(obj):
        return str(obj)

    @staticmethod
    def to_value(obj):
        return obj.id

    def dispatch(self, request, *args, **kwargs):
        if request.method != 'GET':
            raise NotImplementedError('This view only accepts GET requests')
        v = request.GET.get('value', None)
        ajax_list = []
        for model_instance in self.filter(v, user=request.user):
            ajax_list.append({'key': self.to_text(model_instance),
                              'value': self.to_value(model_instance)})
        return JsonResponse(ajax_list, safe=False)
