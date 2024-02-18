# openai_script.py
import openai

def generate_response(user_input):
    openai.api_key = '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'

    prompt = f"Map the user input to the appropriate description by its number. if there are more then on that qualify, seperate then separate with commas: {user_input}"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will map the user input to numbers. If the input is more than one, then return multiple columns separated by commas. You can be general when choosing where to map. Return the list of applicable numbers separated by commas, do not return the name. The options are: 1:Ice Skating, 2:Curling, 3:Weightlifting, 4:Indoor Swimming, 5:Wave Pool, 6:Hot Tub, 7:Climbing Wall, 8:Indoor Track, 9:Outdoor Wading Pool, 10:Indoor Sports, 11:Indoor Racquetball, 12:Steam Room, 13:Diamond Facility, 14:Diving Tank, 15:Springboard Diving, 16:Outdoor Field, 17:Teaching Pool, 18:Spray Park, 19:Outdoor Swimming, 20:Other Pool, 21:Platform Diving, 22:Indoor Wading Pool, 23:Golf, 24:Golf Course, 25:Driving Range, 26:Nordic Skiing, 27:Outdoor Track, 28:Rope Swing, 29:Gymnastics"
            },
            {
                "role": "user",
                "content": {user_input},
            },
        ]
    )
    
    return completion.choices[0].message.content