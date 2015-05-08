from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, RequestContext
# Create your views here.

def home(request):
    context = {}
    return render_to_response('index.html', context, RequestContext(request))

