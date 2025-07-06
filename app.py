from flask import Flask, render_template, request

app = Flask(__name__)

def predict_total_points(home_scored_avg, home_allowed_avg, away_scored_avg, away_allowed_avg):
    home_expected = (home_scored_avg + away_allowed_avg) / 2
    away_expected = (away_scored_avg + home_allowed_avg) / 2
    total_points = home_expected + away_expected
    return round(total_points, 1)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            home_scored = float(request.form['home_scored'])
            home_allowed = float(request.form['home_allowed'])
            away_scored = float(request.form['away_scored'])
            away_allowed = float(request.form['away_allowed'])
            prediction = predict_total_points(home_scored, home_allowed, away_scored, away_allowed)
        except ValueError:
            prediction = "Invalid input"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
