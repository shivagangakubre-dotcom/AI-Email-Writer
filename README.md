# AI Email Writer V1

## Overview
AI Email Writer V1 is an AI-powered application developed using Python and Google's Gemini AI. It helps users generate professional emails by selecting an email type and tone, then automatically creating a well-structured email.

## Features
- AI-powered email generation
- Multiple email types
  - Leave Request
  - Job Application
  - Meeting Request
  - General Email
- Multiple tone options
  - Professional
  - Friendly
  - Formal
- Saves generated emails to a text file
- Easy-to-use command-line interface
- Error handling for smooth execution

## Technologies Used
- Python
- Google Gemini AI
- Google GenAI SDK
- python-dotenv

## Project Structure

AI-Email-Writer/
│
├── main.py
├── README.md
├── .gitignore
└── .env (not uploaded to GitHub)

## Installation

1. Clone the repository

```bash
git clone https://github.com/shivagangakubre-dotcom/AI-Email-Writer.git
```

2. Install dependencies

```bash
pip install google-genai python-dotenv
```

3. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Usage

Run:

```bash
python main.py
```

Follow the prompts:
1. Select email type
2. Select tone
3. Enter email requirement

The AI will generate a professional email and save it to a file.

## Future Enhancements
- Streamlit Web Interface
- PDF Download Feature
- Email Templates
- Copy-to-Clipboard Option
- Multiple Language Support

## Version History

### V0
- Basic AI email generation

### V1
- Email type selection
- Tone selection
- Save email to file
- Improved user experience

## Author
Kubre Shivaganga

## License
This project is for educational and learning purposes.