# We will be using Flask app.
from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
# Here we have to create Flask app and __name__ 
application = Flask(__name__)
app = application

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

# Create template folder 

#Inside this predict_datapoint , we will be doing everything like getting our data and probably doing the prediction .
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        # When we do the post this request will have the entire information .
            
        # Then convert entire information into dataframe .
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])

# What will be there in the home.html . The simple input ddta fields that we really need to provide to our model to do the prediction . That is there in home.html .

if __name__=="__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)

