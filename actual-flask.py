from flask import Flask,request,jsonify
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
global questions
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
    mycursor = mydb.cursor()
    global question,questions,score,level
    score = 0
    question=0
    questions={}
    level="Easy"
    for i in ["Easy","Medium","Hard"]:
        mycursor.execute("SELECT * FROM quiz WHERE Mode = %s ORDER BY RAND() LIMIT 5",(i,))
        myresult = mycursor.fetchall()
        l=[]
        for x in myresult:
            if x[2]==i:
                d={}
                d['question']=x[1]
                d['options']=[x[4],x[5],x[6],x[7]]
                d['answer']=x[3]
                l.append(d)
        questions[i]=l
    print(questions)
    for i in range(5):
        
        vari=quiz(level)
        print (vari)
        global player_answer,current_question
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
    print("Your score is",score)
    return "Your score is {}.Thankyou!!!".format(score)
@app.route('/quiz/<levell>', methods=['GET'])
@app.route('/quiz/<levell>/<int:number>', methods=['GET'])
def level_based(levell,number=None):
    if number==None:
        number=5
    else:
        pass
    global level,question,questions,score
    level=levell
    mycursor = mydb.cursor()
    score = 0
    question=0
    questions={}
    mycursor.execute("SELECT * FROM quiz WHERE Mode = %s ORDER BY RAND() LIMIT 5", (level,))
    myresult = mycursor.fetchall()
    for i in [level]:
        l=[]
        for x in myresult:
            if x[2]==i:
                d={}
                d['question']=x[1]
                d['options']=[x[4],x[5],x[6],x[7]]
                d['answer']=x[3]
                l.append(d)
        questions[i]=l
    for i in range(number):
        vari=quiz(level)
        print (vari)
        global player_answer,current_question
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
@app.route('/update-quiz', methods=['GET'])
def get_update_quiz():
    return jsonify({'message': 'Invalid method'}), 405

@app.route('/update-quiz', methods=['PUT'])
def update_quiz():
    data = request.get_json()
    if not data or 'question' not in data or 'options' not in data or 'answer' not in data:
        return jsonify({'message': 'Invalid data'}), 400

    question = data['question']
    options = data['options']
    answer = data['answer']

    mycursor = mydb.cursor()
    query = "INSERT INTO quiz (Question, Mode, Option1, Option2, Option3, Option4, Answer) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (question, 'Easy', options[0], options[1], options[2], options[3], answer)
    mycursor.execute(query, values)
    return jsonify({'message': 'Quiz question added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
