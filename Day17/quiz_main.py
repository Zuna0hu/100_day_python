from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# to construct a question bank

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

# print(question_bank)

Quiz = QuizBrain(question_bank)

while (Quiz.still_has_questions()):
    Quiz.next_question()
Quiz.print_final_score()




















# The following code is a test

# create a class

# class User: # Pascal Case
#     def __init__(self, id, username):
#         self.id = id
#         self.username = username

#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# # user_1 = User()
# # user_1.id = "001" # create a variable
# # user_1.username = "angela" # create another variable

# # user_2 = User()
# # user_2.id = "002"
# # user_2.username = "jacques" # the starting information are repeated

# # print(user_1.id)
# # print(user_1.username)
# user_1 = User("001", "angela")
# user_2 = User("002", "jack")

# user_1.follow(user_2)

# print(user_1.following)
# print(user_1.followers)

# print(user_2.following)
# print(user_2.followers)