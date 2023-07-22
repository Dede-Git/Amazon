"""View module for handling requests about order products"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from amazonapi.models import OrderProduct


class OrderProductView(ViewSet):
    """Amazon order products view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single order product
        Returns:
            Response -- JSON serialized order product
        """

        try:
            order_product = OrderProduct.objects.get(pk=pk)
            serializer = OrderProductSerializer(order_product)
            return Response(serializer.data)
        except OrderProduct.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all order products
        Returns:
            Response -- JSON serialized list of order products
        """

        order_products = OrderProduct.objects.all()
        serializer = OrderProductSerializer(order_products, many=True)
        return Response(serializer.data)


class OrderProductSerializer(serializers.ModelSerializer):
    """JSON serializer for order products
    """
    class Meta:
        model = OrderProduct
        fields = ('id', 'order', 'product')
