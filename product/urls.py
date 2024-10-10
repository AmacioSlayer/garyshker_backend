from django.urls import path
from .views import ProductViewSet, ProductListView, PaymentViewSet, PaymentListView

urlpatterns = [
    path('products/', ProductListView.as_view({'get': 'list'}), name='product-list'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'get'}), name='product'),
    path('payments/', PaymentListView.as_view({'get': 'list'}), name='payments-list'),
    path('payments/<int:pk>/', PaymentViewSet.as_view({'get': 'get', 'post': 'authorize_payment'}), name='payment'),
]