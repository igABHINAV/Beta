from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import websocket
from django.shortcuts import render
# Create your views here.


@api_view(['POST'])
def send_request(request):
    method = request.data.get('method')
    url = request.data.get('url')
    headers = request.data.get('headers', {})
    data = request.data.get('data', {})
    try:
        if method == 'websocket':
            ws = websocket.WebSocket()
            ws.connect(url, header=headers)
            ws.send(data)
            content = ws.recv()
            ws.close()
            return Response({
                'content': content
            })
        else:
            response = requests.request(method, url, headers=headers, data=data)
            content = response.content
            return Response({
                'status_code': response.status_code,
                'headers': dict(response.headers),
                'content': content
            })
    except requests.exceptions.RequestException as e:
        return Response({
            'error': str(e)
        }, status=400)
    

    
def index(req) :
    return render(req , 'index.html')
