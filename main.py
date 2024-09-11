from flask import Flask, render_template

app = Flask(__name__)

# Головна сторінка
@app.route('/')
def index():
    return render_template('index.html')

# Сторінка з меню
@app.route('/menu')
def menu():
    pizzas = [
        {"name": "Маргарита", "ingredients": "Сир Моцарела, соус, базилік", "price": "120 UAH"},
        {"name": "Пепероні", "ingredients": "Сир Моцарела, пепероні, соус", "price": "150 UAH"},
        {"name": "Гавайська", "ingredients": "Курка, ананас, сир, соус", "price": "140 UAH"}
    ]
    return render_template('menu.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)
