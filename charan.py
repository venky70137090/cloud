from flask import Flask
app=Flask(__name__)
@app.route("/")
def sam():
    return "hello venky"
if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=7000)