import json
import os

def get_bot_response(user_message):
    message = user_message.lower().strip()

    # Load JSON data
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    faq_path = os.path.join(base_dir, 'data', 'faq.json')
    subjects_path = os.path.join(base_dir, 'data', 'subjects.json')

    if "hello" in message or "hi" in message:
        return "Hello! How can I assist you with your academic query today?"

    if "subject" in message or "course" in message:
        try:
            with open(subjects_path, 'r') as f:
                subjects = json.load(f)
            resp = "Available Subjects:\n"
            for s in subjects:
                resp += f"- {s['code']}: {s['name']} ({s['credits']} Credits)\n"
            return resp
        except Exception:
            return "Unable to fetch subjects right now."

    if "attendance" in message:
        return "Minimum 75% attendance is required to sit for end-semester exams."

    return "I'm sorry, I couldn't understand that. Try asking about subjects, syllabus, or attendance requirements!"
  
