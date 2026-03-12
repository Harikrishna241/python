from flask import Flask,render_template
import pandas as pd



app = Flask("__name__")

@app.route("/home")
def home():
    return render_template("tutorial.html")
@app.route("/api/v1/<station>/<date>")
def about(station,date):
    filename="/Users/macos/Downloads/data_small/TG_STAID"+str(station).zfill(6)+".txt"
    df = pd.read_csv(filename,skiprows=20)
    temperature=df.loc[df["Date"]==date]['TG'].squeeze()/10
    print("temp",temperature)

    return {"station": station,
            "date": date,
            "temperature": temperature
    }
if __name__=='__main__':
    app.run(debug=True,port=5001)
