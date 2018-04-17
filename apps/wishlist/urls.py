from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="dashboard"),
    url(r'^wish_items/create$', views.create, name="create_item"),
    url(r'^addwish/(?P<item_id>[0-9]+)$', views.add_wish, name="add_wish"),
    url(r'^removewish/(?P<item_id>[0-9]+)$', views.remove_wish, name="remove_wish"),
    url(r'^wish_items/(?P<item_id>[0-9]+)$', views.show_item, name="show"),
    url(r'^delete/(?P<item_id>[0-9]+)$', views.delete, name="delete")
]