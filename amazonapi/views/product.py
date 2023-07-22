from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from amazonapi.models import Product, User


class ProductView(ViewSet):
    """Amazon product view"""

    def retrieve(self, request, pk):
        """Gets a product by its pk

        Returns:
            Response --  single JSON serialized product dictionary
        """
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def list(self, request):
        """Gets all products

        Returns:
            Response -- JSON serialized list of products
        """
        products = Product.objects.all()
        seller_products = request.query_params.get('seller_id', None)
        if seller_products is not None:
            products = products.filter(seller_id=seller_products)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handles POST operations

        Returns:
            Response -- JSON serialized product instance
        """
        seller = User.objects.get(pk=request.data["seller_id"])
        product = Product.objects.create(
            rare_user_id=seller,
            name=request.data["name"],
            description=request.data["description"],
            quantity=request.data["quantity"],
            price=request.data["price"],
            image=request.data["image"],
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handles PUT requests for a product

        Returns:
            Response -- Empty body with 204 status code
        """
        product = Product.objects.get(pk=pk)
        seller = User.objects.get(pk=request.data["seller_id"])
        product.seller_id = seller
        product.name = request.data["name"]
        product.description = request.data["description"]
        product.quantity = request.data["quantity"]
        product.price = request.data["price"]
        product.image = request.data["image"]
        product.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE requests for a product

        Returns:
            Response -- Empty body with 204 status code
        """
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'seller_id',
                  'name', 'description', 'image',
                  'price', 'quantity')
        depth = 1
