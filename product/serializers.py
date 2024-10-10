from rest_framework import serializers
from .models import Product, Payment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity']

    def update(self, instance, validated_data):
        quantity = validated_data.get('quantity', instance.quantity)
        if quantity < 0:
            raise serializers.ValidationError("Количество не может быть отрицательным!")
        instance.quantity = quantity
        instance.save()
        return instance

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'vendor', 'amount']

    def update(self, instance, validated_data):
        amount = validated_data.get('amount', instance.amount)
        if amount < 0:
            raise serializers.ValidationError("Сумма не может быть отрицательной!")
        instance.amount = amount
        instance.save()
        return instance