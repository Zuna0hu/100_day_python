class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        # if self.question_number == len(self.question_list)-1:
        #     return False
        return (self.question_number < len(self.question_list))

    def next_question(self):
        question = self.question_list[self.question_number]
        ans = input(f"Q.{self.question_number+1}: {question.text}(True/False)?") 
        # check answer
        right_answer = question.answer
        self.check_answer(ans, right_answer)
        
        # add one to question number
        self.question_number += 1
        
    def check_answer(self, user_answer,right_answer):
        if user_answer.lower() == right_answer.lower():
            print("Right answer!")
        else:
            print("Wrong answer!")
        print(f"The right answer was: {right_answer} .")