import requests
from config import API_KEY, API_URL, MAX_TOKENS, TEMPERATURE

def consolidate_code_with_groq(transcript, extracted_data):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    consolidated_code = ""
    for frame_data in extracted_data:
        context = " ".join([cap['text'] for cap in transcript])
        prompt = f"Context:\n{context}\n\nCode Snippet:\n{frame_data['text']}\n\nConsolidate and improve the code based on the context."
        data = {
            "model": "llama-3.1-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS
        }
        response = requests.post(API_URL, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            consolidated_code += result['choices'][0]['message']['content'] + "\n\n"
    return consolidated_code
