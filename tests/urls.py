from django.conf.urls import url

from tests.test_views import ClsTestRelatedSelectView

urlpatterns = [
    url(r'', ClsTestRelatedSelectView.as_view(), name='test-view'),
]
