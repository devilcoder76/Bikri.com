from django.urls import path
from . import views
app_name='products'

urlpatterns =[
    path("productsample/",views.sample,name="productsample"),
    path('',views.view_products,name="view_product"),
    path('product/<int:pk>',views.view_product_single,name="view_product_single"),
    path('order/<int:pk>',views.order_product,name="order_product"),
    path('sell/',views.sell_product,name="sell_product"),
    path('orders/',views.view_orders,name="view_orders"),
    path('sellerlist/',views.view_listed_products,name="listed_products"),
    path('sellerorder/',views.seller_orders,name="seller_orders"),
    path('cart/',views.cart_view,name="view_cart")
]
