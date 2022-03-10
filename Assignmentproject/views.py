from rest_framework import mixins
from rest_framework import generics
from Assignmentproject.models import router_details
from Assignmentproject.serializers import router_detailsserializer
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated



class router_detailsAPIView(mixins.ListModelMixin, 
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):

    queryset = router_details.objects.all()
    serializer_class = router_detailsserializer
    permission_classes =(IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class router_detailAPIView(generics.RetrieveAPIView,mixins.ListModelMixin, 
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin):
    serializer_class = router_detailsserializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)    

def jsonmethod(request):
    data={
        'Sapid':1,
        'Hostname':"kuldeep",
        'Loopback':"192.168.172.78",
        'Macaddress':'98:01:7e:40:95:pa',
    }
    dataserializer= router_details.objects.all()
    response={'router':list(dataserializer.values('Sapid','Hostname'))}
    return JsonResponse(response)

    
        
    
        
    