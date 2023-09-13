from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import PersonSerializer
from .models import Person



class PersonView(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None):
        name = request.query_params.get('name')
        if name:
            persons = Person.objects.filter(name__icontains=name)
            serializer = PersonSerializer(persons, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        if id:
            human = Person.objects.get(id=id)
            serializer = PersonSerializer(human)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        humans = Person.objects.all()
        serializer = PersonSerializer(humans, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        human = Person.objects.get(id=id)
        serializer = PersonSerializer(human, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, id=None):
        human = get_object_or_404(Person, id=id)
        human.delete()
        return Response({"status": "success", "data": "Item Deleted"}, status=status.HTTP_200_OK)