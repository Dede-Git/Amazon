from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from amazonapi.models import Order, User


class OrderView(ViewSet):
    """Order View"""

    def retrieve(self, request, pk):
        """get single"""
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
                            status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """get all"""
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        """create"""

        customer_id = User.objects.get(pk=request.data["customer_id"])

        order = Order.objects.create(
            date=request.data["date"],
            closed=request.data["closed"],
            customer_id=customer_id
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def update(self, request, pk):
        """update"""
        order = Order.objects.get(pk=pk)
        order.date = request.data["date"]
        order.closed = request.data["closed"]

        customer_id = User.objects.get(pk=request.data["customer_id"])
        order.customer_id = customer_id
        order.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """delete"""
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OrderSerializer(serializers.ModelSerializer):
    """order serializer"""
    class Meta:
        model = Order
        fields = ('id', 'customer_id', 'date', 'closed')

        depth = 1
