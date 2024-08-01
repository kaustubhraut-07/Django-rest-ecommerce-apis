from django.urls import path
from .views import PaymentView
# from .views import CreatePayment

urlpatterns = [
    # path('create/', CreatePayment.as_view() , name='createpayment'),
    path('cashfree/', PaymentView.as_view(), name='cashfreepayment'),
]