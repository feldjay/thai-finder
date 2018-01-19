from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

url = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD'
data = pd.read_csv(url)
acceptable_grades = ['A', 'B']


@app.route("/")
def get_restaurants():
    thai_restaurants = data.loc[data["CUISINE DESCRIPTION"] == 'Thai']
    df = thai_restaurants.loc[data["GRADE"].isin(acceptable_grades)]
    df_list = df.iloc[0:10].sort_values("SCORE").values.tolist()
    rest_names = [row[1:3] for row in df_list]
    keys = ['name', 'boro']
    rest_dict = {x: list(y) for x, y in zip(keys, zip(*rest_names))}
    import pdb; pdb.set_trace()
    rest_boros = []
    for row in rest_names:
        if row[1] not in rest_boros:
            rest_boros.append(row[1])
    return render_template('layout.html', restaurants=rest_names, boros=rest_boros)


if __name__ == "__main__":
    app.run(debug=True)
