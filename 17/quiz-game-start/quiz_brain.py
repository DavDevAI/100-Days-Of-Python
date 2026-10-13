class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.score = 0

    def still_has_question(self):
        while self.question_number < len(self.questions_list):
            return True
        return False
    def next_question(self):
        current_q = (self.questions_list[self.question_number])
        self.question_number +=1
        answer = input(f"Q. {self.question_number}: {current_q.text} (True/False): ")
        self.check_answer(answer, current_q.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")