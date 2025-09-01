from django.http import HttpResponse
import asyncio

# View assíncrona
async def contador_view(request):
    resposta = "<h1>Contador Assíncrono</h1>"
    for i in range(1, 11):
        resposta += f"Segundos passados: {i}<br>"
        await asyncio.sleep(1)  
    return HttpResponse(resposta)
