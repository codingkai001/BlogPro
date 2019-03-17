from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')


def post(request):
    return render_to_response('post_detail.html')


def preview_post(request):
    return render_to_response('preview_post.html')

