from django.urls import path
from . import views

urlpatterns = [
    path('transaction/',views.SavePurch.as_view()),
    path('transaction1/',views.RetTransSum.as_view()),
    path('transaction/<int:pk>',views.MosRetrieveUpdate.as_view()),
    path('transaction2/',views.RetriveAPISc2.as_view()),
    # path('transaction3/',views.RetInvSc1.as_view()),
    path('transaction3/',views.RetInvSc1.as_view()),
]