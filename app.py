from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__, static_folder='static')

inp_arr = {'algo':".", 'class':".", 'file':"."}

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        inp_arr['algo'] = request.form.get('algo')
        inp_arr['file'] = request.form.get('file')
        inp_arr['class'] = request.form.get('class')
        return (redirect(url_for('result')))
    else:
        return render_template('home.html')

@app.route("/result", methods = ['GET', 'POST'])
def result():
    if request.method == 'GET':
        return("<h1>" + " Results : " +"</h1>"+ "<br> file : " + inp_arr["file"]+'<br> algo: '+inp_arr["algo"] + '<br> class: '+ inp_arr["class"])

if __name__ == '__main__':
    app.run(port=8000, debug=True)