from flask import Flask, render_template, redirect, request, url_for
import pandas as pd
import algoPred as ap

app = Flask(__name__, static_folder='static')

inp_arr = {'algo':".", 'class':".", 'file':"."}

index_for_classes = pd.read_csv("./index_for_classes.csv")
data = pd.read_csv("./dataset.csv", names = ['path', 'class'])

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        inp_arr['algo'] = request.form.get('algo')
        
        f = request.files['file']
        x = f
        
        path = "./static/A.jpg"
        
        f.save(path)
        # x.save("./static/user.jpg")
        
        end = 0
        start = 0
        inp_arr['class'] = request.form.get('class')
        ui_class = inp_arr['class']
        
        for i in range(len(index_for_classes['class'])):
            if(ui_class == index_for_classes['class'][i]):
                start = index_for_classes['id'][i]
                end = index_for_classes['id'][i+1]
                if start == end == 0:
                    return ("<h1>Class name error</h1>")
        global arr
        if inp_arr['algo'] == "Jaccard":
            arr = ap.pred_jaccard("./static/A.jpg", data, start, end)
        elif inp_arr['algo'] == "SSIM":
            arr = ap.pred_ssim("./static/A.jpg", data, start, end)
        return (redirect(url_for('result')))
    
    else:
        return render_template('home.html')

@app.route("/res", methods = ['GET', 'POST'])
def result():
    if request.method == 'GET':
        
        return(render_template("results.html", array=arr, inps = inp_arr))

if __name__ == '__main__':
    app.run(port=8000, debug=True)