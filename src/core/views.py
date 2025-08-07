import os
import zipfile
import shutil

from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.response import Response
from .services import gerar_cartoes_pdf


# Create your views here.
def getRoutes(request) :
    return JsonResponse('Our API', safe=False)

def upload_view(request):
    return render(request, 'upload.html')

class ProcessarCartoesView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        pdf_file = request.FILES.get('arquivo_pdf')
        lista_file = request.FILES.get('lista_presenca')
    
        if not pdf_file or not lista_file:
            return Response({'error': 'Envie arquivo_pdf e lista_presenca.'}, status=400)
    
        # Define o diretório de uploads (crie a pasta 'uploads' na raiz do projeto se não existir)
        upload_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'uploads')
        if os.path.exists(upload_dir):
            shutil.rmtree(upload_dir)
        os.makedirs(upload_dir, exist_ok=True)

        download_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'downloads')
        if os.path.exists(download_dir):
            shutil.rmtree(download_dir)
        os.makedirs(download_dir, exist_ok=True)

        pdf_path = os.path.join(upload_dir, pdf_file.name)
        lista_path = os.path.join(upload_dir, lista_file.name)
        output_dir = os.path.join(upload_dir, 'cartoes_gerados')

        # Salva arquivos recebidos
        with open(pdf_path, 'wb') as f:
            for chunk in pdf_file.chunks():
                f.write(chunk)
        with open(lista_path, 'wb') as f:
            for chunk in lista_file.chunks():
                f.write(chunk)

        # Processa os cartões
        gerar_cartoes_pdf.main(pdf_path, lista_path, output_dir)

        # Compacta os arquivos gerados
        zip_path = os.path.join(download_dir, 'cartoes.zip')
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for fname in os.listdir(output_dir):
                fpath = os.path.join(output_dir, fname)
                if os.path.isfile(fpath) and fname != 'cartoes.zip':
                    zipf.write(fpath, arcname=fname)

        return FileResponse(open(zip_path, 'rb'), as_attachment=True, filename='cartoes.zip')
