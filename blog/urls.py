from django.urls import path
from .template_views import index, post, preview_post
from .api_views import get_all_blogs, get_all_categorys, get_blog, get_blog_set


urlpatterns = [
    # 模板部分url
    path('', index),
    path('post/', post),
    path('preview/', preview_post),
    # 接口部分url
    path('api/blog/get/all/', get_all_blogs),   # 所有博客列表
    path('api/category/get/all/', get_all_categorys),    # 所有标签列表
    path('api/blog/get/', get_blog),    # 获取指定博客(blog_id)
    path('api/blog_set/get/', get_blog_set),    # 获取指定博客集(category_id)
]
