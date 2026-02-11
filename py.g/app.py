from flask import Flask, render_template, request
import requests
#search for cocktail by name: https://www.thecocktaildb.com/api/json/v1/1/search.php?s=
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        req = request.form.get('search')
        data = requests.get(
            f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={req}'
        ).json()

        drinks = data.get("drinks", [])

        if not drinks:
            return render_template("results.html", cocktails=None)

        print(drinks[0]["strDrink"])

        return render_template("results.html", drinks=drinks)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
