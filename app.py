from flask import Flask, render_template, request,url_for, flash
from pickle import load


app=Flask(__name__)
app.secret_key= "mykey"
model = load(open('svm_classifier_mdl.pkl','rb'))

# the route can be either requested with a '/' or '/Equity-Predictions'
@app.route("/fake-news", methods=["POST","GET"])
@app.route("/", methods=["POST","GET"])
def fake():
    if request.method=='POST':
        try:
            msg=request.form.get("title")
            if len(msg) < 3:
                flash('Please enter title of news')
                return render_template('fake_news_detection.html')
            else:
                predict=model.predict([msg])
                return render_template('fake_news_detection.html', prediction=predict, message=msg)
        except:
            flash('Please enter title of news')
    
    return render_template('fake_news_detection.html')

if __name__=="__main__":
    app.run(debug=True)