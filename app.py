from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' 
socketio = SocketIO(app)

scores = {}
questions = [
    {"question": "Ile wynosi 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "Jakie jest stolicą Polski?", "options": ["Warszawa", "Kraków", "Gdańsk"], "answer": "Warszawa"},
    {"question": "W którym roku rozpoczęła się II wojna światowa?", "options": ["1938", "1939", "1940"], "answer": "1939"},
]

@socketio.on('add_question')
def handle_add_question(data):
    questions.append({
        "question": data["question"],
        "options": data["options"],
        "answer": data["answer"]
    })
    print(f"Nowe pytanie dodane: {data['question']}")

@socketio.on('get_question')
def handle_get_question(data):
    username = data.get('username')
    question_index = data.get('index', 0)
    if username not in scores:
        scores[username] = 0 
    if question_index < len(questions):
        question = questions[question_index]
        emit('question', {'index': question_index, 'question': question['question'], 'options': question['options']})
    else:
        emit('end_quiz', {'message': f"Koniec quizu, {username}! Twój wynik to: {scores[username]} punktów."})

@socketio.on('submit_answer')
def handle_submit_answer(data):
    username = data.get('username')
    question_index = data.get('index')
    user_answer = data.get('answer')
    if question_index < len(questions):
        correct_answer = questions[question_index]['answer']
        if user_answer == correct_answer:
            scores[username] += 1 
            emit('answer_result', {'result': "correct", 'score': scores[username]})
        else:
            emit('answer_result', {'result': "wrong", 'score': scores[username]})
    else:
        emit('error', {'message': "Nieprawidłowy indeks pytania"})

@app.route('/')
def index():
    return "Serwer quizu działa poprawnie!"

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000)

