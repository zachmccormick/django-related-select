from django.conf.urls import url

from tests.test_views import TestRelatedSelectView

urlpatterns = [
    url(r'', TestRelatedSelectView.as_view(), name='test-view'),
]
