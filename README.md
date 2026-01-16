# AI Study Vault 🤖📚

**A simple CLI note-taking utility powered by Google GenAI (Gemini).**

This project lets you ask questions to the Gemini model, saves the generated answers as notes in a local `notes.json`, and provides commands to view or delete those notes.

---

## 🚀 Features

- Generate content or answers using Google GenAI (Gemini)
- Save generated responses with timestamps to `notes.json`
- View saved notes from the command line
- Delete notes you no longer need

---

## 🔧 Requirements

- Python 3.10+
- A Google GenAI API key with access to Gemini
- The dependencies listed in `requirements.txt`

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd AI-Study-Vault
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

The application reads the key from the `GEMINI_API_KEY` environment variable using `python-dotenv`.

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

You will see a simple menu:

1. Make a note — prompts for question and response length (short/medium/long) and saves the generated response
2. View Notes — list and view saved notes
3. Delete Note — remove a saved note
4. Exit — close the application

Saved notes are stored in `notes.json` in the project root.

---

## 💡 Notes & Tips

- If `notes.json` does not exist or is empty, it will be created/initialized automatically.
- The app uses `gemini-flash-latest` by default; you can change this in `core.py` if desired.

---

## Project Status

Closer (Not Maintained)
