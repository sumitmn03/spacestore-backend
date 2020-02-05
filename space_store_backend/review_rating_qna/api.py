from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import ReviewSerializer, Q_N_ASerializer
from .models import Review, Q_N_A


class ReviewViewSet(generics.GenericAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        user = request.user
        if Review.objects.filter(user=user, product=request.data["product"]).exists():
            return Response({
                "already_exists": "already_exists",
            })
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            review = serializer.save(user=request.user)
            return Response({
                "review": ReviewSerializer(review, context=self.get_serializer_context()).data,
            })


class QnaViewSet(generics.GenericAPIView):
    serializer_class = Q_N_ASerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # q_n_a = serializer.save(user=request.user)
        # return Response({
        #     "question": Q_N_ASerializer(q_n_a, context=self.get_serializer_context()).data,
        # })
        user = request.user
        if Q_N_A.objects.filter(user=user, product=request.data["product"]).count() > 4:
            return Response({
                "limit_crossed": "limit_crossed",
            })
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            q_n_a = serializer.save(user=request.user)
            return Response({
                "question": Q_N_ASerializer(q_n_a, context=self.get_serializer_context()).data,
            })
