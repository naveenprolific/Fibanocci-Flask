from flask import Flask,render_template,request,url_for
app = Flask(__name__)


@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        r = request.form["number"]
        l = ["0","1"]
        for i in range(int(r)-2):
            l.append(str(int(l[-1])+int(l[-2])))
        l = ",\t\t".join(map(str,l))
        return render_template('home.html',ls=l)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)