from question_model import Question
from quiz_brain import QuizBrain
import data as qd

question_bank = []
#q2 = Question(qd.question_data[0]["text"], qd.question_data[0]["answer"])
#print(q2.text)

idx = 0
for question in qd.question_data:
    idx +=1
    q = Question(qd.question_data[idx-1]["text"], qd.question_data[idx-1]["answer"])
    question_bank.append(q)
    #IF I WANTED TO APPEND IT AND SAVE IT AS A STRING AND NOT AN OBJECT
    # question_bank.append(q.text)

nq = QuizBrain(question_bank)
while nq.still_has_question():
    nq.next_question()