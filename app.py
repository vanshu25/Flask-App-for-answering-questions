from flask import Flask, render_template, request

import joblib
cdqa_pipeline= joblib.load('./models/bert_qa_custom.joblib')

app = Flask(__name__)


@app.route('/')
def man():
    return render_template('home.html')

@app.route('/Answer', methods=['POST'])
def home():
    data1 = request.form['a']
    pred = cdqa_pipeline.predict(data1,3)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)