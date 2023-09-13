from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import PersonSerializer
from .models import Person
from rest_framework.serializers import ValidationError


class CreatePersonView(APIView):
    def post(self, request):

        for key, value in request.data.items():
            if type(value) != type("str"):
                raise ValidationError({"status": "error", "data": f"{key} must be a string"})

        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class PersonView(APIView):
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
        
    def delete(self, request, id=None):
        human = get_object_or_404(Person, id=id)
        human.delete()
        return Response({"status": "success", "data": "Item Deleted"}, status=status.HTTP_200_OK)
    
    
class NameView(APIView):
    def post(self, request):

        for key, value in request.data.items():
            if type(value) != type("str"):
                raise ValidationError({"status": "error", "data": f"{key} must be a string"})

        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, nameid=None):
        if nameid:
            persons = Person.objects.filter(name__icontains=nameid)
            serializer = PersonSerializer(persons, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        humans = Person.objects.all()
        serializer = PersonSerializer(humans, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, nameid=None):
        human = Person.objects.get(id=nameid)
        serializer = PersonSerializer(human, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, nameid=None):
        human = get_object_or_404(Person, id=nameid)
        human.delete()
        return Response({"status": "success", "data": "Item Deleted"}, status=status.HTTP_200_OK)