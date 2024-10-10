from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Payment
from .serializers import ProductSerializer, PaymentSerializer


class ProductViewSet(viewsets.ViewSet):
    def get(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
class ProductListView(viewsets.ViewSet):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PaymentViewSet(viewsets.ViewSet):
    def get(self, request, pk=None):
        try:
            payment = Payment.objects.get(pk=pk)
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def authorize_payment(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            if product.quantity <= 0:
                return Response({"error": "Quantity is zero. Cannot process payment."}, status=status.HTTP_400_BAD_REQUEST)

            # Сохранение информации о платеже (можно расширить логику по необходимости)
            serializer = PaymentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                # Уменьшаем количество продукта
                product.quantity -= 1
                product.save()

                return Response({"title": "Платёж успешно сохранён", "message": f"Оставшееся количество товара: {product.quantity}"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
class PaymentListView(viewsets.ViewSet):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)