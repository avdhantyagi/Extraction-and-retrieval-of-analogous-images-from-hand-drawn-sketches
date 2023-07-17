from flask import Flask, render_template, redirect, request, url_for
import pandas as pd

app = Flask(__name__, static_folder='static')

inp_arr = {'algo':".", 'class':".", 'file':"."}

index_for_classes = pd.read_csv("./index_for_classes.csv")
end = 0
start = 0

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        inp_arr['algo'] = request.form.get('algo')
        
        f = request.files['file']
        
        path = "./A.jpg"
        
        f.save(path)
        
        inp_arr['class'] = request.form.get('class')
        ui_class = inp_arr['class']
        
        for i in range(len(index_for_classes['class'])):
            if(ui_class == index_for_classes['class'][i]):
                start = index_for_classes['id'][i]
                end = index_for_classes['id'][i+1]
        return (redirect(url_for('result')))
    
    else:
        return render_template('home.html')

@app.route("/result", methods = ['GET', 'POST'])
def result():
    if request.method == 'GET':
        
        return("<h1>" + " Results : " + inp_arr["file"]+'<br> algo: '+inp_arr["algo"] + '<br> class: '+ inp_arr["class"])

if __name__ == '__main__':
    app.run(port=8000, debug=True)