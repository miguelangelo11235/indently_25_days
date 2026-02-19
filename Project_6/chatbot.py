from datetime import datetime

def contains(terms: list[str], content: str) -> bool:
    matches: list[bool] = []
    for term in terms:
        matches.append(term in content.lower())

    return any(matches)

def response(text: str) -> str:
    text = text.lower()

    if contains(["hello", "hi"], text):
        return "Hello there"
    elif contains(["goodbye", "bye"], text):
        return "Talk to you later!"

    elif contains(["what time is it", "current time"], text):
        return f"The time is {datetime.now()}"
    elif contains(["how are you"], text):
        return "I'm doing fine! Thanks for asking."
    else:
        return "Sorry, I can't answer that right now."


while True:
    user_input: str = input("You: ")
    bot_response: str = response(user_input)
    print(f"Bot: {bot_response}")
    if bot_response == "Talk to you later!":
        break