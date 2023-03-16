from django.shortcuts import render
from .models import Tutorial
from .serializers import TutorialSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# Create your views here.

@api_view(['GET', 'POST'])
def tutorial_list(request):
	# Get a list of tutorials
	if request.method == 'GET':
		all_tutorials = Tutorial.objects.all()
		serializer = TutorialSerializer(all_tutorials, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	elif request.method == 'POST':
		tutorial_data = JSONParser().parse(request)
		serializer = TutorialSerializer(data=tutorial_data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, id):
	try:
		tutorial = Tutorial.objects.get(pk=id)
	except Tutorial.DoesNotExist:
		return Response({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = TutorialSerializer(tutorial)
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	elif request.method == 'PUT':
		tutorial_data = JSONParser().parse(request)
		serializer = TutorialSerializer(tutorial, data=tutorial_data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		tutorial.delete()
		return Response({'message': 'Tutorial was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)