class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        # if self.question_number == len(self.question_list)-1:
        #     return False
        return (self.question_number < len(self.question_list))

    def next_question(self):
        ans = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text}(True/False)?") 
        if ans == self.question_list[self.question_number].answer:
            print("Right answer!")
        else:
            print("Wrong answer!")
        
        # add one to question number
        self.question_number += 1
        