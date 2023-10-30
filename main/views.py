
from django.shortcuts import render
from .models import PersonalityTypes
from django.shortcuts import render
from .forms import YesNoForm

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
        "Is the sky blue?",
        "Do you like ice cream?",
        "Have you ever been to Paris?",
        # Add more questions as needed
    ]

    if request.method == 'POST':
        form = YesNoForm(questions, request.POST)
        if form.is_valid():
            # Process the form data here
            # You can access the user's answers using form.cleaned_data
            # Do something with the collected answers
            answers = [form.cleaned_data[f"question_{i}"] for i in range(len(questions))]
            # Further processing or saving the answers
            # Redirect or render a response
    else:
        form = YesNoForm(questions)

    return render(request, 'adminPage.html', {'form': form, 'questions': questions})

