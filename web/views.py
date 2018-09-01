from django.shortcuts import render

from web.models import Token, User, Expense, Income
from datetime import datetime

from json import JSONEncoder
from django.http import JsonResponse
#برای آن که دچار حملات
#DDOS
#نشویم، برنامه اجبار میکند که حتما درخواست از سوی فرم انجام شود
# این دو خط برای این است که بی‌خیال این مسیله شود و اجاز دهد که از طریق غیرفرم هم درخواست انجام شود
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt


# Create your views here.

def submit_expense(request):
    """submits an expense"""
    now = datetime.now()
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    Expense.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=now)

    return JsonResponse(
    {
        'status':'ok',
    },
    encoder=JSONEncoder
    )

@csrf_exempt
def submit_income(request):
    """submits an income"""
    now = datetime.now()
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    Income.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=now)

    return JsonResponse(
    {
        'status':'ok',
    },
    encoder=JSONEncoder
    )
