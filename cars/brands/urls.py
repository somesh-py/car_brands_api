from django.urls import path
from . import views

urlpatterns = [
    # path('cardetails/<int:pk>/',views.car_details),
    # path('cardetails/',views.car_detailsall),
    path('cardetailsadd/',views.postjsondata),
]
