import socketio

# Inicjalizacja klienta Socket.IO
sio = socketio.Client()

# Globalne zmienne
username = None
current_question_index = 0

# Obsługa połączenia z serwerem
@sio.on('connect')
def on_connect():
    global username
    print("Połączono z serwerem quizu!")
    if not username:  # Zapytaj o nazwę użytkownika tylko raz
        username = input("Podaj swoją nazwę użytkownika: ")
    sio.emit('get_question', {"username": username, "index": current_question_index})

@sio.on('disconnect')
def on_disconnect():
    print("Rozłączono z serwerem!")

@sio.on('quiz_start')
def on_quiz_start(data):
    print(data['message'])

@sio.on('question')
def on_question(data):
    global current_question_index
    print(f"Pytanie: {data['question']}")
    for i, option in enumerate(data['options'], start=1):
        print(f"{i}. {option}")
    answer = input("Wybierz numer odpowiedzi: ")
    try:
        answer_index = int(answer) - 1
        sio.emit('submit_answer', {
            "username": username,
            "index": current_question_index,
            "answer": data['options'][answer_index]
        })
    except (ValueError, IndexError):
        print("Niepoprawna odpowiedź! Spróbuj ponownie.")
        sio.emit('get_question', {"username": username, "index": current_question_index})  # Wyślij pytanie jeszcze raz

@sio.on('answer_result')
def on_answer_result(data):
    global current_question_index
    if data['result'] == "correct":
        print(f"Poprawna odpowiedź! Twój wynik: {data['score']}")
    else:
        print(f"Zła odpowiedź! Twój wynik: {data['score']}")
    current_question_index += 1
    print(f"Proszę o kolejne pytanie (index: {current_question_index})")
    sio.emit('get_question', {"username": username, "index": current_question_index})

@sio.on('end_quiz')
def on_end_quiz(data):
    print(data['message'])
    print("Koniec quizu!")
    sio.disconnect()

# Główna logika klienta
if __name__ == '__main__':
    try:
        print("Łączenie z serwerem...")
        sio.connect('http://127.0.0.1:5000')  # Połącz z serwerem
        sio.wait()  # Poczekaj na zakończenie połączenia
    except Exception as e:
        print("Nie udało się połączyć z serwerem:", e)





