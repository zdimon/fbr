from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, RequestContext
from map.models import Cotter, Radiation, Vegetation
from djgeojson.views import GeoJSONLayerView
from djgeojson.serializers import Serializer as GeoJSONSerializer
# Create your views here.




def home(request):
    context = {}
    return render_to_response('index.html', context, RequestContext(request))


def radiation(request):
    context = {}
    return render_to_response('radiation.html', context, RequestContext(request))

def vegetation(request):
    context = {}
    return render_to_response('vegetation.html', context, RequestContext(request))



def cot(request):
    context = {}
    return render_to_response('cotter.html', context, RequestContext(request))

def slope(request):
    context = {}
    return render_to_response('slope.html', context, RequestContext(request))

def radiation_json(request):
    context = {}
    return render_to_response('radiation-json.html', context, RequestContext(request))


def vegetation_json(request):
    context = {}
    return render_to_response('vegetation-json.html', context, RequestContext(request))


class GetPolygonJsonCotter(GeoJSONLayerView):
    # Options
    from fbr.settings import BASE_DIR
    precision = 4   # float
    simplify = 0.5  # generalization
    def get_queryset(self):
        return Cotter.objects.all()

    def render_to_response(self, context, **response_kwargs):
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/cotter.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       precision=self.precision,
                       simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response


class GetPolygonJsonRadiation(GeoJSONLayerView):
    # Options
    from fbr.settings import BASE_DIR
    precision = 4   # float
    simplify = 0.5  # generalization
    def get_queryset(self):
        return Radiation.objects.all()

    def render_to_response(self, context, **response_kwargs):
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/radiation.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       precision=self.precision,
                       simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response






class GetPolygonJsonVegetation(GeoJSONLayerView):
    # Options
    from fbr.settings import BASE_DIR
    precision = 4   # float
    simplify = 0.5  # generalization
    def get_queryset(self):
        return Vegetation.objects.all()

    def render_to_response(self, context, **response_kwargs):
        from fbr.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/vegetation.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       precision=self.precision,
                       simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response

