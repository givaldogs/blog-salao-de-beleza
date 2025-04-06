from django.urls import path
from blog.views import index, post, page, search_view  # Importe a função search_view aqui


app_name = 'blog'



urlpatterns = [
     path('', index, name='index'),
     path('post/<slug:slug>/', post, name='post'),
     path('page/', page, name='page'),
     path('page/<slug:slug>/', page, name='page'),
    # path('created_by/<int:author_pk>/', created_by, name='created_by'),
     #path('category/<slug:slug>/', category, name='category'),

]

'''
# meu
urlpatterns = [
    path('', index, name='index'),
    path('post/', post, name='post'),
    path('page/', page, name='page'),
    path('created_by/<int:pk>/', views.created_by, name='created_by'),
    path('search/', search_view, name='search'),  # Adicione a URL de busca
    
'''