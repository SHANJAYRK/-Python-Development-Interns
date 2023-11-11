import time
import random

def generate_random_text():
    # You can replace this with an API call or use a predefined set of texts.
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and rewarding.",
        "Practice makes perfect!",
        "Python is a powerful programming language.",
        "Type, practice, and improve your skills.",
    ]
    return random.choice(texts)

def calculate_typing_speed(start_time, end_time, typed_text):
    words_typed = len(typed_text.split())
    minutes_elapsed = (end_time - start_time) / 60.0
    wpm = words_typed / minutes_elapsed
    return wpm

def typing_speed_test():
    print("Welcome to the Typing Speed Tester!")
    input("Press Enter to start the test.")
    
    # Generate random text for the user to type
    original_text = generate_random_text()
    print("\nType the following:\n")
    print(original_text)

    # Record the start time
    start_time = time.time()

    # User types the text
    typed_text = input("\nType the above text here:\n")

    # Record the end time
    end_time = time.time()

    # Calculate typing speed
    typing_speed = calculate_typing_speed(start_time, end_time, typed_text)

    print("\nTest completed!")
    print(f"Your typing speed: {typing_speed:.2f} WPM")

if __name__ == "__main__":
    typing_speed_test()

