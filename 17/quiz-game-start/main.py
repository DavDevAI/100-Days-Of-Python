from question_model import Question
from quiz_brain import QuizBrain
import data as qd

question_bank = []
#q2 = Question(qd.question_data[0]["text"], qd.question_data[0]["answer"])
#print(q2.text)

idx = 0
for question in qd.question_data:
    idx +=1
    q = Question(qd.question_data[idx-1]["question"], qd.question_data[idx-1]["correct_answer"])
    question_bank.append(q) #now Question Bank would be a list of objects
    #IF I WANTED TO APPEND IT AND SAVE IT AS A STRING AND NOT AN OBJECT
    # question_bank.append(q.text)

nq = QuizBrain(question_bank)
while nq.still_has_question():
    nq.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {nq.score}/{nq.question_number}")