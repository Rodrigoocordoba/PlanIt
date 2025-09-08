from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MeView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        if request.user.is_authenticated:
            u = request.user
            return Response({"id": u.id, "username": u.username, "email": u.email})
        return Response({"anonymous": True})
