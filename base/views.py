from django.shortcuts import render, redirect
from base.models import Polls
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

def index(request):
    all_polls = Polls.objects.all()
    context={'all_polls':all_polls}
    return render(request, 'index.html',context)

def vote(request,pk):
    poll = Polls.objects.get(pk=pk)
    if request.method == 'POST':
        vote=request.POST.get('poll')
        if vote=='option1':
            poll.o1_votes += 1
            poll.total_votes += 1
        elif vote=='option2':
            poll.o2_votes += 1
            poll.total_votes += 1
        elif vote=='option3':
            poll.o3_votes += 1
            poll.total_votes += 1
        elif vote == 'option4':
            poll.o4_votes += 1
            poll.total_votes += 1
        else:
            return HttpResponse("sorry")
        poll.save()
        messages.success(request,"Your Vote has been submitted")
        return redirect('home')
        
    return render(request,'vote.html',{'poll':poll})

def detail_poll(request,pk):
    poll = Polls.objects.get(id=pk)
    context={'poll':poll}
    return render(request, 'detail_poll.html',context)


class PollAdd(CreateView):
    model = Polls
    template_name = 'poll_add.html'
    fields = ('question','o1','o2','o3','o4')
    success_url = reverse_lazy('home')