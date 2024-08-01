# from django.shortcuts import render
# from django.http import JsonResponse
# import os
# from dotenv import load_dotenv
# load_dotenv()
# from django.views.decorators.csrf import csrf_exempt

# from cashfree_pg.models.create_order_request import CreateOrderRequest
# from cashfree_pg.api_client import Cashfree
# from cashfree_pg.models.customer_details import CustomerDetails

# # Create your views here.

# Cashfree.XClientId = os.getenv("APP_ID")
# Cashfree.XClientSecret = os.getenv("SECREAT_KEY")

# Cashfree.XEnvironment = Cashfree.SANDBOX
# x_api_version = "2023-08-01"

# @csrf_exempt
# def cashfreepayment(request):
#     customerDetails = CustomerDetails(customer_id="walterwNrcMi", customer_phone="9011686021")

#     # Assuming order_meta is part of CreateOrderRequest
#     # print(os.getenv("SECREAT_KEY"))
#     order_id = "abc_124_order_1"
#     orderMeta = {
#         "return_url": f"https://www.cashfree.com/devstudio/preview/pg/web/checkout?order_id={order_id}"
#     }
#     # print(orderMeta)
#     createOrderRequest = CreateOrderRequest(
#         order_id= order_id,
#         order_amount=1,
#         order_currency="INR",
#         customer_details=customerDetails,
#         order_meta=orderMeta
#     )
#     print(createOrderRequest)
#     try:
#         api_response = Cashfree().PGCreateOrder(x_api_version, createOrderRequest, None, None)
#         return JsonResponse({'status': 'success', 'data': api_response.data})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializer import PaymentSerializer
import requests
import os
class PaymentView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            payment = serializer.instance
            print(payment , "@@@@@@")
            
            token_url = 'https://sandbox.cashfree.com/pg/'
            headers = {
                'Content-Type': 'application/json',
                'x-api-id': os.getenv("APP_ID"),
                'x-api-secret': os.getenv("SECREAT_KEY")
            }
            token_data = {
                'order_id': payment.order_id,
                'amount': float(payment.amount),  
                'currency': payment.currency
            }
            token_response = requests.post(token_url, headers=headers, json=token_data)
            print(f'Token response: {token_response.status_code} - {token_response.text}')
            if token_response.status_code == 200:
                token = token_response.json()['token']
                payment.payment_token = token
                payment.save()
               
                payment_url = f'https://test.cashfree.com/api/v1/payments/{token}'
                return Response({'payment_url': payment_url}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Token generation failed"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            error_message = serializer.errors
            error_message['error'] = 'Invalid request data'
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)