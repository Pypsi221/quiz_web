from flask import Flask,render_template,request,session,redirect,url_for
from db.crud import get_quizes, get_questions_after, check_right_answer
from random import shuffle# імпортуємо необхідні модулі та функції


app = Flask(__name__)# ініціалізуємо додаток Flask
app.secret_key = "1234567890 "# секретний ключ для сесій

def start_session(quiz_id=0):
    # створюємо сесію для збереження стану тестування
    session["quiz_id"] = quiz_id
    session["last_question_id"] = 0
    session["correct_ans"] = 0
    session["wrong_ans"] = 0
    session["total"] = 0

def question_form(question):
    #формуємо сторінку з питанням та варіантами відповідей
    answwers_list = [
        question[2],
        question[3],   
        question[4],
        question[5]
    ]
    shuffle(answwers_list)
    return render_template("test.html", quest_id=question[0], quest=question[1], ans_list=answwers_list)
    
def check_answer(question_id, selected_answer):
    if check_right_answer(question_id, selected_answer):
        session["correct_ans"] += 1
    else:
        session["wrong_ans"] += 1
        session["total"] += 1

    
# Головна сторінка з вибором тесту
@app.route("/", methods=["GET", "POST"])

def index():
    # якщо метод гет одна логіка отримуємо іктоини тестів і відображаємо їх
    if request.method == "GET":
        quizes = get_quizes()
        start_session(-1)
        return render_template("index.html", quizes_list=quizes)
    else:
        # якщо метод пост - отримуємо вибраний тест і починаємо сесію тестування
        quiz_id = request.form.get("quiz")# отримуємо ід вибраного тесту з форми
        start_session(quiz_id)
        return redirect(url_for("test"))# перенаправляємо на сторінку тестування

    

# Сторінка тестування
@app.route("/test", methods=["GET", "POST"])
def test():
    # перевіряємо чи є активна сесія тестування
    if not ("quiz_id" in session)  or  int(session["quiz_id"]) < 0:
        return redirect(url_for("index"))
    else: 
        # якщо метод гет - отримуємо перше питання тесту
        if request.method == "POST":
            selected_answer = request.form.get("ans")
            question_id = int(request.form.get("quest_id"))
            check_answer(question_id, selected_answer)
            session["last_question_id"] = question_id
        # отримуємо наступне питання тесту
        new_question = get_questions_after(session["quiz_id"], session["last_question_id"])
        if new_question is None:
            return redirect(url_for("result"))
        else:
            return question_form(new_question)
        
@app.route("/result")# Сторінка з результатами тестування
def result():# відображаємо результати тестування
    result = render_template("result.html", right=session["correct_ans"], wrong=session["wrong_ans"], total=session["total"])# очищуємо сесію тестування
   #session.clear()
    return result

if __name__ == '__main__':# запускаємо додаток
    app.run()