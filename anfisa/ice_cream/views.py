from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Asset')


def ice_cream_list(request):
    return HttpResponse('Asset list')


def ice_cream_detail(request, pk):
    return HttpResponse(f'Asset detail: {pk}')
