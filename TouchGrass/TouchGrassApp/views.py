from django.shortcuts import render, redirect
from .models import Facility, Activity
import openai

def homescreen(request):
    return render(request, 'TouchGrassApp/base.html')

def index(request):
    return render(request, 'TouchGrassApp/index.html')

def map_view(request):
    facilities = Facility.objects.all()  # Query all facilities from your database
    context = {
        'facilities': facilities
    }
    return render(request, 'TouchGrassApp/index.html', context)

def index(request):
   facilities = Facility.objects.all()
   print( {'facilities': facilities})
   return render(request, 'TouchGrassApp/index.html', {'facilities': facilities})

def index(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')  # Get user input from the form
        openai_response = generate_response(user_input)  # Get response from OpenAI
        print(openai_response)
        activities = openai_response.split(',')  # Split the response into activities

        # Initialize an empty list to store facility IDs
        facility_ids = []

        # Query facilities based on activities
        for activity_id in activities:
            try:
                # Query the Activity model to get the activity object by ID
                activity = Activity.objects.get(id=int(activity_id.strip()))
                # Retrieve the related facility IDs for the current activity
                facility_ids.extend(activity.facilities.values_list('id', flat=True))
            except (Activity.DoesNotExist, ValueError):
                # Handle the case where the activity does not exist or the ID is invalid
                pass

        # Filter facilities based on the collected facility IDs
        filtered_facilities = Facility.objects.filter(id__in=facility_ids).distinct()

        print(filtered_facilities)
        # Pass the filtered facilities to the template
        context = {'facilities': filtered_facilities}
        return render(request, 'TouchGrassApp/index.html', context)
    else:
        return render(request, 'TouchGrassApp/index.html')  # Render the index page if not a POST request


def generate_response(user_input):
    openai.api_key = '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'

    prompt = "1:Ice Skating, 2:Curling, 3:Weightlifting, 4:Indoor Swimming, 5:Wave Pool, 6:Hot Tub, 7:Climbing Wall, 8:Indoor Track, 9:Outdoor Wading Pool, 10:Indoor Sports, 11:Indoor Racquetball, 12:Steam Room, 13:Diamond Facility, 14:Diving Tank, 15:Springboard Diving, 16:Outdoor Field, 17:Teaching Pool, 18:Spray Park, 19:Outdoor Swimming, 20:Other Pool, 21:Platform Diving, 22:Indoor Wading Pool, 23:Golf, 24:Golf Course, 25:Driving Range, 26:Nordic Skiing, 27:Outdoor Track, 28:Rope Swing, 29:Gymnastics. \n According to this list, map the following to comma seperated integers, based on user input. The goal is to map them to the activity based on their input. It can be general."

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content":prompt
            },
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )
    response = completion.choices[0].message.content
    return response