import random

# Dictionaries for each language
korean_dict = {
    "hello": "안녕하세요",
    "thank you": "감사합니다",
    "please": "제발",
    "goodbye": "안녕히 가세요",
    "water": "물",
    "food": "음식",
    "love": "사랑",
    "family": "가족",
    "friend": "친구",
    "house": "집",
    "school": "학교",
    "book": "책",
    "teacher": "선생님",
    "car": "자동차",
    "dog": "개"
}

german_dict = {
    "hello": "hallo",
    "thank you": "danke",
    "please": "bitte",
    "goodbye": "auf wiedersehen",
    "water": "wasser",
    "food": "essen",
    "love": "liebe",
    "family": "familie",
    "friend": "freund",
    "house": "haus",
    "school": "schule",
    "book": "buch",
    "teacher": "lehrer",
    "car": "auto",
    "dog": "hund"
}

dutch_dict = {
    "hello": "hallo",
    "thank you": "dank je",
    "please": "alsjeblieft",
    "goodbye": "tot ziens",
    "water": "water",
    "food": "eten",
    "love": "liefde",
    "family": "familie",
    "friend": "vriend",
    "house": "huis",
    "school": "school",
    "book": "boek",
    "teacher": "leraar",
    "car": "auto",
    "dog": "hond"
}

def select_language():
    """Prompt the user to select a language."""
    print("\nChoose a language to practice:")
    print("1. Korean")
    print("2. German")
    print("3. Dutch")
    print("4. Exit Quiz")
    choice = input("Enter the number corresponding to your choice: ").strip()

    if choice == "1":
        return korean_dict, "Korean"
    elif choice == "2":
        return german_dict, "German"
    elif choice == "3":
        return dutch_dict, "Dutch"
    elif choice == "4":
        return None, "Exit"
    else:
        print("Invalid choice. Please select a valid option.")
        return select_language()

def language_flashcards():
    print("Welcome to LEARNINO - Learn N Fun ")

    while True:
        selected_dict, language = select_language()

        # Exit the quiz if the user selects "Exit"
        if language == "Exit":
            print("Thank you for playing! Goodbye!")
            break

        print(f"\nYou selected {language}. Match the English words to their meanings in {language}!")
        print("Type 'change' to switch languages or 'exit' to quit at any time.\n")

        words = list(selected_dict.keys())
        random.shuffle(words)

        score = 0
        for word in words:
            correct_answer = selected_dict[word]
            # Generate multiple choices including the correct answer
            options = list(selected_dict.values())
            options.remove(correct_answer)
            choices = random.sample(options, 3) + [correct_answer]
            random.shuffle(choices)

            # Display the question
            print(f"What is the meaning of '{word}' in {language}?")
            for i, choice in enumerate(choices, 1):
                print(f"{i}. {choice}")

            user_input = input("Enter the number of your choice (or type 'change'/'exit'): ").strip()

            # Handle 'change' and 'exit' inputs
            if user_input.lower() == "change":
                print("Switching language...\n")
                break
            elif user_input.lower() == "exit":
                print("Thank you for playing! Goodbye!")
                return

            # Validate the user's answer
            try:
                user_choice = int(user_input)
                if choices[user_choice - 1] == correct_answer:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is '{correct_answer}'.\n")
            except (ValueError, IndexError):
                print(f"Invalid input. The correct answer was '{correct_answer}'.\n")

        # Display the score for the current session
        print(f"Your score in {language}: {score}/{len(words)}\n")

# Run the flashcard program
language_flashcards()