from datetime import datetime
from google import genai
from dotenv import load_dotenv
load_dotenv()  # this reads .env automatically
import os
import json

def load_data():
    try:
        with open("notes.json", "r") as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open("notes.json", "w") as file:
        json.dump(data, file, indent=2)

def save_response(response, question):
    data = load_data()
    data.append({
        "question": question,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "response": response
    })
    save_data(data)

    

def gen_content():

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  

  
    length = input("Enter the desired response length (short/medium/long): ")
    question = input("Enter your question: ")
    query= f"Please provide a {length} answer to the following question: {question}.make it informative and don't add unnecessary follow-up questions."


    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=query
    )
    save_response(response.text, question)
    print("\n✅ Notes saved successfully!\n")

def view_notes():
    data=load_data()
    if not data:
        print("No notes available.")
        return
    print("\nChoose a note to view:\n")
    for i, note in enumerate(data):
        print(f"{i + 1}. Note: {note['question']}\n   Timestamp: {note['timestamp']}\n")
    choise=input("Enter the number of the note to view (or 'q' to quit): ")
    if choise.lower() == 'q':
        return
    try:
        index = int(choise) - 1
        if 0 <= index < len(data):
            note = data[index]
            print(f"\nQuestion: {note['question']}\nTimestamp: {note['timestamp']}\nResponse: {note['response']}\n")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_note():
    data = load_data()
    if not data:
        print("No notes available to delete.")
        return

    for i, note in enumerate(data):
        print(f"{i + 1}. {note['question']} - {note['timestamp']}")

    try:
        choice = int(input("Enter the number of the note to delete: "))
        if 1 <= choice <= len(data):
            del data[choice - 1]
            save_data(data)
            print("Note deleted successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

