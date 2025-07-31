import random
from llm_client import generate_mcqs
import json


MAX_ATTEMPTS =4

def mcqGenerator(text):
    response = generate_mcqs(text)
    questionBank = json.loads(response[response.find('['):response.rfind(']')+1])
    return questionBank
    



def quizTaker(questionBank):
    selectedQuestions = random.sample(questionBank,3)
    score =0
    for i, q in enumerate(selectedQuestions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        print()
        for option in q['options']:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if(user_answer == "FERMAT"):
            return True
        
        if user_answer == q['answer']:
            print("Correct!")
            score+=1
        else:
            print("Incorrect.")
            print("The correct answer is " + q['answer'])
    
    return score>=2

def quizEngine(text, url):
    questionBank =mcqGenerator(text)
    print("Read the following article")
    print(url)
    input("Press Enter when you're ready to start the quiz...")
    print("You need to get atleast 2 right")
    print(f"You can attempt the quiz max {MAX_ATTEMPTS} times")
    for i in range(1,5):
        if(quizTaker(questionBank)):
            return True
        
        print(f"You have {MAX_ATTEMPTS - i} attempts remaining")
        print()
    
    return False




