from flask import Flask
import mysql.connector
import random


app = Flask(__name__)
app.debug = True
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678A@',
    port='3306',
    database='example'
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM quiz")

myresult = mycursor.fetchall()
global question,level
li=['Easy','Medium','Hard']
questions={}
for i in li:
    l=[]
    for x in myresult:
        if x[2]==i:
            d={}
            d['question']=x[1]
            d['options']=[x[4],x[5],x[6],x[7]]
            d['answer']=x[3]
            l.append(d)
    questions[i]=l
for i in questions:
    random.shuffle(questions[i])
    random.shuffle(questions[i])
score = 0
level="Easy"
question=0
print("Welcome to the Chess Quiz Game!")
print("Answer the questions correctly to increase the difficulty level.")
def quiz(level):
            global current_question
            current_question = questions[level].pop(0)
            print("\nQuestion:", current_question['question'])
            print("Options:")
            for i, option in enumerate(current_question['options']):
                print(f"{i+1}. {option}")
            return "\n"

@app.route('/')
def Home():
    return "Hello!.This is a basic api built using flask.Answer the questions in the command promt.Total 5 questions.To start enter /quiz in url.There are three modes namely Easy,Medium and Hard.You can select specific mode by using /Mode in url.Additionally if you want to answer only few questions(less than 5) that also you can mention by /Mode/No. of questions.Have a good time "
@app.route('/quiz', methods=['GET'])
def full():
    for i in range(5):
        global level
        vari=quiz(level)
        print (vari)
        global question,score,player_answer,current_question
        answer_index = int(input("Enter your answer (1-4): ")) - 1
        player_answer = current_question['options'][answer_index]
        question+=1
        if player_answer == current_question['answer']:
            score += 1
            print("Correct answer!")
            if score == 2:
                level = 'Medium'
            elif score == 4:
                level = 'Hard'
        else:
            print("Wrong answer!")
        if not questions[level]:
            random.shuffle(questions[level])
            random.shuffle(questions[level])
    print("Your score is",score)
    return "Your score is {}.Thankyou!!!".format(score)
@app.route('/quiz/<levell>', methods=['GET'])
def level_based(levell):
    global level
    level=levell
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM quiz WHERE Mode = %s", (level,))
    myresult = mycursor.fetchall()
    questions={}
    for i in li:
        l=[]
        for x in myresult:
            if x[2]==i:
                d={}
                d['question']=x[1]
                d['options']=[x[4],x[5],x[6],x[7]]
                d['answer']=x[3]
                l.append(d)
        questions[i]=l
    if not questions[level]:
        random.shuffle(questions[level])
        random.shuffle(questions[level])
    for i in range(5):
        vari=quiz(level)
        print (vari)
        global question,score,player_answer,current_question
        answer_index = int(input("Enter your answer (1-4): ")) - 1
        player_answer = current_question['options'][answer_index]
        question+=1
        if player_answer == current_question['answer']:
            score += 1
            print("Correct answer!")
        else:
            print("Wrong answer!")
    print("Your score is",score)
    return "Your score is {}.Thankyou!!!!".format(score)
@app.route('/quiz/Easy/<int:integer>', methods=['GET'])
def no_based(integer):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM quiz WHERE Mode = 'Easy'")
    myresult = mycursor.fetchall()
    questions={}
    for i in li:
        l=[]
        for x in myresult:
            if x[2]==i:
                d={}
                d['question']=x[1]
                d['options']=[x[4],x[5],x[6],x[7]]
                d['answer']=x[3]
                l.append(d)
        questions[i]=l
    if not questions['Easy']:
        random.shuffle(questions['Easy'])
        random.shuffle(questions['Easy'])
    for i in range(integer):
        vari=quiz("Easy")
        print (vari)
        global question,score,player_answer,current_question
        answer_index = int(input("Enter your answer (1-4): ")) - 1
        player_answer = current_question['options'][answer_index]
        question+=1
        if player_answer == current_question['answer']:
            score += 1
            print("Correct answer!")
        else:
            print("Wrong answer!")
    print("Your score is",score)
    return "Your score is {}.Thankyou!!!!".format(score)
@app.route('/quiz/Medium/<int:integer>', methods=['GET'])
def num_based(integer):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM quiz WHERE Mode = 'Medium'")
    myresult = mycursor.fetchall()
    questions={}
    for i in li:
        l=[]
        for x in myresult:
            if x[2]==i:
                d={}
                d['question']=x[1]
                d['options']=[x[4],x[5],x[6],x[7]]
                d['answer']=x[3]
                l.append(d)
        questions[i]=l
    if not questions['Medium']:
        random.shuffle(questions['Medium'])
        random.shuffle(questions['Medium'])
    for i in range(integer):
        vari=quiz("Medium")
        print (vari)
        global question,score,player_answer,current_question
        answer_index = int(input("Enter your answer (1-4): ")) - 1
        player_answer = current_question['options'][answer_index]
        question+=1
        if player_answer == current_question['answer']:
            score += 1
            print("Correct answer!")
        else:
            print("Wrong answer!")
    print("Your score is",score)
    return "Your score is {}.Thankyou!!!!".format(score)
@app.route('/quiz/Hard/<int:integer>', methods=['GET'])
def number_based(integer):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM quiz WHERE Mode = 'Hard'")
    myresult = mycursor.fetchall()
    questions={}
    for i in li:
        l=[]
        for x in myresult:
            if x[2]==i:
                d={}
                d['question']=x[1]
                d['options']=[x[4],x[5],x[6],x[7]]
                d['answer']=x[3]
                l.append(d)
        questions[i]=l
    if not questions["Hard"]:
        random.shuffle(questions['Hard'])
        random.shuffle(questions['Hard'])
    for i in range(integer):
        vari=quiz("Hard")
        print (vari)
        global question,score,player_answer,current_question
        answer_index = int(input("Enter your answer (1-4): ")) - 1
        player_answer = current_question['options'][answer_index]
        question+=1
        if player_answer == current_question['answer']:
            score += 1
            print("Correct answer!")
        else:
            print("Wrong answer!")
    print("Your score is",score)
    return "Your score is {}.Thankyou!!!!".format(score)
if __name__ == '__main__':
    app.run(debug=True)
