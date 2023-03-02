from rest_framework import serializers

from users.models import User, Payment, Subscription


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'phone',
            'city',
            'first_name',
            'last_name'
        )


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            'datetime',
            'lesson',
            'course',
            'amount',
            'pay_type'
        )


class UserProfileInfoSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = (
            'email',
            'phone',
            'city',
            'first_name',
            'last_name',
            'payments'
        )


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = (
            'course',
        )
