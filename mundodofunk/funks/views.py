from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def api_view(request):
    if request.method == 'GET':
        data = {"message": "GET request recebida meu camarada"}
        return JsonResponse(data)
    
    elif request.method == 'POST':
        data = {"message": "POST request Davi"}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = {"message": "PUT request Matheus"}
        return JsonResponse(data)
    
    elif request.method == 'DELETE':
        data = {"message": "DELETE request Kaique"}
        return JsonResponse(data)
    
    else:
        return HttpResponseBadRequest("Unsupported request method")
