from django.conf.urls import url

from .views import (
    searchproductview,
    )


urlpatterns = [
    url(r'^$', searchproductview, name='search'),
    ]
