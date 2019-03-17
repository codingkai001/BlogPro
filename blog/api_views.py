from django.http import HttpResponse
from .models import Blog, Category
from django.shortcuts import get_object_or_404
from django.core import serializers
from .serializers import CategorySerializer, BlogSerializer
import json
import time


def get_all_blogs(request):
    data = {}
    try:
        blogs = Blog.get_all()
        # many=True，序列化fields所有字段，否则抛出AttributeError
        blog_serializer = BlogSerializer(blogs, many=True)
        # fields = ('title', 'author', 'body', 'publish_date', 'read_nums', 'category')
        # data['data'] = serializers.serialize('json', blogs, fields=fields, ensure_ascii=False)
        data['data'] = blog_serializer.data
        data['status'] = 200

    except Exception as e:
        data['data'] = None
        data['status'] = 500
        record_errors(e)

    finally:
        response = HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json', charset='utf-8')
        return response


def get_all_categorys(request):
    data = {}
    try:
        categorys = Category.objects.all()
        # many=True，序列化fields所有字段，否则抛出AttributeError
        category_serializer = CategorySerializer(categorys, many=True)
        # data['data'] = serializers.serialize('json', categorys, ensure_ascii=False)
        # 获取序列化之后的数据
        data['data'] = category_serializer.data
        data['status'] = 200

    except Exception as e:
        data['data'] = None
        data['status'] = 500
        record_errors(e)

    finally:
        response = HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json', charset='utf-8')
        return response


def get_blog(request):
    data = {}
    try:
        bid = request.GET['bid']
        blog = Blog.objects.get(pk=bid)
        blog_serializer = BlogSerializer(blog, many=False)
        data['data'] = blog_serializer.data
        data['status'] = 200

    except (Blog.DoesNotExist, KeyError):
        data['data'] = 'Invalid parameter'
        data['status'] = 200
    except Exception as e:
        data['data'] = None
        data['status'] = 500
        record_errors(e)

    finally:
        response = HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json', charset='utf-8')
        return response


def get_blog_set(request):
    data = {}
    try:
        cid = request.GET['cid']
        blog = Blog.objects.filter(category=cid)
        blog_serializer = BlogSerializer(blog, many=True)
        data['data'] = blog_serializer.data
        data['status'] = 200

    except (Blog.DoesNotExist, KeyError):
        data['data'] = 'Invalid parameter'
        data['status'] = 200
    except Exception as e:
        data['data'] = None
        data['status'] = 500
        record_errors(e)

    finally:
        response = HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json', charset='utf-8')
        return response


def record_errors(e):
    with open("internal_errors.log", 'a+t', encoding="UTF-8") as f:
        f.write("[" + str(time.ctime()) + "]" + str(e) + "\n")
