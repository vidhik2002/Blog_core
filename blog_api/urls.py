from django.urls import path
from .views import PostList, PostDetail
app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name="createdetails"),
    path('', PostList.as_view(), name="createlist"),

]
