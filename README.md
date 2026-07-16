# AI Email Writer

## Overview
AI Email Writer is a Python-based application that generates professional emails using Google's Gemini AI model. Users simply enter their email requirement, and the application creates a well-structured email with a subject, greeting, body, and closing.

## Features
- Generate professional emails instantly
- User-friendly command-line interface
- AI-powered email content generation
- Customizable email requests
- Fast and efficient responses

## Technologies Used
- Python
- Google Gemini AI
- python-dotenv
- Google GenAI SDK

## Project Structure

AI-Email-Writer/
│
├── main.py
├── .gitignore
├── README.md
└── .env (not uploaded to GitHub)

## Installation

1. Clone the repository

```bash
git clone https://github.com/shivagangakubre-dotcom/AI-Email-Writer.git
```

2. Navigate to the project folder

```bash
cd AI-Email-Writer
```

3. Install dependencies

```bash
pip install google-genai python-dotenv
```

4. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Usage

Run the application:

```bash
python main.py
```

Enter your email requirement when prompted.

Example:

```text
Request leave for 2 days due to fever
```

The AI will generate a complete professional email.

## Example Output

Subject: Leave Request Due to Illness

Dear Sir/Madam,

I am writing to request leave for two days due to fever. I am currently unwell and require rest for recovery.

Thank you for your understanding.

Sincerely,
[Your Name]

## Future Enhancements
- Web-based interface using Streamlit
- Multiple email tone options
- Email templates
- Download generated emails as PDF

## Author
Kubre Shivaganga

## License
This project is created for educational and learning purposes.
