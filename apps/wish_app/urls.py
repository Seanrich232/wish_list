from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^add$', views.add),
    url(r'^createWish$', views.createWish),
    url(r'^joinWishlist/(?P<wish_id>\d+)', views.joinWishlist),
    url(r'^delete/(?P<wish_id>\d+)', views.delete),
    url(r'^remove/(?P<wish_id>\d+)', views.remove),
    url(r'^wish_item/(?P<wish_id>\d+)', views.wish_item)
]