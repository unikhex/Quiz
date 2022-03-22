
    
#beggining with the normal class,and variables that will be inside
class Question:
     def __init__(self, ques, answer ):
          self.ques = ques
          self.answer = answer
          
#my questions, they related to avengers, i will add more later
question_ques = [
     "What is the first name of iron man??\n(a) Tony\n(b)Stark",
     "Who is the god of lighting in avengers?\n(a) Scarlet witch\n(b)Thor",
     "Which class are we in?\n (a) Teinf20 (b) TeTek"
     
]
questions = [
    Question(question_ques[0],"a"),
    Question(question_ques[1],"b"),
    Question(question_ques[2],"a")
]

#the above is a varible showing the answers, i forgot to put a comma afterword making everything not run in the end

#defining the questions 
# adding the score
#and running the quiz
def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.ques)
          if answer == question.answer:
               score += 1
     print("you got", str(score), "out of", len(questions))

run_quiz(questions)