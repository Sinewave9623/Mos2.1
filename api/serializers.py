from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import TranSum
from django.db.models import Sum,Count,Max,Min,Q


class TranSumSerializer(serializers.ModelSerializer):
    # total_qty=serializers.IntegerField()
    # nbr=serializers.IntegerField()
    
    # closing = serializers.SerializerMethodField()
    # investment_value = serializers.SerializerMethodField()
    class Meta:
        model=TranSum
        fields=('trId','group','code','fy','againstType','sp','part','fmr','isinCode','trDate','qty','rate','sVal','sttCharges','otherCharges','noteAdd')

    # def get_closing(self, obj): 
    #     totalclosing = TranSum.objects.all().aggregate(closing=Sum('qty'))
    #     return totalclosing["closing"]

    # def get_investment_value(self, obj):
    #     totalopening = TranSum.objects.filter(trId=1).aggregate(investment_value=Sum('sVal'))
    #     return totalopening["investment_value"]




# class TranSumSerializersc2(serializers.ModelSerializer):
#     total_qty=serializers.IntegerField()
#     nbr=serializers.IntegerField()
#     class Meta:
#         model=TranSum
#         fields = ['total_qty','nbr']

    
