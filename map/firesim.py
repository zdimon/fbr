from django.http import HttpResponse

def fire_init(request):
    html = 'Time:<input name="time">'
    return HttpResponse(html)


