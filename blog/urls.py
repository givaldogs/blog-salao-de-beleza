from django.urls import path
from blog.views import index, post, page, search_view  # Importe a função search_view aqui


app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/', post, name='post'),
    path('page/', page, name='page'),
    path('search/', search_view, name='search'),  # Adicione a URL de busca
    
]
