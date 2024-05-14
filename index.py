from flask import Flask, request, render_template, url_for
from math import ceil

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/calc")
def calc_page():
    return render_template("calc.html")

@app.route("/result", methods=['GET','POST'])
def result():
    if request.method == "POST":
        credit = int(request.form["_summ"])
        first_pay = int(request.form["_first_pay"])
        years = int(request.form["_years"])

    rule = ceil(credit * 0.2)
    maxi = ceil(credit * 0.7)
    note = ''
    color = "alert-success"

    if(maxi >= first_pay >= rule):
        note = 'Расчет проведен верно'
        percent = 0.0075
        k = (percent * (1 + percent) ** (years * 12)) / ((1 + percent) ** (years * 12) - 1)
        monthly_payment = ceil((credit - first_pay) * k) - 10000

        timeline = years
        summa = credit
        payment_f = first_pay

        return render_template("calc.html", result=monthly_payment, note=note, color=color, timeline=timeline, summa=summa, payment_f=payment_f)

    if(first_pay >=  maxi):
        note = ('Первоначальный платеж должен быть\nне БОЛЕЕ ') + str(maxi) + ' рублей'
        color = "alert-danger"

        timeline = years
        summa = credit
        payment_f = first_pay

        return render_template("calc.html", result='Неверные данные', note=note, color=color, timeline=timeline,
                               summa=summa, payment_f=payment_f)

    else:
        note = ('Первоначальный платеж должен быть\nне МЕНЕЕ ')+str(rule)+' рублей'
        color = "alert-warning"

        timeline = years
        summa = credit
        payment_f = first_pay

        return render_template("calc.html", result='Неверные данные', note=note, color=color, timeline=timeline, summa=summa, payment_f=payment_f)




if __name__ == "__main__":
    app.run(debug=True)
