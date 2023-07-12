from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__, static_folder='static')

inp_arr = [0,0]

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        inp_arr[0] = request.form.get('algo')
        inp_arr[1] = request.form.get('file')
        print('Hello '+inp_arr[1]+' with algo: '+inp_arr[0])
        return (redirect(url_for('result')))
    else:
        return render_template('home.html')

@app.route("/result", methods = ['GET', 'POST'])
def result():
    if request.method == 'GET':
        return("<h1> Results = " + inp_arr[0] + "</h1>")

if __name__ == '__main__':
    app.run(port=8000, debug=True)