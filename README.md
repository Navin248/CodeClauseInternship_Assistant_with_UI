# Robo-text-based-ai-assistant
This project implements Robo, a user-friendly AI assistant built with Python libraries. Robo utilizes speech recognition for understanding user queries and text-to-speech for generating responses.

Features:
        Speech Recognition: Leverages the speech_recognition library to convert spoken user input into text.
        Text-to-Speech: Integrates the pyttsx3 library to convert generated responses into spoken audio.
        Question Answering: Employs Google's Generative AI service (genai) to access and process information, formulating informative answers to user questions.
        Website Opening (Optional): Allows opening websites based on user requests using system commands (customizable).
        Customizable Tone (Optional): Enables adjusting Robo's communication style based on user input (further development required).

Technologies Used:
        Python 3.x
        SpeechRecognition
        pyttsx3
        Google Generative AI (genai) (API key required)
        tkinter (for user interface)
        Pillow (for image processing, if using background image)
Requirments:       
        Ensure you have Python 3.x installed.
        Install required libraries using pip:
        pip install speech_recognition pyttsx3 genai tkinter Pillow
        Obtain a Google Cloud Project API key and configure genai in the code (refer to genai documentation).
        pip install speech_recognition pyttsx3 genai tkinter Pillow
Usage
        Clone or download the project repository.
        (Optional) Replace background image (bg.jpg) and microphone icon (mic.png) with your desired files.
        Run the script:
        python assistant.py
        
        Click the microphone button or press Enter to activate speech recognition.
        
        Ask Robo questions or provide instructions.
