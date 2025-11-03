from difflib import get_close_matches
import json

def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, 1, cutoff=0.6)

    if matches:
        return matches[0]

def chatbot(knowledge: dict):
    while True:
        user_input: str = input('You: ')
        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            if best_match == 'bye':
                print(f'Bot: {answer}')
                break
            print(f'Bot: {answer}')
        else:
            print('Bot: I do not understand that')

if __name__ == '__main__':
    with open('questions.json', 'r', encoding='utf-8') as f:
        brain: dict = json.load(f)
        # brain: dict = {'hello': 'hey there',
    #                'how are you': 'thanks',
    #                'what time is it': 'Don\'t know, don\'t care',
    #                'bye': 'see you!'}
    chatbot(knowledge=brain)


