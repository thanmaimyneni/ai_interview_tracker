# backend/services/openai_chat.py

import openai
from config.settings import settings

openai.api_key = settings.OPENAI_API_KEY

def ask_hr_bot(resume_text: str, user_input: str) -> str:
    messages = [
        {"role": "system", "content": "You are an HR interviewer evaluating candidates based on their resume."},
        {"role": "user", "content": f"This is the candidate's resume:\n{resume_text}"},
        {"role": "assistant", "content": "Great, let's begin the interview."},
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=250
    )

    return response.choices[0].message.content.strip()
