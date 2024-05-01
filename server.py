from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the machine learning model from the pickle file
with open('/Users/shiva/Developer/Data Science/placement_Review/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get CGPA and IQ scores from the form
    cgpa = float(request.form['cgpa'])
    iq = float(request.form['iq'])

    # Make predictions using the loaded model
    prediction = model.predict([[cgpa, iq]])[0]

    # Convert prediction to 'Yes' or 'No'
    placement = 'Yes' if prediction == 1 else 'No'

    return render_template('result.html', placement=placement)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
