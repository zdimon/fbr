from django.http import HttpResponse
from map.models import Burning, Radiation


def fire_init(request):
    Burning.objects.all().delete()
    r = Radiation.objects.get(pk=request.GET['gid'])
    b = Burning()
    b.burning = 1
    b.day = 1
    b.time = 1
    b.save()
    html = 'Time:<input name="time">'
    return HttpResponse(html)


