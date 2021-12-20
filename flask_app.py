# Importing required packages
from flask import Flask, render_template, request
from search import search_online

# create flask app
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def scrappers():
    if request.method == 'POST':
        # Get search string entered by user
        searchString = request.form['content'].replace(" ", "")

        # search for string online
        reviews = search_online(searchString)

        # showing the review to the user
        return render_template("results.html", reviews=reviews)
    else:
        return render_template("index.html", index=True)


# running the app on the local machine on port 9000
if __name__ == "__main__":
    app.run(port=8000, debug=False)
