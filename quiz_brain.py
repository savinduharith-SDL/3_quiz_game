class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score= 0

    def check_answer(self,given_answer):
        if(self.question_list[self.question_number-1].answer.lower() == given_answer.lower()):
            return True
        return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = current_question.text
        question_answer = current_question.answer
        answer = input(f"Q.{self.question_number}: {question_text}. (True/False)?: ")
        if(self.check_answer(answer)):
            self.score += 1
            print(f"Answer is correct! Score is {self.score} / {self.question_number}")
        else:
            print("Wrong!!")
        print("\n")

    def still_has_question(self):
        if(len(self.question_list) > self.question_number):
            return True
        else:
            return False
