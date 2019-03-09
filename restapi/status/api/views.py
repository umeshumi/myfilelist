from status.models import Status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StatusSerializer
from rest_framework import generics, mixins


# class StatusListSearchAPIView(APIView):
# 	permission_classes 		= []
# 	authentication_classes 	= []

# 	def get(self, request, format=None):
# 		qs = Status.objects.all()
# 		serializer = StatusSerializer(qs, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		qs = Status.objects.all()
# 		serializer = StatusSerializer(qs, many=True)
# 		return Response(serializer.data)

class StatusAPIView(mixins.CreateModelMixin,
	mixins.DestroyModelMixin,
	mixins.UpdateModelMixin,
	generics.RetrieveAPIView,
 	generics.ListAPIView):
	permission_classes 		= []
	authentication_classes 	= []
	serializer_class 		= StatusSerializer

	def get_queryset(self):
		qs = Status.objects.all()
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(content__icontains=query)
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


# class StatusCreateAPIView(generics.CreateAPIView):
# 	permission_classes 		= []
# 	authentication_classes 	= []
# 	queryset 				=Status.objects.all()
# 	serializer_class 		= StatusSerializer

	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)


# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
# 	permission_classes 		= []
# 	authentication_classes 	= []
# 	queryset 				= Status.objects.all()
# 	serializer_class 		= StatusSerializer

# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
# 	permission_classes 		= []
# 	authentication_classes 	= []
# 	queryset 				= Status.objects.all()
# 	serializer_class 		= StatusSerializer

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def patch(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)


# class StatusUpdateAPIView(generics.UpdateAPIView):
# 	permission_classes 		= []
# 	authentication_classes 	= []
# 	queryset 				=Status.objects.all()
# 	serializer_class 		= StatusSerializer

# class StatusDeleteAPIView(generics.DestroyAPIView):
# 	permission_classes 		= []
# 	authentication_classes 	= []
# 	queryset 				=Status.objects.all()
# 	serializer_class 		= StatusSerializer