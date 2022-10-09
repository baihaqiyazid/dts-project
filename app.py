from flask import Flask, render_template, url_for, request
import pickle

app = Flask(__name__)

def predict(features):
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    return pickled_model.predict([features]).round()
    
@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        speedAvg = request.form['speedAvg']
        speedStd = request.form['speedStd']
        secondZoneAvg = request.form['secondZoneAvg']
        secondZoneStd = request.form['secondZoneStd']

        features = [speedAvg, speedStd, secondZoneAvg, secondZoneStd]

        volume = int(predict(features))
        return render_template('Result.html', 
                                speedAvg=speedAvg,
                                speedStd=speedStd,
                                secondZoneAvg=secondZoneAvg,
                                secondZoneStd=secondZoneStd,
                                volume=volume)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)