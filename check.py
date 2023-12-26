import mysql.connector
import random
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678A@',
    port='3306',
    database='example'
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE quiz (Qid VARCHAR(5) PRIMARY KEY, Question VARCHAR(200), Mode VARCHAR(10), Ans VARCHAR(20), Opt1 VARCHAR(20), Opt2 VARCHAR(20), Opt3 VARCHAR(20), Opt4 VARCHAR(20))")
#s="insert into quiz (Qid,Question,Mode,Ans,Opt1,Opt2,Opt3,Opt4) values (%s,%s,%s,%s,%s,%s,%s,%s)"
"""v=[
    ('E1','What is the smallest piece in chess?','Easy','Pawn','Pawn', 'King', 'Rook', 'Knight'),
    ('E2','Which piece moves in an L-shaped pattern?','Easy','Knight','Queen', 'Bishop', 'Rook', 'Knight'),
    ('E3','Which chess piece can only move diagonally?','Easy','Bishop','Queen', 'BIshop', 'Rook', 'Knight'),
    ('E4','How many pawns does each player start with?','Easy','8','16', '8', '10', '12'),
    ('E5','Which chess piece can move in any direction?','Easy','King','Pawn', 'King', 'Rook', 'Knight'),
    ('E6','What is the starting position of the white queen?','Easy','d1','e8', 'd8', 'e1', 'd1'),
    ('E7','Which chess piece can jump over other pieces?','Easy','Knight','Queen', 'King', 'Rook', 'Knight'),
    ('M1','What is the maximum number of moves required to checkmate an opponent?','Medium','3','4', '5', '2', '1'),
    ('M2','Which chess piece can move any number of squares in a straight line?','Medium','Rook','Bishop', 'King', 'Rook', 'Knight'),
    ('M3','Which chess piece is considered the most powerful(acc to points)?','Medium','Queen','Queen', 'King', 'Rook', 'Knight'),
    ('M4','In algebraic notation, which letter represents the vertical columns on a chessboard?','Medium','a-h','A-H', 'a-h', '1-8', 'A-G'),
    ('M5','Which chess piece can move both diagonally and forward/backward?(more than a square)','Medium','Bishop','Bishop', 'King', 'Rook', 'Knight'),
    ('M6','Which chess piece can move both diagonally and forward?(Only one square)','Medium','Pawn','Pawn', 'King', 'Rook', 'Knight'),
    ('M7','Which chess term is used for a condition where no move is possible yet there is no check?','Medium','Stalemate','Checkmate', 'Enpassant', 'Stalemate', 'Pin'),
    ('H1','What is the highest possible Elo rating a chess player can have?','Hard','3000','2000', '2500', '3000', '5000'),
    ('H2','Which chess player is considered the "Mozart of Chess"?','Hard','Magnus Carlsen','Magnus Carlsen', 'Bobby Fischer', 'Garry Kasparov', 'Viswanathan Anand'),
    ('H3','Which chess player held the World Chess Championship title for the longest consecutive period?','Hard','Garry Kasparov','Magnus Carlsen', 'Bobby Fischer', 'Garry Kasparov', 'Anatoly Karpov'),
    ('H4','Which chess player famously defeated a supercomputer in a match?','Hard','Garry Kasparov','Viswanathan Anand', 'Vladimir Kramnik', 'Garry Kasparov', 'Fabiano Caruana'),
    ('H5','What is the objective of a chess game?','Hard','Checkmate','Checkmate', 'Capture all pieces', 'Control the board', 'Promote pawn'),
    ('H6','Which chess opening is named after a river in Russia?','Hard','Volga Gambit','King\'s Gambit', 'Nimzo-Indian Defense', 'Volga Gambit', 'Queen\'s Gambit'),
    ('H7', 'Which chess player was known for his eccentric behavior and unorthodox playing style?','Hard','Mikhail Tal','Viktor Korchnoi', 'Mikhail Tal', 'Boris Spassky', 'Anatoly Karpov'),
   ]"""
'''sql = "UPDATE quiz SET Opt2 = 'Bishop' WHERE Qid = 'E3'"
mycursor.execute(sql)

mydb.commit()'''
#mycursor.executemany(s,v)
#print(mycursor.rowcount,"was inserted.")
mycursor.execute("SELECT * FROM quiz")

myresult = mycursor.fetchall()
'''
for x in myresult:
  print()
  print(x[1])
  print(x[2])
  print(x[3])
  print(x[4])
  print(x[5])
  print(x[6])
  print(x[7])
  print()
'''
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
for level in questions:
    random.shuffle(questions[level])
level = 'Easy'
score = 0
question=0
print("Welcome to the Chess Quiz Game!")
print("Answer the questions correctly to increase the difficulty level.")

while score  < 5 and question<5:
    current_question = questions[level].pop(0)
    print("\nQuestion:", current_question['question'])
    print("Options:")
    for i, option in enumerate(current_question['options']):
        print(f"{i+1}. {option}")

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

    random.shuffle(questions[level])

print("\nCongratulations!")
print("You gained knowledge on chess!")
    
    
        
