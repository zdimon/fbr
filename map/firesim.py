from django.http import HttpResponse
from map.models import Burning, Radiation


def fire_init(request,gid):
    Burning.objects.all().delete()
    r = Radiation.objects.get(pk=gid)
    b = Burning()
    b.burning = 1
    b.day = 1
    b.time = 1
    b.geom = r.geom
    b.gridcode = r.gridcode
    b.save()
    for r in Radiation.objects.all():
        b = Burning()
        b.burning = 0
        b.day = 1
        b.time = 0
        b.geom = r.geom
        b.gridcode = r.gridcode
        b.save()
    html = 'Time: <input name="time" id="time_fire" value="1"> hour <a href="#" onclick="return false" id="firesim" > Go! </a>'
    return HttpResponse(html)


