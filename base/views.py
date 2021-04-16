from django.shortcuts import render
from base.models import Polls
from django.http import HttpResponse
# Create your views here.

def index(request):
        


    all_polls = Polls.objects.all()
    context={'all_polls':all_polls}
    return render(request, 'index.html',context)

def vote(request,pk):
    poll = Polls.objects.get(pk=pk)
    if request.method == 'POST':
        vote=request.POST['poll']
        if vote=='option1':
            poll.o1_votes += 1
        elif vote=='option2':
            poll.o2_votes += 1
        elif vote=='option3':
            poll.o3_votes += 1
        elif vote == 'option4':
            poll.o4_votes += 1
        else:
            return HttpResponse("sorry")
        poll.save()
        
    return render(request,'vote.html',{'poll':poll})

def detail_poll(request,id):
    detail_obj = Polls.objects.filter(pk=id)
    print(detail_obj)
    return render(request, 'detail_poll.html')