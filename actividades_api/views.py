from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from firebase_admin import db
from datetime import datetime


class ActividadesAPI(APIView):
    name = "actividades api"
    collection_name = "actividades"

    def get(self, request):

        ref = db.reference(f'{self.collection_name}')

        data = ref.get()

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data

        if 'titulo' not in data or 'descripcion' not in data or 'responsable' not in data:
            return Response({'error': 'faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

        ref = db.reference(f'{self.collection_name}')

        current_time  = datetime.now()
        custom_format = current_time.strftime("%d/%m/%Y, %I:%M:%S %p").lower().replace('am', 'a. m.').replace('pm', 'p. m.')
        data.update({"fecha_creacion": custom_format})

        new_resource = ref.push(data)

        return Response({"id": new_resource.key}, status=status.HTTP_201_CREATED)
