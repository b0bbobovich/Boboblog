from django.urls import path
from . import views as my_views

urlpatterns = [
    path('', my_views.Home.as_view(), name='home'),
    path('article/<int:pk>/', my_views.ArticleDetail.as_view(), name='article-detail'),
    path('add_post/', my_views.AddPost.as_view(), name='add-post'),
    path('article/edit/<int:pk>/', my_views.UpdatePost.as_view(), name='update-post'),
    path('article/<int:pk>/remove/', my_views.DeletePost.as_view(), name='delete-post'),
    path('add_category/', my_views.AddCategory.as_view(), name='add-category' ),
    path('category/<str:catg_name>/', my_views.Category, name='category'),
    path('category-list/', my_views.CategoryList, name='category-list'),
    path('like/<int:pk>/', my_views.Like, name='like-post'),
]
