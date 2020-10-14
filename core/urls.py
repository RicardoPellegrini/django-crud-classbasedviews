from django.urls import path
from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('add/', CreateProdutoView.as_view(), name='add_produto'),
  path('<int:id>/update/', UpdateProdutoView.as_view(), name='update_produto'),
  path('<int:id>/delete/', DeleteProdutoView.as_view(), name='delete_produto'),
]
