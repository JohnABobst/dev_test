from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'matcher': reverse('matcher:match-reports', request=request, format=format),
        'recordings': reverse('recordings:recordings-list', request=request, format=format),
        
    })
