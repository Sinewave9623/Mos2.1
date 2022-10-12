from lib2to3.pgen2.grammar import opmap_raw
from django.shortcuts import render
from .models import TranSum
from .serializers import TranSumSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q,Sum,Avg,Count,F
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404

# Create your views here.

class MosCreatList(generics.ListCreateAPIView):
    queryset=TranSum.objects.all()
    serializer_class=TranSumSerializer
    # start_fy=queryset[0]['fy'].split("-")[0]+"-04-01"
    # print('Split start  Fy ------->',start_fy)
    # end_fy=queryset[0]['fy'].split("-")[1]+"-03-31"
    # print('Split end  Fy ------->',end_fy)


    serializer_class=TranSumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group','code','againstType','part']

    def get_queryset(self):
        option = self.request.query_params.get('option')
        dfy = self.request.query_params.get('dfy')
        # print("option-->",option)
        try:
            start_fy=dfy[:4]+"-04-01"
            end_fy=dfy[5:]+"-03-31"
        except:
            raise Http404
        # print('start fy---->',start_fy)
        # print('end fy---->',end_fy)
        
        if option == 'O':
            opening=self.queryset.filter(trDate__lt=start_fy)                                           
            # print("Opening Data ----->",opening)
            return opening
        elif option=='A':
            addition=self.queryset.filter(trDate__range=(start_fy,end_fy))
            # print("Addition Data ----->",addition)
            return addition 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data) 
        return Response({'status':True,'Message': 'You have successfully Created','data':serializer.data}, status=status.HTTP_201_CREATED,headers=headers)



class MosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=TranSum.objects.all()
    serializer_class=TranSumSerializer
   
    def update(self, request, *args, **kwargs):
       partial = kwargs.pop('partial', False)
       instance = self.get_object()
       serializer = self.get_serializer(instance, data=request.data, partial=partial)
       serializer.is_valid(raise_exception=True)
       self.perform_update(serializer)
       result = {
        "status": True,
        "message": "Data successfully updated",
        "data": serializer.data,
       }
       return Response(result)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'status':True,'Message': 'You have successfully Deleted'})


# class MostListsc2(generics.ListAPIView):
#     queryset=TranSum.objects.values('part').annotate(total_qty=Sum('qty'),
#                                                              nbr=Count('trId'))
#     serializer_class=TranSumSerializersc2
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['group','code','againstType','fy','sp']
#     def list(self, request):
#         queryset = self.get_queryset()

#         return Response({'data':queryset},status=status.HTTP_200_OK)
    
