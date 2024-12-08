from ..site_data.models import User,Classes,Plans
import requests
from django.http import JsonResponse
from django.conf import settings
class Resource:
      def plan_duration_cost(self):
          #get plan cost for platinum and standard
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
      def payment1(request,amount,email):
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
                  print(data)

                   # Access the nested status
                  transaction = data.get('data', {})
                  payment_page_url = transaction.get('authorization_url')
                  reference = transaction.get('reference')
                  print (payment_page_url)
                  print(reference)
                  return payment_page_url, reference
               return None
          m=response_data()

          return JsonResponse(response.json())
