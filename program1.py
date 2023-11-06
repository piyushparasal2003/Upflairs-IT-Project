import random
import time

def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python programming is fun and exciting!",
        "Practice makes perfect in typing.",
        "Coding is a valuable skill in today's world.",
        "I love to learn new programming languages."
    ]
    return random.choice(sentences)

def calculate_typing_speed(start_time, end_time, typed_words):
    words_per_minute = (typed_words / (end_time - start_time)) * 60
    return words_per_minute

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start...")
    
    sentence = generate_random_sentence()
    print("Type the following sentence:")
    print(sentence)
    
    input("Press Enter when you are ready to start typing...")
    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()
    
    typed_words = len(typed_text.split())
    speed = calculate_typing_speed(start_time, end_time, typed_words)
    
    print(f"\nYour typing speed is {speed:.2f} words per minute.")
    print("Thank you for taking the typing speed test!")

typing_speed_test()




