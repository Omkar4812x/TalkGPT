import os
from dotenv import load_dotenv
import openai
import speech_recognition as sr
import pyttsx3
import time

# Load environment variables from .env file
load_dotenv()

# Initialize the speech recognition and text-to-speech engines
engine = pyttsx3.init()
listener = sr.Recognizer()

# Set the OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    print("Please set your OpenAI API key before running the script.")
    print("You can do this by:")
    print("1. On Windows PowerShell: $env:OPENAI_API_KEY='your-api-key'")
    print("2. On Windows Command Prompt: set OPENAI_API_KEY=your-api-key")
    print("3. Create a .env file in the project directory with: OPENAI_API_KEY=your-api-key")
    exit(1)

def get_user_input():
    """Get user input using speech recognition"""
    with sr.Microphone() as source:
        print("Speak now...")
        try:
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            data = listener.recognize_google(voice)
            return data
            
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error during speech recognition: {e}")
            return None

def get_openai_response(prompt):
    """Get a response from OpenAI's chat completion API"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1024,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"OpenAI API error (Attempt {attempt + 1}/{max_retries}): {e}")
            
            # Check for specific quota-related errors
            error_message = str(e)
            if "insufficient_quota" in error_message:
                print("\n--- IMPORTANT API USAGE NOTICE ---")
                print("You have exceeded your current OpenAI API quota. Please:")
                print("1. Check your OpenAI account billing status")
                print("2. Verify your payment method")
                print("3. Add credits to your account")
                print("4. Check for any account restrictions")
                print("Visit: https://platform.openai.com/account/usage for details")
                print("-----------------------------------\n")
                return None
            
            # Wait before retrying
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2  # Exponential backoff
                print(f"Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
            else:
                print("Max retry attempts reached. Unable to get a response.")
                return None

def main():
    print("Voice-Enabled ChatGPT Assistant")
    print("Speak your question. Say 'exit' to quit.")
    
    while True:
        try:
            # Get user input via speech
            data = get_user_input()
            
            # Check for exit condition or no input
            if not data:
                continue
            if data.lower() == "exit":
                print("Exiting the assistant.")
                break

            # Get AI response
            response = get_openai_response(data)
            if not response:
                print("Could not get a response. Please check your API settings.")
                continue

            # Print response
            print("\nResponse:")
            print(response)

            # Optional speech output
            choice = input("\nPress 1 to print the response or press 2 to print and hear the response: ")
            if choice == "2":
                engine.say(response)
                engine.runAndWait()

            # Continue or exit
            repeat = input("\nDo you want to ask more questions? (yes/no): ")
            if repeat.lower() != "yes":
                break

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()