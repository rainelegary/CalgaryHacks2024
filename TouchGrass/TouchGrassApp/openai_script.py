# openai_script.py
import openai

def generate_response(user_input):
    openai.api_key = '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'

    prompt = f"Translate the following English text to French:\nUser Input: {user_input}"

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                        
                "role": "system",
                "content": "You will map the user to Springboard Diving: ",
            },
            {
                "role": "user",
                "content": "How are you feeling today",
            },
        ],
    )
    return completion.choices[0].message.content