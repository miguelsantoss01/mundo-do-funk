import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from funks.models import Funk

@require_http_methods(["GET", "POST", "PUT", "DELETE"])
@csrf_exempt
def FunkView(request):
    if request.method == 'GET':
        data = {"message": "GET request recebida meu camaradaaaaa"}
        return JsonResponse(data)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        funk = Funk(
            nome = data.get("nome"),
            artista = data.get("artista"),
            duracao = data.get("duracao"),
            descricao = data.get("descricao"),
            data = data.get("data"),
            logo = data.get("logo"),
        )
        funk.save()
        
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = {"message": "PUT request Matheus"}
        return JsonResponse(data)
    
    elif request.method == 'DELETE':
        data = {"message": "DELETE request Kaique"}
        return JsonResponse(data)
    
    else:
        return HttpResponseBadRequest("Unsupported request method")
