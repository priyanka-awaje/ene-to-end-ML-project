from flask import Flask,render_template,request
import pickle
import sklearn
import numpy as np

app=Flask(__name__)
model=pickle.load(open("rf_model.pkl","rb"))

@app.route("/")
def home_func():
    return render_template("home.html")


@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        year=int(request.form['year'])
        year=2022-year
        present_price=float(request.form['price'])
        km_driven=int(request.form['km_driven'])
        owner=int(request.form['owner'])
        fuel_type_petrol=request.form['fuel_type']
        if(fuel_type_petrol=='Petrol'):
            fuel_type_petrol=1
            fuel_type_disel=0
        else:
            fuel_type_petrol=1
            fuel_type_disel=0
        seller_type_individual=request.form['seller_type']
        if seller_type_individual=='Individual':
            seller_type_individual=1
        else:
            seller_type_individual=0
        transmission_mannual=request.form['transmission_type']
        if transmission_mannual=='manual':
            transmission_mannual=1
        else:
            transmission_mannual=0

        prediction=model.predict([[present_price,km_driven,owner,year,fuel_type_disel,fuel_type_petrol,seller_type_individual,
        transmission_mannual]])
        output=round(prediction[0],2)

        if output<0:
            return render_template("home.html",prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template("home.html",prediction_text="You can Sell the car at {}".format(output))
    else:
        return render_template("home.html")





if __name__=="__main__":
    app.run(debug=True)