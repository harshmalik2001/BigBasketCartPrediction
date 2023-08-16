from flask import Flask, render_template, request
from models.apriori_model import load_data, get_recommendations

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_product = request.form['product']
        transactions = load_data()
        recommendations = get_recommendations(transactions, input_product)

        formatted_recommendations = []
        for recommendation in recommendations:
            recommended_product = recommendation[0]
            confidence = recommendation[1] * 100
            formatted_recommendations.append((recommended_product, confidence))

        return render_template('index.html', input_product=input_product, recommendations=formatted_recommendations)

    return render_template('index.html', recommendations=None)

if __name__ == '__main__':
    app.run(debug=True)
