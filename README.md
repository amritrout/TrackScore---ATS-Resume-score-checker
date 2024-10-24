# Resume ATS Scanner

A Streamlit-based application that uses Google's Gemini AI to analyze resumes against job descriptions, providing ATS scoring and keyword analysis.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Google API Setup](#google-api-setup)
  - [Local Setup](#local-setup)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)

## Features

* **ATS Score Analysis**: Get a percentage match between your resume and job description
* **Missing Keywords Detection**: Identify key skills and keywords missing from your resume
* **Profile Summary**: Receive an AI-generated summary of your professional profile
* **PDF Support**: Upload and analyze PDF resumes
* **Clean Text Processing**: Automated text normalization and cleaning

## Prerequisites

* Python 3.8+
* Google Cloud Account
* PDF Resume
* pip (Python package installer)

## Getting Started

### Google API Setup

1. **Create a Google Cloud Account**:
   * Go to [Google Cloud Console](https://console.cloud.google.com/)
   * Sign up for a new account if you don't have one

2. **Enable Gemini API**:
   * Navigate to "APIs & Services" > "Dashboard"
   * Click "+ ENABLE APIS AND SERVICES"
   * Search for "Gemini API"
   * Click "Enable"

3. **Create API Key**:
   * Go to "APIs & Services" > "Credentials"
   * Click "CREATE CREDENTIALS" > "API key"
   * Copy your API key
   * (Optional) Restrict the API key to only Gemini API

### Local Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd resume-ats-scanner
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

## Installation

1. Install required packages:
```bash
pip install streamlit google-generativeai python-dotenv PyPDF2
```

2. Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your_api_key_here
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Access the application in your browser at `http://localhost:8501`

3. Use the interface:
   * Paste the job description in the text area
   * Upload your resume in PDF format
   * Click "Submit" to get your analysis

## Configuration

### Environment Variables

Create a `.env` file with the following variables:
```
GOOGLE_API_KEY=your_api_key_here
```

### Application Settings

The application uses the following configurations:
* Model: `gemini-pro`
* File types supported: PDF
* Maximum file size: Determined by Streamlit's default settings

## Troubleshooting

### Common Issues

1. **API Key Error**:
   * Verify your API key in the `.env` file
   * Ensure the API is enabled in Google Cloud Console
   * Check if the API key has proper permissions

2. **PDF Upload Issues**:
   * Ensure PDF is not password protected
   * Check file size limits
   * Verify PDF is text-based (not scanned)

3. **Response Parsing Error**:
   * Check if job description is empty
   * Ensure resume is properly formatted
   * Verify PDF text extraction is successful

### Error Messages

* "Failed to parse the response": Issue with API response format
* "Please upload a valid resume": PDF upload required
* "Please provide a valid job description": Job description field is empty

## File Structure
```
resume-ats-scanner/
├── app.py               # Main application file
├── .env                 # Environment variables
├── requirements.txt     # Project dependencies
└── README.md           # Documentation
```

## Dependencies

```
streamlit==1.24.0
google-generativeai==0.3.0
python-dotenv==1.0.0
PyPDF2==3.0.1
```

## Security Notes

* Never commit your `.env` file
* Restrict your API key's usage in Google Cloud Console
* Regularly rotate your API keys
* Monitor API usage for unusual patterns

---

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## License

This project is licensed under the MIT License - see the LICENSE file for details.