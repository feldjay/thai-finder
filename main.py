import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd


app = Flask(__name__)
engine = create_engine('sqlite:///foo.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foo.db'
db = SQLAlchemy(app)

#url = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD'
url = 'restaurants.csv'
data = pd.read_csv(url)
acceptable_grades = ['A', 'B']
thai_restaurants = data.loc[data["CUISINE DESCRIPTION"] == 'Thai']
df = thai_restaurants.loc[data["GRADE"].isin(acceptable_grades)]
df.to_sql(con=engine, name='restaurant', if_exists='append')


@app.route("/")
def get_restaurants():
    rest_q = engine.execute('SELECT * FROM restaurant ORDER BY SCORE asc limit 10').fetchall()
    data_dict = {}
    for rest in rest_q:
        if rest['BORO'] in data_dict:
            data_dict[rest['BORO']].append(rest['DBA'])
        else:
            data_dict[rest['BORO']] = [rest['DBA']]
    return render_template('layout.html', data=data_dict)


if __name__ == "__main__":
    app.run(debug=True)
