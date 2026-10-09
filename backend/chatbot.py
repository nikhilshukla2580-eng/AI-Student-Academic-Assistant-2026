import json
import os

FAQ_FILE = os.path.join(os.path.dirname(__file__), '../data/faq.json')

def load_faqs():
    if os.path.exists(FAQ_FILE):
        with open(FAQ_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_faq(category, question, answer):
    faqs = load_faqs()
    faqs.append({"category": category, "question": question, "answer": answer})
    with open(FAQ_FILE, 'w', encoding='utf-8') as f:
        json.dump(faqs, f, indent=2)

def get_chatbot_response(user_message):
    query = user_message.lower().strip()
    faqs = load_faqs()

    # 1. Direct Keyword Matching from local FAQ database
    for item in faqs:
        if item['question'].lower() in query or query in item['question'].lower():
            return item['answer']

    # 2. APSU Quick Fallback Links
    if "marksheet" in query or "result" in query:
        return "APSU Marksheet portal par jaane ke liye link: https://share.google/y3DLZPbjaHIH6jnNy"
    elif "mponline" in query or "fee" in query:
        return "APSU MPOnline portal: https://apsu.mponline.gov.in/portal/"
    elif "website" in query or "official" in query:
        return "APSU Official Website: https://share.google/bolPJrwg8nLkSPfjN"

    # 3. Default Response
    return f"Aapke query '{user_message}' se related exact notice db mein nahi mila. Kripya APSU Official Portal visit karein: https://share.google/bolPJrwg8nLkSPfjN"
    
