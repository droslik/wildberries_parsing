from django.urls import path
from .views import GoodsApiView


urlpatterns = [
    path('goods', GoodsApiView.as_view(), name='goods'),
]
