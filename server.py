from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "lmao"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def capture_info():
    session['username'] = request.form['name']
    session['userlocale'] = request.form['dojo_location']
    session['favelang'] = request.form['favorite_language']
    session['usercomment'] = request.form['comment']
    return render_template("result.html", username = session['username'], userlocale = session['userlocale'], favelang = session['favelang'], usercomment = session['usercomment'])
    
@app.route('/goback', methods=['POST'])
def go_back():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

