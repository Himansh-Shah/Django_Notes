from django.shortcuts import render, redirect
from home.models import Difficulty, Topic, Question
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home_page(request):
    if(request.method=='POST'):
        title = request.POST.get('title')
        difficulty = request.POST.get('difficulty')
        topic = request.POST.getlist('topic')
        notes = request.POST.get('notes')
        code = request.POST.get('code')
        print(request.POST)
        
        print(topic)
        
        dif = Difficulty.objects.filter(difficulty = difficulty)[0]
        
        question = Question.objects.create(
            title=title,
            difficulty = dif,
            note = notes,
            code = code

        )
        for items in topic:
            question.topics.add(Topic.objects.filter(name=items)[0])
            question.save()
        return redirect('/home')
    queryset1 = Difficulty.objects.all()
    queryset2 = Topic.objects.all()
    queryset3 = Question.objects.all()
    return render(request , 'home/home.html', context={'Difficulty':queryset1, 'Topics':queryset2, 'Questions':queryset3})

