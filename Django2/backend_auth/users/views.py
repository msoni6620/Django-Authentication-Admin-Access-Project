
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if username and password:
                if User.objects.filter(username=username).exists():
                    return JsonResponse({"error": "Username already taken!"}, status=400)

                User.objects.create_user(username=username, password=password)
                return JsonResponse({"message": "User registered successfully!"}, status=201)
            return JsonResponse({"error": "Invalid data!"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    elif request.method == 'GET':
        return JsonResponse({"message": "Use POST to register a new user."})

    return JsonResponse({"error": "Method not allowed!"}, status=405)

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Simple validation
        if not username or not password:
            return JsonResponse({"error": "Username and password are required!"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already taken!"}, status=400)

        # Create the user
        User.objects.create_user(username=username, password=password)
        return JsonResponse({"message": "User registered successfully!"}, status=201)

    # For GET requests, show the registration form
    return render(request, 'register.html')
from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser  # Import CustomUser instead of User

def registerview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role', 'User')  # Get the role, default to 'User'

        # Simple validation
        if not username or not password:
            return JsonResponse({"error": "Username and password are required!"}, status=400)

        # Check if username already exists
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already taken!"}, status=400)

        # Create the user with the CustomUser model
        CustomUser.objects.create_user(username=username, password=password, role=role)
        return JsonResponse({"message": "User registered successfully!"}, status=201)

    # For GET requests, show the registration form
    return render(request, 'register.html')
from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')


# Admin-Only Access Example
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_view(request):
    if request.user.role != 'Admin':
        return Response({"error": "Access Denied"}, status=status.HTTP_403_FORBIDDEN)
    return Response({"message": "Welcome Admin!"}, status=status.HTTP_200_OK)

