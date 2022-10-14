from .models import TranSum
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q,Sum
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from rest_framework.views import APIView
from .serializers import TranSumSaveSerializer,TranSumRetrivSerializer,TranSumRetrivesc2Serializer

# -------------------- Saving API
class MosSaveApi(APIView):
    def post(self, request, format=None):
        serializer = TranSumSaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------- Retriveing API
class MosRetrive(generics.ListAPIView):
    queryset=TranSum.objects.all()
    serializer_class=TranSumRetrivSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group','code','againstType','part']

    # -------------------- Overriding Queryset
    def get_queryset(self):
        option = self.request.query_params.get('option')
        dfy = self.request.query_params.get('dfy')
        try:
            start_fy=dfy[:4]+"-04-01"
            end_fy=dfy[5:]+"-03-31"
        except:
            raise Http404

        if option == 'O':
            opening=self.queryset.filter(trDate__lt=start_fy)
            return opening
        elif option=='A':
            addition=self.queryset.filter(trDate__range=(start_fy,end_fy))
            return addition 
    # -------------------- Overriding Create Method 
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data) 
        return Response({'status':True,'Message': 'You have successfully Created','data':serializer.data}, status=status.HTTP_201_CREATED,headers=headers)


#   ------------------------- Update and Retrive API
class MosRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset=TranSum.objects.all()
    serializer_class=TranSumRetrivSerializer
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
    # ---------------  Overriding Destroy Method
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'status':True,'Message': 'You have successfully Deleted'})
 
 # Retrive API Screen No Two
class RetriveAPISc2(APIView):
    def get(self, request, format=None):
        # ------------ fetching parameter in  Url
        group = self.request.query_params.get('group')
        code = self.request.query_params.get('code')
        againstType = self.request.query_params.get('againstType')
        part = self.request.query_params.get('part')
        dfy = self.request.query_params.get('dfy')
        try:
            start_fy=dfy[:4]+"-04-01"
            end_fy=dfy[5:]+"-03-31"
        except:
            raise Http404
        #--------------------- Opening
        opening = TranSum.objects.filter(trDate__lt=start_fy,group=group,code=code,againstType=againstType,part=part).values_list('qty')
        open=list(opening)
        varop=0
        for i in open:
            w=int(i[0])
            varop=varop+w 
        print(varop)  
        #--------------------- Additions
        addition = TranSum.objects.filter(trDate__range=(start_fy,end_fy),group=group,code=code,againstType=againstType,part=part).values_list('qty')
        print("Daaaa",addition)
        b=list(addition)
        varadd=0
        for i in b:
            w=int(i[0])
            varadd=varadd+w   
       
        # ------------------------- Closing
        closing=varadd+varop
        serializer = TranSumRetrivesc2Serializer(addition, many=True)
        return Response({'status':True,'msg':'done','opening':varop,'addition':varadd,'closing':closing})