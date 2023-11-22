from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route('/')
def random_number():
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)
    sum_result = number1 + number2
    product_result = number1 * number2

    return render_template('index.html', number1=number1, number2=number2, sum_result=sum_result, product_result=product_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
