
# LLM Email-Based Model

Welcome to the LLM Email-Based Model project. This project aims to create a Language Model (LLM) based on emails sent by users. By processing and training on a user's email data, the model can answer queries related to the user's email history, linguistic changes over time, and more.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [Contact](#contact)
- [License](#license)

## Introduction

This project was born out of the idea to understand and analyze a user's email communication over time. By leveraging the power of LLMs, we can gain insights into the user's communication patterns, linguistic changes, and more.

## Interface Screenshots

### Interface
![Interface](.projeto-llm/templates/interface.png)

### Landing Page
![Landing Page](.projeto-llm/templates/landingpage.png)

### Login Page
![Login Page](.projeto-llm/templates/loginpage.png)

### Signup Page
![Signup Page](.projeto-llm/templates/signuppage.png)

## 1. Overview of the Algorithm Construction

In the development of our LLM (Language Learning Model) based on user emails, we followed a systematic approach:

-  Authentication : We implemented OAuth2 authentication to access a user's Gmail account. This ensures secure access to the user's sent emails without compromising their credentials.

-  Email Processing : After successful authentication, we access the user's sent emails. These emails are then processed and converted into a format suitable for training our LLM. We utilized the mbox format, which is a standard format for storing email messages, and converted it into intermediary formats like JSON for easier processing.

-  Model Training : Using the processed emails, we trained an LLM using the LangChain library. LangChain provides a streamlined approach to training language models using various sources of data.

-  API for Queries : We developed a Flask-based API that allows users to query the trained LLM. This provides an interactive way for users to get insights from their email data.

-  Technologies Used :
  - Flask: For creating the web-based interface and API.
  - LangChain: For training the LLM and processing language data.
  - OAuth2: For secure authentication with Gmail.
  - Pinecone: To store the LLM vector database online.
  - CORS:  flask_cors==3.0.10

Certainly! Here's a comprehensive guide on setting up, training, and using the system, suitable for inclusion in the README:

---

## Setup, Training, and Usage Guide

### 1. Project Setup

#### Prerequisites:
- Python 3.8 or newer
- A Gmail account for testing

#### Steps:
1. Clone the Repository:
   ```
   git clone [https://github.com/dougdotcon/LLMemailAnalyzer]
   cd projeto_llm
   ```

2.  Install Dependencies :
   ```
   pip install -r requirements.txt
   ```

3.  Set Up OAuth 2.0 for Gmail :
   - Go to the [Google Developers Console](https://console.developers.google.com/).
   - Create a new project.
   - Enable the Gmail API for the project.
   - Create OAuth 2.0 credentials.
   - Download the `credentials.json` file and place it in the root directory of the project.

### 2. Training the LLM Model

1. Authenticate with Gmail:
   Run the `auth.py` script to authenticate with Gmail and obtain an access token.
   ```
   python src/auth.py
   ```
   Follow the on-screen instructions to authenticate and grant the necessary permissions.

2. Process Emails:
   Run the `mbox_processor.py` script to fetch emails from Gmail and save them in the `input.mbox` file.
   ```
   python src/mbox_processor.py
   ```

3. Train the LLM Model:
   Run the `llm_trainer.py` script to train the LLM model using the processed emails.
   ```
   python src/llm_trainer.py
   ```
   This will train the model and save it in the `/models` directory.

### 3. Using the System

1. Start the Flask API:
   ```
   python src/api.py
   ```
   This will start the Flask server on port 5000.

2. Access the Web Interface:
   Open a web browser and navigate to `http://localhost:5000`. You'll see the LLM Query Interface where you can type in questions and get responses from the trained LLM model.

3. Query the Model:
   - Type a question in the provided text area (e.g., "When was the last time I emailed Joe?").
   - Click "Send".
   - The system will display the model's response below your question.

### 4. Additional Notes

- Model Optimization: Depending on the quality of the model's responses, you might need to adjust the training parameters or preprocess the emails differently.
  
- Security: If deploying in a production environment, ensure you have proper security measures in place, especially regarding authentication and token storage.

## 2. Places to Replace for Testing

For users looking to test and adapt this project, the following placeholders and sections need to be replaced or configured:

- Authentication:
  - Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with your OAuth2 credentials for Gmail authentication in `auth.py`.

- Email Processing:
  - If you're using a different email service, adjust the email fetching logic in `auth.py`.

- Model Training:
  - In `llm_trainer.py`, you might want to adjust the training parameters or use a different base model from Hugging Face Hub.

- API Configuration:
  - If deploying the Flask API, adjust the server and port configurations in `api.py`.

## 3. Purpose of Our Project

Our project aims to provide users with a unique perspective on their email communication patterns. By training a Language Learning Model (LLM) on a user's sent emails, we can derive insights and answer queries related to their communication habits. Questions like "When was the last time I emailed Joe?", "How has my language changed over the past 10 years?", or "Any friend I'm losing touch with?" can be answered. This not only offers a reflection on one's communication style but also aids in understanding and improving personal and professional relationships.

## System Flow:

1.  Authentication (`auth.py`) :
    - The user accesses the web interface (powered by Flask) and clicks on a button/link to authenticate using their Gmail account.
    - The system redirects the user to the Gmail login page.
    - Upon successful authentication, Gmail redirects the user back to the application with an access token.

2.  Email Processing (`mbox_processor.py`) :
    - Using the access token obtained from the previous step, the system makes calls to the Gmail API to fetch the user's emails.
    - The retrieved emails are processed and saved in an mbox file (`input.mbox`).

3.  LLM Model Training (`llm_trainer.py`) :
    - The system reads the processed mbox file.
    - Using the LangChain library, the system trains an LLM model with the fetched emails.
    - The trained LLM model is saved in the `/models` directory.

4.  LLM Model Query (`api.py` and `templates`) :
    - The user accesses the web interface and is presented with a form where they can input a question.
    - The user inputs a question (e.g., "When was the last time I emailed Joe?") and clicks "Query".
    - The question is sent to the backend, which queries the trained LLM model.
    - The LLM model's response is displayed on the web interface for the user.

## Use Case Example:

1. Douglas accesses the application and sees an option to "Connect with Gmail". He clicks on it.
2. He's redirected to the Gmail login page and enters his credentials.
3. After successful authentication, he's redirected back to the application.
4. The application begins processing his emails and saves the data in the `input.mbox` file.
5. The system trains the LLM model using the processed emails.
6. Douglas is presented with an interface where he can input questions to query the LLM model.
7. He inputs the question: "When was the last time I emailed Joe?" and clicks "Query".
8. Within moments, the response is displayed: "You emailed Joe 3 days ago."
9. Douglas can continue to ask further questions or exit the application.

## Features

- Email Authentication: Authenticate with a user's email address.
- Email Processing: Process mbox files, converting them into intermediate formats (HTML/PDF) for training.
- LLM Training: Train a new LLM based on the processed emails.
- Query Interface: A simple API to query the trained LLM with questions like:
  - "When was the last time I emailed Joe?"
  - "How has my language changed over the past 10 years?"
  - "Any friends I'm losing touch with?"

## Setup and Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory and install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
3. Set up any necessary environment variables or configurations as detailed in the `src/auth.py` module.
4. Run the main application (instructions provided in the [Usage](#usage) section).

## Usage

1. Authenticate with your email address.
2. Provide the mbox file (typically named `input.mbox` and located in the `data` directory).
3. Process the mbox file to convert emails into the desired intermediate format.
4. Train the LLM using the processed data.
5. Start the Flask API and make queries to the trained LLM.

Detailed instructions and examples will be provided in the respective modules.

## Contributors

-  Douglas Asimov : Project Lead and Developer

## Contact

For any inquiries, suggestions, or collaborations, feel free to reach out:

- Twitter: [@dougdotcon](https://twitter.com/dougdotcon)
- Facebook: [dougdotcon](https://www.facebook.com/dougdotcon)
- ... and on other platforms as `dougdotcon`.

## License

This project is open-source and available under the MIT License. See the `LICENSE` file for more details.


