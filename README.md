# Project Title (e.g., Gemini ATS Resume Classifier)

## Code in the Master Branch..😊


## Table of Contents
- [About](#about)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Setup Google API Key](#setup-google-api-key)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About
[Choose one of the detailed descriptions above, or combine elements. This section explains what your project is and why it's useful.]

## Features
* Professional HR evaluation of resume vs. job description.
* Personalized skill improvement suggestions.
* Precise percentage match score with keyword breakdown.
* User-friendly Streamlit interface.
* Supports PDF resume uploads.

## How It Works
1.  **User Input:** The user provides a job description via a text area and uploads a resume in PDF format.
2.  **PDF Processing:** PyMuPDF extracts the content (specifically the first page as an image) from the uploaded PDF.
3.  **AI Analysis:** The extracted resume content, along with the job description and specific prompts, is sent to the Google Gemini-1.5-Flash model.
4.  **Intelligent Response:** Gemini processes the input and generates a detailed response based on the chosen query (evaluation, skill improvement, or percentage match).
5.  **Display Results:** The generated response is displayed clearly on the Streamlit interface.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (You'll need to create a `requirements.txt` file. See the section below.)

## Usage

1.  **Set up your Google API Key:** (See the `Setup Google API Key` section below)

2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    (Assuming your main Streamlit script is named `app.py`)

3.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## Technologies Used
* **Python**
* **Streamlit:** For building the interactive web application.
* **Google Generative AI (Gemini API):** For resume analysis and natural language processing.
* **PyMuPDF (fitz):** For robust PDF parsing and image extraction.
* **Pillow (PIL):** For image manipulation.
* **python-dotenv:** For managing environment variables (API keys).

## Setup Google API Key

1.  Go to the [Google AI Studio](https://aistudio.google.com/app/apikey) and generate your API key.
2.  Create a file named `.env` in the root directory of your project.
3.  Add your API key to the `.env` file in the following format:
    ```
    GOOGLE_API_KEY="your_api_key_here"
    ```
    (Replace `your_api_key_here` with your actual key.)

## Contributing
We welcome contributions! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. (You should create a LICENSE file if you don't have one.)

## Contact
Your Name - [Your LinkedIn/GitHub Profile/Email]
