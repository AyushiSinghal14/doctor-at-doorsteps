import numpy as np
from flask import Flask,request,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('models/model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():
    int_features=[int(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=model.predict(features)
    result=prediction[0]
    
    return render_template('index.html',prediction=result)

@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in requestAnimationFrame.form.values()]
    features=[np.array(int_features)]
    prediction=model.predict(features)
    result=prediction[0]

    return render_template('results.html',prediction=result)

if __name__=="__main__":
    app.run(debug=True)     






