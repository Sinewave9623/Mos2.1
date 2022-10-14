from django.urls import path
from . import views

urlpatterns = [
    path('transaction/',views.MosSaveApi.as_view()),
    path('transaction1/',views.MosRetrive.as_view()),
    # path('transaction2/',views.MosRetrivesc2.as_view()),
    path('transaction2/',views.RetriveAPISc2.as_view()),
    path('transaction/<int:pk>',views.MosRetrieveUpdate.as_view()),
]