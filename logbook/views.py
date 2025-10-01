# Import necessary functions and classes from Django and the current app.
from django.shortcuts import render, redirect
from .models import Quest, Servant, Construct
from .forms import QuestForm, ServantForm

# This view handles the request for the home page.
# It doesn't need any data from the models, it just shows the base template.
def home(request):
    context = {}
    return render(request, "logbook/base.html", context)

# --- Quest Views ---

# This view handles the page that lists all the Quests.
def quest_list(request):
    # 1. Get all Quest objects from the database.
    quests = Quest.objects.all()
    # 2. Create a context dictionary to pass the quest list to the template.
    context = {"quests": quests}
    # 3. Render the 'quest_list.html' template, passing it the context.
    return render(request, "logbook/quest_list.html", context)

# This view handles displaying the details for a single, specific quest.
def quest_detail(request, pk):
    # 1. Get the single Quest object from the database whose primary key (pk) matches the one from the URL.
    chosen_quest = Quest.objects.get(pk=pk)
    # 2. Create a context dictionary to pass this single quest to the template.
    context = {"chosen_quest": chosen_quest}
    # 3. Render the 'quest_detail.html' template, passing it the context.
    return render(request, "logbook/quest_detail.html", context)

# This view handles both displaying the form to create a new quest and processing the submitted form data.
def create_quest(request):
    # Check if the request method is POST, which means the user has submitted the form.
    if request.method == "POST":
        # 1. Create a form instance and populate it with data from the request.
        form = QuestForm(request.POST)
        # 2. Check if the form's data is valid according to the model's rules.
        if form.is_valid():
            # 3. Save the new Quest object to the database.
            form.save()
            # 4. Redirect the user to the quest list page to see the new quest.
            return redirect("quest-list")
    # If the request method is GET, which means the user is just visiting the page.
    else:
        # Create a blank, unbound instance of the form to display.
        form = QuestForm()

    # Package the form into the context dictionary.
    context = {"form": form}
    # Render the template, passing it the form.
    return render(request, "logbook/create_quest.html", context)

# --- Servant Views ---

# This view handles the page that lists all the Servants.
def servant_list(request):
    servants = Servant.objects.all()
    context = {"servants": servants}
    return render(request, "logbook/servant_list.html", context)

# --- Construct Views ---

# This view handles the page that lists all the Constructs.
def construct_list(request):
    constructs = Construct.objects.all()
    context = {"constructs": constructs}
    return render(request, "logbook/construct_list.html", context)

#this view handles displaying the servant and proccessing the submited data:
def summon_servant(request):
    #check if the user submited any data:
    if request.method == "POST":
        #create a form instance and populate it with the user data:
        form = ServantForm(request.POST)
            #check if the form is valid and save it
        if form.is_valid():
            form.save()
            #redrict the user to the servant page to see the change:
            return redirect("servant-list")
        #if the request is a GET(user just entered page) show the form:
    else:
        form = ServantForm()
        context = {"form":form}
        #render the template passing it the form:
        return render(request,"logbook/summon_servant.html",context)