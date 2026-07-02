from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/claims")
def claims():

    df = pd.read_csv("data/claims.csv")

    return df.to_html(index=False)

app.run(debug=True)