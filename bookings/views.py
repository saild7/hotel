from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, render
from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
from bookings.forms import GuestForm
from bookings.models import Guest
from user.models import UserProfile

MERCHANT_KEY='UkuUb!W%XMMZsDMo'
# Create your views here.
def index(request):
    return HttpResponse("hy")

@login_required(login_url='/login')
def guest_detail(request,id):
    current_user = request.user
    # profile = UserProfile.objects.get(user_id=current_user.id)
    if request.method == 'POST':  # if there is a post
        form = GuestForm(request.POST)
        if form.is_valid():
            data = Guest()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.address = form.cleaned_data['address']
            data.country=form.cleaned_data['country']
            data.check_in= form.cleaned_data['check_in']
            data.check_out= form.cleaned_data['check_out']

            # guest=Guest.objects.filter(user_id=current_user.id,room_id=id)
            guest=Guest.objects.filter(room_id=id)
            print(guest)
            if guest:
                for rs in guest:
                    print(rs.check_in)
                    print(rs.check_out)
                    print(data.check_in)
                    print(data.check_out)
                    if data.check_in<=rs.check_in and data.check_out>=rs.check_out:
                        print("error1")
                        messages.warning(request,"Room already booked on these days")
                        break
                        
                    elif data.check_in<=rs.check_in and data.check_out>=rs.check_in:
                        print("error2")

                        messages.warning(request,"Room already booked on these days")
                        break

                    elif data.check_in==rs.check_in and data.check_out==rs.check_out:
                        messages.warning(request,"Room already booked on these days")
                        break
                        
                    elif data.check_in>=rs.check_in and data.check_out>=rs.check_out and data.check_in>data.check_out:
                        print("error3")
                        messages.warning(request,"Room already booked on these days")
                        break
                        
                    elif data.check_in>rs.check_in and data.check_out<=rs.check_out:
                        print("error4")
                        messages.warning(request,"Room already booked on these days")
                        break

                    else: 
                        result=data.check_out-data.check_in
                        data.stay=result.days
                        data.user_id = current_user.id
                        data.room_id=id
                        if data.check_out<=data.check_in:
                            messages.warning(request,"Check out date should be greater than Check In")
                            break
                        else:
                            data.save()
                            oid=data.id
                            param_dict = {
                            'MID':'NdpDYp66468182668374',
                            'ORDER_ID':str(data.id),
                            'TXN_AMOUNT':str(data.totalamount),
                            'CUST_ID':current_user.email,
                            'INDUSTRY_TYPE_ID':'Retail',
                            'WEBSITE':'worldpressplg',
                            'CHANNEL_ID':'WEB',
                            'CALLBACK_URL':'http://localhost:8000/bookings/handlerequest/',
                            }
                            param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict,MERCHANT_KEY)
                            return render(request,'paytm.html',{'param_dict':param_dict})
                            messages.success(request, "Room has been booked. Thank you ")
            else:
                result=data.check_out-data.check_in
                data.stay=result.days
                data.user_id = current_user.id
                data.room_id=id
                if data.check_out<=data.check_in:
                    messages.warning(request,"Check out date should be greater than Check In")
                else:
                    data.save()
                    oid=data.id
                    param_dict = {
                    'MID':'NdpDYp66468182668374',
                    'ORDER_ID':str(oid),
                    'TXN_AMOUNT':str(data.totalamount),
                    'CUST_ID':current_user.email,
                    'INDUSTRY_TYPE_ID':'Retail',
                    'WEBSITE':'worldpressplg',
                    'CHANNEL_ID':'WEB',
                    'CALLBACK_URL':'http://localhost:8000/bookings/handlerequest/',
                    }
                    param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict,MERCHANT_KEY)
                    return render(request,'paytm.html',{'param_dict':param_dict})
                    messages.success(request, "Room has been booked. Thank you ")

        else:
            # return redirect("/")
            messages.warning(request, form.errors)

    form=GuestForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context={'form':form,'profile':profile}
    return render(request, 'guest_form.html',context)
 

@csrf_exempt
def handlerequest(request):
    form=request.POST
    response_dict={}
    for i in form.keys():
        response_dict[i]=form[i]
        if i == 'CHECKSUMHASH':
            checksum=form[i]
    verify=Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            print('booking successfull')
        else:
            print('booking failed because' + response_dict['RESPMSG'])
    return render(request,'order_completed.html',{'response':response_dict})
