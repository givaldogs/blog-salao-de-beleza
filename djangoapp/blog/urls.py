from django.urls import path
from blog.views import  PostDetailView, PageDetailView, CategoryListView, TagListView, SearchListView,   \
                        PostListView, CreatedByListView


app_name = 'blog'


urlpatterns = [
     path('', PostListView.as_view(), name='index'),
     path('post/<slug:slug>/', PostDetailView.as_view(), name='post'),
     path('page/<slug:slug>/', PageDetailView.as_view(), name='page'),
     path('created_by/<int:author_pk>/', CreatedByListView.as_view(), name='created_by'),
     path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
     path('tag/<slug:slug>/', TagListView.as_view(), name='tag'),
     path('search/', SearchListView.as_view(), name='search'),
     #path('avaliacao/', avaliacao_view, name='avaliacao'),
     #path('', index, name='index'),
     #path('page/<slug:slug>/', page, name='page'),
     # path('tag/<slug:slug>/', tag, name='tag'),
     #path('search/', search, name='search'),
      #path('category/<slug:slug>/', category, name='category'),
      #path('created_by/<int:author_pk>/', created_by, name='created_by'),
]