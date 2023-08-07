from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserForm
from service.models import Service
from news.models import News
from django.core.paginator import Paginator


def index(request):
    newsdata=News.objects.all()
    serdata=Service.objects.all().order_by('-service_title')
    pagin = Paginator(serdata,2)
    page_number = request.GET.get('page')
    ServiceDataFinal = pagin.get_page(page_number)
    if request.method=='GET':
        st=request.GET.get('searchser')
        # print(st)
        if st!=None:
            serdata=Service.objects.filter(service_icon__icontains=st)

        # __icontains -- used for only one lettersearch

    # for a in serdata:
    #     print(a)                   # just for print data in terminal
    #     print(a.service_icon)
    #     print(a.service_title)
    #     print(a.service_des)
    data={
        # 'serdata':serdata,     # before paginator 
        'serdata':ServiceDataFinal,   # for paginator
        'newsdata':newsdata,
        
    }
    return render(request,'index.html',data)

def newsdetail(request,slug):
    # print(id)
    newsdetail=News.objects.get(news_slug=slug)
    data={
        'newsdetails':newsdetail,
    }
    return render(request,'newsdetail.html',data)

def Coh(request):
    data = {
        'title':'ExcelPTP.in',
        'h1':'Welcome to Excel PTP.',
        'clist':['python','Web desing','Web devlopment','react.js','node.js'],
        'student':[
            {'name':'Dhaval','id':'999'},
            {'name':'Baba Yaga','id':'555'}
        ],
        'numbers':[10,20,30,40,50,60],
        # 'numbers':[]

    }
    return render(request,'Coh.html',data)

def about(request):
    return render(request,'about.html')

def contactus(request):
    if request.method=='GET':
        output=request.GET.get('sum')
    return render(request,'contactus.html',{'output':output})

def droptech(request):
    return render(request,'droptech.html')

def submitform(request):
    try:
        
        if request.method=='POST':
#             # n1 = request.GET['num-1']
            n1 = int(request.POST.get('num_1'))      # we use num-1 for html.for form,py we use num_1.
            n2 = int(request.POST.get('num_2'))
            
            sum = n1 + n2
#         #    print(n1)
#         #   print(n2)
            data = {
                'n1':n1,
                'n2':n2,
                'sum':sum
            }
            return HttpResponse(f'Your sum is: {sum}')                #2
            # url="/contactus/?sum={}".format(sum)  #1
            # return redirect(url)                  #1
            # return HttpResponseRedirect(url)    #1
        

#            # return HttpResponseRedirect('/')
#             # return HttpResponseRedirect('/contactus/')

    except:
        pass
    # return HttpResponse(request)                 #3 first not needed

def userform(request):
    fn=UserForm()
    # sum = ''
    data = {'form':fn }      # render form in indexHTML
    try:
        if request.method=='POST':
            # n1 = request.GET['num-1']
            n1 = int(request.POST.get('num_1'))   # we use num-1 for html.
            n2 = int(request.POST.get('num_2'))
            
            sum = n1 + n2
        #    print(n1)
        #   print(n2)
            data = {
                'n1':n1,
                'n2':n2,
                'sum':sum,
                'form':fn
            }
            url="/contactus/?sum={}".format(sum)
            return HttpResponseRedirect(url)
            # return redirect(url)
            # return HttpResponseRedirect('/')
            # return HttpResponseRedirect('/contactus/')

    except:
        pass
    return render(request,'userform.html',data)
    # return render(request,'userform.html',{'sum':sum})
    
def calculator(request):
    c=' '
    try:
        if request.method=='POST':
            n1 = eval(request.POST.get('num-1'))        # evel data type used for both int and float
            n2 = eval(request.POST.get('num-2'))
            opr = request.POST.get('opr')
            if (opr=='+'):
                c=n1+n2
            elif opr=='-':
                c=n1-n2
            elif opr=='x':
                c=n1*n2
            elif opr=='%':
                c=n1/n2
            # ans=c
            # else:
            #     print('Choose opretion')

    except:
        pass
    # print(f' number 1 is :{n1}')         # it is for terminal
    # print(f' number 2 is :{n2}')
    # print(f'Your answer for {opr} is: {c}')
    
    return render(request,'calculator.html',{'c':c})

def odd(request):
    c=''
    data={}
    if request.method=='POST':
        if request.POST.get('num')=="":
            return render(request,"Odd_Even.html",{'error':True})
        

        n1=eval(request.POST.get('num'))
        if (n1%2==0):
            c='Even'
        else:
            c='Odd'
        data = {
                'n1':n1,
                'c':c,
            }
        # return HttpResponse(f'Your number {n1} is: {c}')
    return render(request,"Odd_Even.html",data)
def marksheet(request):
    param={}
    if request.method=='POST':
        s1=eval(request.POST.get('m1'))
        s2=eval(request.POST.get('m2'))
        s3=eval(request.POST.get('m3'))
        s4=eval(request.POST.get('m4'))
        s5=eval(request.POST.get('m5'))
        total=s1+s2+s3+s4+s5
        percentage=total/5
        param = {
            'total':total,
            'per':percentage
        }
        return render(request,'marksheet.html',param)
    return render(request,'marksheet.html')
def course(request):
    

    return HttpResponse('<h1>Welcome to courses</h1>')

def courseDatalist(request):
    return HttpResponse('<h1>Welcome to coursesDatalist</h1>')