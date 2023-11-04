
from django.shortcuts import render
from .models import PersonalityTypes
from django.shortcuts import render
from .forms import PersonalityQtnForm

# Create your views here.


def home(request):
    return render(request,'HomePage.html')


def personalityType(request):
   
    allTypes=PersonalityTypes.objects.all()
    return render(request,'PersonalityTypes.html',{'alltypes':allTypes})





def AllProfiles(request):
    return render(request,'all-profiles.html')

def aboutpage(request):
    return render(request,'about.html')






def personalityTest(request):
    questions = [
         ("Do you feel more energized after spending time alone (I) or with others (E)? ", 'I', 'E'),
    ("Would you rather attend a small gathering with close friends (I) or a large party with many people (E)? ", 'I', 'E'),
    ("Do you prefer one-on-one conversations (I) or group discussions (E)? ", 'I', 'E'),
    ("Do you enjoy meeting new people and making new friends (E), or do you prefer deeper connections with a few close friends (I)? ", 'I', 'E'),
    ("Are you more reserved and quiet (I) or outgoing and talkative (E)? ", 'I', 'E'),
    ("Do you focus on the present moment and concrete details (S) or future possibilities and abstract concepts (N)? ", 'S', 'N'),
    ("Are you more practical and realistic (S) or imaginative and creative (N)? ", 'S', 'N'),
    ("Do you prefer step-by-step instructions and guidelines (S) or the freedom to explore new ways of doing things (N)? ", 'S', 'N'),
    ("Are you more likely to trust your gut instincts (N) or rely on facts and evidence (S)? ", 'S', 'N'),
    ("Do you find it easy to remember specific details and facts (S) or tend to forget them but remember the big picture (N)? ", 'S', 'N'),
    ("When making decisions, do you prioritize logic and rationality (T) or consider the impact on people's feelings and emotions (F)? ", 'T', 'F'),
    ("Are you more objective and analytical (T) or empathetic and compassionate (F)? ", 'T', 'F'),
    ("Do you value honesty and straightforwardness (T) or diplomacy and harmony (F)? ", 'T', 'F'),
    ("Are you more likely to critique and criticize (T) or encourage and support (F)? ", 'T', 'F'),
    ("Is it easier for you to remain emotionally detached (T) or emotionally invested (F)? ", 'T', 'F'),
    ("Do you prefer having a structured and organized life (J) or enjoy flexibility and adaptability (P)? ", 'J', 'P'),
    ("Are you more comfortable with planned schedules and deadlines (J) or go with the flow and adapt as things come (P)? ", 'J', 'P'),
    ("Do you like making decisions and sticking to them (J) or keeping your options open and being spontaneous (P)? ", 'J', 'P'),
    ("Are you inclined to complete tasks before relaxing (J) or leave things open-ended and enjoy the process (P)? ", 'J', 'P'),
    ("Do you tend to be more methodical and systematic (J) or improvisational and opportunistic (P)? ", 'J', 'P'),
    ]
    
    if request.method == 'POST':
        form = PersonalityQtnForm(questions, request.POST)
        if form.is_valid():
            # Process the form data here
            # You can access the user's answers using form.cleaned_data
            # Do something with the collected answers
            answers = [form.cleaned_data[f"question_{i}"] for i in range(len(questions))]
            # Further processing or saving the answers
            # Redirect or render a response
            print(answers)
            

    else:
        form = PersonalityQtnForm(questions)

    return render(request, 'adminPage.html', {'form': form, 'questions': questions})

