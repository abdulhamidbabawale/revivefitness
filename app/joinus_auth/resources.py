from ..site_data.models import User,Classes,Plans
import requests
from django.http import JsonResponse
from django.conf import settings
class Resource:
      def plan_duration_cost(self):
          #get plan cost for platinum and standard
           global standard_cost
           global platinum_cost
           standard_cost = Plans.objects.filter(plan_name='standard').values_list('plan_price', flat=True).first()
           platinum_cost = Plans.objects.filter(plan_name='platinum').values_list('plan_price', flat=True).first()

           #multiply plan cost based on duration and use '{:,}' to add ' , ' symbol to the price
           Resource.plan_duration_cost.platinum_monthly='{:,}'.format(platinum_cost)
           Resource.plan_duration_cost.platinum_quterly= '{:,}'.format(int(platinum_cost * 2.4))
           Resource.plan_duration_cost.platinum_yearly='{:,}'.format(int(platinum_cost * 7.4))
           Resource.plan_duration_cost.standard_monthly='{:,}'.format(standard_cost)
           Resource.plan_duration_cost.standard_quterly= '{:,}'.format(int(standard_cost * 2.4))
           Resource.plan_duration_cost.standard_yearly='{:,}'.format(int(standard_cost * 7.4))
      def cookies_data(self,request):
           Resource.cookies_data.selected_plan_id=request.COOKIES.get('selectedplan')
           Resource.cookies_data.selected_Class_id=request.COOKIES.get('selectedClass')
           Resource.cookies_data.plan_Duration_id=request.COOKIES.get('planDuration')
      def naira_to_kobo(amount):
           return int(amount * 100)
      def plan_price(self,request):
          #  Resource.cookies_data(self,request)
          #  price = None
           plan_id=request.COOKIES.get('selectedplan')
           duration=request.COOKIES.get('planDuration')
           if plan_id == '2':
                if duration == 'monthly':
                   price =platinum_cost
                if duration == 'quarterly':
                   price =platinum_cost * 2.4
                if duration == 'yearly':
                   price =platinum_cost * 7.4
                return int(price)
           elif plan_id == '1':
                if duration == 'monthly':
                   price =standard_cost
                if duration == 'quarterly':
                   price =standard_cost * 2.4
                if duration == 'yearly':
                   price =standard_cost * 7.4
                return int(price)
      def payment1(self,request,amount,email):
          url= "https://api.paystack.co/transaction/initialize"
          headers = {
              "Authorization":f"Bearer {settings.PAYSTACK_API_KEY}",
              "Content-Type": "application/json"
            }
          amount_in_kobo=Resource.naira_to_kobo(amount)
          data = {
              "email": email,
              "amount": amount_in_kobo
           }
          response = requests.post(url, json=data,headers=headers)
          pay=response
          def response_data():
               response_key=requests.get(url)
               if pay.status_code == 200:
                  data = pay.json()  # Parse JSON data from the response
                  # print(data)

                   # Access the nested status
                  transaction = data.get('data', {})
                  payment_page_url = transaction.get('authorization_url')
                  request.session['payment_page_url']=payment_page_url
                  reference = transaction.get('reference')
                  request.session['reference']=reference
                  # print (payment_page_url)
                  # print(reference)
                  return payment_page_url, reference
               return None
          m=response_data()


          return JsonResponse(response.json())
      def verify_payment1(self,request,reference):
          url="https://api.paystack.co/transaction/verify/{}".format(reference)
          headers = {
            "Authorization":f"Bearer {settings.PAYSTACK_API_KEY}",
            "Content-Type": "application/json"
              }

          response = requests.get(url, headers=headers)
          get_response_data=response
          verify_response=get_response_data.json()
          payload=verify_response.get('data',{})
          status=payload.get('status')
          gateway_response=payload.get('gateway_response')
          request.session['status']=status
          print(status)
          print(gateway_response)


          return JsonResponse(response.json())
