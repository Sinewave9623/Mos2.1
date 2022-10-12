from django.urls import path
from . import views

urlpatterns = [
    path('transaction/',views.MosCreatList.as_view()),
    path('transaction/<int:pk>',views.MosRetrieveUpdateDestroy.as_view()),
    # path('transactionsc2/',views.MostListsc2.as_view())
]