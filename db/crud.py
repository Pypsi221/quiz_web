import sqlite3 


DB_NAME = "quizes.db"
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()



def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS quiz(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title VARCHAR,
                   description TEXT
                   )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                   question VARCHAR,
                   answer VARCHAR,
                   wrong1 VARCHAR,
                   wrong2 VARCHAR,
                   wrong3 VARCHAR
                   )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS quiz_questions(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                   quiz_id  INTEGER,
                   question_id INTEGER,
                   FOREIGN KEY (quiz_id) REFERENCES quiz (id),
                    FOREIGN KEY (question_id) REFERENCES questions (id)
                   )''')
    

    conn.commit()
    close()

def add_quiz():
    open()

    quizes = [
    ("Міфи та легенди світу", 
     "Вікторина для любителів давніх історій — від грецьких богів до єгипетських міфів. Перевір, чи зможеш ти відрізнити Зевса від Тора!"
    ),

    ("Їжа навколо світу", 
     "Смачний тест про національні страви з різних куточків планети. Від борщу до суші — подорожуй кулінарно!"
    ),

    ("Попкультура ХХІ століття", 
     "Фільми, музика, меми й соціальні мережі — перевір, наскільки ти в темі сучасних трендів!"
    ),

    ("Детективна пригода", 
     "Поринь у світ загадок, злочинів і розслідувань. Чи зможеш ти мислити як справжній детектив?"
    ),

    ("Фантастичні світи", 
     "Від 'Матриці' до 'Володаря перснів' — тест для справжніх фанатів фентезі та наукової фантастики."
    )
    ]

    cursor.executemany("""INSERT INTO quiz(title,description) VALUES(?,?)""", quizes)
    conn.commit()
    close()
    
def add_questions():
    open()
    questions = [
        #енди світу
        ("Хто був головним богом у грецькій міфології?", "Зевс", "Арес", "Посейдон", "Гермес"),
        ("Як звали скандинавського бога грому?", "Тор", "Локі", "Одін", "Фрейр"),
        ("Який герой вкрав вогонь у богів і подарував його людям?", "Прометей", "Геракл", "Тесей", "Персей"),
        ("Як називається світ мертвих у давньоєгипетській міфології?", "Дуат", "Елізіум", "Асгард", "Гадес"),
        ("Яке створіння охороняло вхід до підземного царства Гадеса?", "Цербер", "Сфінкс", "Мінотавр", "Грифон"),

        # Їжа навколо світу
        ("З якої країни походить страва суші?", "Японія", "Китай", "Корея", "Таїланд"),
        ("Що є головним інгредієнтом піци Маргарита?", "Моцарела", "Салямі", "Курка", "Тунець"),
        ("У якій країні популярна страва такос?", "Мексика", "Іспанія", "Аргентина", "Бразилія"),
        ("Яка страва є національною для України?", "Борщ", "Плов", "Суші", "Паелья"),
        ("Що традиційно подають з британськими фіш-енд-чіпс?", "Картопля фрі", "Пюре", "Рис", "Овочевий салат"),

        # Попкультура ХХІ століття
        ("Яка соціальна мережа належить компанії Meta?", "Instagram", "TikTok", "X (Twitter)", "Snapchat"),
        ("Який співак виконав пісню 'Shape of You'?", "Ед Ширан", "Дрейк", "Шон Мендес", "Post Malone"),
        ("Яка гра стала світовим хітом у 2020 році з екіпажем і самозванцями?", "Among Us", "Minecraft", "Fortnite", "PUBG"),
        ("Хто зіграв роль Айронмена у фільмах Marvel?", "Роберт Дауні-молодший", "Кріс Еванс", "Том Голланд", "Марк Руффало"),
        ("Який серіал зробив фразу 'Winter is coming' всесвітньо відомою?", "Гра престолів", "Відьмак", "Доктор Хто", "Ходячі мерці"),

        # Детективна пригода
        ("Хто є автором оповідань про Шерлока Голмса?", "Артур Конан Дойл", "Агата Крісті", "Джордж Орвелл", "Ієн Флемінг"),
        ("Як звали помічника Шерлока Голмса?", "Доктор Ватсон", "Інспектор Лестрейд", "Моріарті", "Пуаро"),
        ("Який відомий бельгійський детектив створений Агатою Крісті?", "Еркюль Пуаро", "Міс Марпл", "Шерлок Голмс", "Сем Спейд"),
        ("Як називається наука, що досліджує відбитки пальців?", "Дактилоскопія", "Трасологія", "Балістика", "Токсикологія"),
        ("Що зазвичай шукають детективи на місці злочину?", "Докази", "Свідків", "Підозрюваних", "Газети"),

        # Фантастичні світи
        ("Хто створив сагу 'Володар перснів'?", "Дж. Р. Р. Толкін", "Дж. К. Ролінґ", "Джордж Мартін", "Стівен Кінг"),
        ("Як називається планета, на якій відбуваються події фільму 'Аватар'?", "Пандора", "Набу", "Марс", "Криптон"),
        ("У якій франшизі можна зустріти лицарів-джедаїв?", "Зоряні війни", "Зоряний шлях", "Володар перснів", "Дюна"),
        ("Як звали головного героя 'Матриці'?", "Нео", "Морфеус", "Сміт", "Кейн"),
        ("Який чарівник носить шрам у вигляді блискавки?", "Гаррі Поттер", "Гендальф", "Мерлін", "Доктор Стрендж")
    ]
        

    cursor.executemany("""INSERT INTO questions (question,answer,wrong1,wrong2,wrong3) VALUES(?,?,?,?,?)""",questions)
    conn.commit()
    close()

def add_links():
    open()
    cursor.execute("PRAGMA foreign_keys=on")
    action = input("ДОДАТИ?(y/n)")
    
    while  action != "n":
        quiz_id = int(input("Введіть номер вікторини "))
        question_id = int(input("Введіть номер питання "))
        cursor.execute("""INSERT INTO quiz_questions(quiz_id,question_id) VALUES(?,?)""",[quiz_id,question_id])
        conn.commit()
        action = input("ДОДАТИ?(y/n)")
    close()

def open():
    global conn, cursor
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


def close():
    global conn,cursor
    cursor.close()
    conn.close()
def get_quizes():
    open()
    cursor.execute("SELECT *FROM quiz")
    quizes = cursor.fetchall()
    close()
    return quizes

def get_questions_after(quiz_id=1,question_id=0):
    open()
    cursor.execute("""SELECT questions.id, questions.question, questions.answer, questions.wrong1, questions.wrong2, questions.wrong3
                  FROM questions, quiz_questions
                  WHERE quiz_questions.quiz_id = ? AND
                  quiz_questions.question_id > ? AND
                  quiz_questions.question_id = questions.id
                  ORDER BY quiz_questions.id""", (quiz_id, question_id))

    
def create_quiz(title, description):
    open()
    cursor.execute("""INSERT INTO quiz (title, description) VALUES(?,?)""", (title, description))
    conn.commit()
    close()

def check_right_answer(question_id, selected_answer):
    open()
    cursor.execute("""SELECT answer FROM questions WHERE id = ?""", (question_id,))
    correct_answer = cursor.fetchone()[0]
    close()
    if selected_answer == correct_answer:
        return True 
    else:
        return False


                   