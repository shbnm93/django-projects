from . import views
from django.urls import path


urlpatterns = [
    path('products/', views.get_products, name="products"),
    path('products/<str:pk>', views.get_product, name="get_product_details")
]



handler404 = 'utils.error_views.handler404'
handler500 = 'utils.error_views.handler500'