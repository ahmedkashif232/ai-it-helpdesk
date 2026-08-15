# AI IT Help Desk Assistant

An AI-powered IT support application that analyzes user-reported technical issues and generates structured help-desk ticket information.

## Features

- Categorizes IT support issues
- Assigns Low, Medium, High, or Critical priority
- Identifies possible causes
- Generates practical troubleshooting steps
- Recommends whether the issue should be escalated
- Creates a formatted support-ticket summary
- Allows the completed ticket to be downloaded
- Warns users not to submit passwords or sensitive information

## Technologies

- Python
- Streamlit
- OpenAI Responses API
- python-dotenv

## How It Works

The user describes a technical issue through the Streamlit interface. The application sends the issue to a language model with instructions to behave as an IT help-desk triage assistant. The model returns a structured analysis containing the issue category, priority, likely cause, troubleshooting steps, escalation recommendation, and ticket summary.

## Tested Scenarios

The application was tested using common support situations, including:

1. A MacBook connected to Wi-Fi but unable to load websites
2. A suspected phishing email requesting immediate password verification

## Security

API credentials are stored in a local `.env` file and excluded from version control through `.gitignore`. The interface warns users not to enter passwords, API keys, financial information, or other sensitive data.

## Limitations

The assistant provides recommendations rather than guaranteed diagnoses. Important, sensitive, or high-priority incidents should be reviewed by a qualified IT or security professional.

## Run Locally

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

```bash
pip install -r requirements.txt