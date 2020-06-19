from flask import Flask,request,redirect,url_for,render_template
# import investpy
import re
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ticker/',methods=["GET", "POST"])
def result():
    if request.method == 'POST':
        result = request.form['result']
        res = re.sub(r'\..*',"",result)
        print(res)
        # df = investpy.moving_averages(name=res, country='india', product_type='stock', interval='daily')
        # print(df.head())
        return redirect(url_for('display',r = result))

@app.route('/ticker/<string:r>') 
def display(r):
    url_result = str(r)
    return render_template('result.html', result = url_result)
     
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
        