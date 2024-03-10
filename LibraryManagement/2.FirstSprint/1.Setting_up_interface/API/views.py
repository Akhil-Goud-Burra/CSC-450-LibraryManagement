from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
#########################################################################################################################
# End User Authentication:
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class EndUser_Authentication(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        if not request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authenticated as an end user."}, status=status.HTTP_200_OK)
        
        else:
            return Response({"message": "You are Not Authenticated as an end user."}, status=status.HTTP_403_FORBIDDEN)
##############################################################################################################

#########################################################################################################################
# Admin User Authentication:
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class AdminUser_Authentication(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authenticated as an Admin user."}, status=status.HTTP_200_OK)
        
        else:
            return Response({"message": "You are Not Authenticated as an Admin user."}, status=status.HTTP_403_FORBIDDEN)
##############################################################################################################
# Adding Enduser to Admin User Group and removing from Admin Group 
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User,Group
from django.shortcuts import get_object_or_404

@api_view(['POST', 'DELETE'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']

    if username:
        user = get_object_or_404(User, username=username)
        managers_group = Group.objects.get(name="Manager")

        if request.method == 'POST':
            managers_group.user_set.add(user)
            return Response({"message": "User Added"})
        
        elif request.method == 'DELETE':
            managers_group.user_set.remove(user)
            return Response({"message": "User Removed"})
    
    return Response({"message": "error"}) #, status=status.HTTP_400_BAD_REQUEST) 
##############################################################################################################