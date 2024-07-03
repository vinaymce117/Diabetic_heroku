from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# code business logic

@app.route('/')
def base():
    print("Hello World")
    return render_template('home.html')

@app.route('/predict', methods=['post'])
def predict():

    print("Reached here")
    #load the model
    model = joblib.load('diabatic_80.pkl')
    print("Model loded")

    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
   
   
    print(preg, plas, pres, skin, test, mass, pedi, type(age)) 

    output = model.predict([[int(preg), int(plas), int(pres), int(skin), int(test), int(mass), int(pedi), int(age)]])

    if output[0]==0:
        data = 'Person is not diabetic'
    else:
        data = 'person is diabetic'

    return render_template('predict.html', data = data)

if __name__  == "__main__":

app.run(debug=True)