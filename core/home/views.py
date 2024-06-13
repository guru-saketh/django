from django.shortcuts import render

# Create your views here.
def home(request):
    people = [
        {'name': 'saketh', 'age': 24},
        {'name': 'varun', 'age': 25},
        {'name': 'dinesh', 'age': 26},
        {'name': 'raghu', 'age': 24},
    ]
    
    # For debugging purposes; remove or comment out in production
    for person in people:
        print(person)

    return render(request, "index.html", context={'people': people})
