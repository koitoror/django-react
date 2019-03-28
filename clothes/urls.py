from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/clothes/$',
        views.get_post_clothes,
        name='get_post_clothes'
    ),
    url(
        r'^api/v1/clothes/(?P<pk>[0-9]+)$',
        views.get_delete_update_clothes,
        name='get_delete_update_clothes'
    )
]