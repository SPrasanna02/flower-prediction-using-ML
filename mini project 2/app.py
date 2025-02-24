from flask import Flask,render_template, url_for
app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("index.html")


@app.route("/admin") 
def admin():
    return "<h1>welcome admin!</h1>"

@app.route("/guest") 
def guest():
    return "<h1>welcome guest!</h1>"

@app.route("/mypage/<name>")
def mypage(name):
    return "<h1>hey %s welcome to my website</h1>" % name


if __name__=="__main__":
    app.run(debug=True)
