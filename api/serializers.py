from dataclasses import field, fields
from rest_framework import serializers
from .models import TranSum
 

 # ---------------------- Saving API
class SavePurchSerializer(serializers.ModelSerializer):
    class Meta:
        model=TranSum
        fields=('trId','group','code','fy','againstType','sp','part','fmr','isinCode','trDate','qty','rate','sVal','sttCharges','otherCharges','noteAdd')
# ------------------------ Retriveing API
class RetTransSumSerializer(serializers.ModelSerializer):
    class Meta:
        model=TranSum
        fields=['trId','trDate','qty','rate','sVal','sttCharges','otherCharges','noteAdd']

# ------------------------ Retrivng API Screen No2 (opening, addition, closing)
class TranSumRetrivesc2Serializer(serializers.ModelSerializer):
    class Meta:
        model=TranSum
        fields=['trId','fmr','isinCode']

# # ------------------------ Retrivng API Screen No2
# class TranssumRetInvSc1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=TranSum
#         fields=['fmr','isinCode','marketValue']

class RetInvSc1serializer(serializers.ModelSerializer):
    class Meta:
        model=TranSum
        fields=['sp','part','fmr','isinCode','marketValue']
    