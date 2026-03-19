from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .bfs import buscar_solucion_BFS, obtener_camino

# Grafo (puedes moverlo a DB después)
CONEXIONES = {
    'JILOYORK': ['CELAYA', 'CDMX', 'QUERÉTARO'],
    'SONORA': ['ZACATECAS', 'SINALOA'],
    'GUANAJUATO': ['AGUASCALIENTES'],
    'OAXACA': ['QUERÉTARO'],
    'SINALOA': ['CELAYA', 'SONORA', 'JILOYORK'],
    'CDMX': ['MONTERREY'],
    'CELAYA': ['JILOYORK', 'SINALOA'],
    'ZACATECAS': ['SONORA', 'MONTERREY', 'QUERÉTARO'],
    'MONTERREY': ['ZACATECAS'],
    'TAMAULIPAS': ['QUERÉTARO'],
    'QUERÉTARO': ['TAMAULIPAS', 'ZACATECAS', 'SINALOA', 'JILOYORK', 'OAXACA']
}


@csrf_exempt
def buscar_ruta(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            estado_inicial = data.get('inicio')
            solucion = data.get('destino')

            if not estado_inicial or not solucion:
                return JsonResponse({
                    'error': 'Debes enviar "inicio" y "destino"'
                }, status=400)

            nodo_solucion = buscar_solucion_BFS(
                CONEXIONES,
                estado_inicial,
                solucion
            )

            camino = obtener_camino(nodo_solucion, estado_inicial)

            return JsonResponse({
                'ruta': camino,
                'encontrado': len(camino) > 0
            })

        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)