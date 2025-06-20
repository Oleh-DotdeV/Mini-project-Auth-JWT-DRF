from .permissions import *
from rest_framework import generics
from .serializers import *
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *

User = get_user_model()


class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer


class NotesAPIList(generics.ListCreateAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = (IsAuthenticatedOrReadOnly,)

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)


class NotesAPIUpdate(generics.RetrieveUpdateAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = (IsOwnerOrReadOnly,)

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)


class NotesAPIDestroy(generics.RetrieveDestroyAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = (IsAdminOrReadOnly,)

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
