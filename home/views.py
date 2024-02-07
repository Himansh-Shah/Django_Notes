from django.shortcuts import render, redirect
from home.models import Difficulty, Topic, Question
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home_page(request, id):
    if(request.method=='POST'):
        title = request.POST.get('title')
        difficulty = request.POST.get('difficulty')
        topic = request.POST.getlist('topic')
        notes = request.POST.get('notes')
        code = request.POST.get('code')
        
        dif = Difficulty.objects.filter(difficulty = difficulty)[0]
        
        question = Question.objects.create(
            user = id,
            title=title,
            difficulty = dif,
            note = notes,
            code = code

        )
        for items in topic:
            question.topics.add(Topic.objects.filter(name=items)[0])
            question.save()
        return redirect(f'/home/{id}')
    queryset1 = Difficulty.objects.all()
    queryset2 = Topic.objects.all()
    queryset3 = Question.objects.filter(user = id)
    return render(request , 'home/home.html', context={'Difficulty':queryset1, 'Topics':queryset2, 'Questions':queryset3})

def question_detail(request, id):
    queryset = Question.objects.filter(id = id)[0]
    return render(request, 'home/details.html', context= {'queryset':queryset})