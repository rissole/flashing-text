from flask import *
#based64
import base64 as based64
app = Flask(__name__)


@app.route('/')
def main(): 
    return render_template("main.html")

@app.route('/e/<base64_string>')
def show(base64_string):
    string = based64.urlsafe_b64decode(base64_string)
    return render_template("display.html", string=string)

@app.route('/<gag>')
def show_gag(gag):
    return render_template("display.html", string=gag)

@app.errorhandler(404)
def custom404(e):
    return render_template("404.html"), 404

#LEGACY CODE BELOW, NOT CHANGED SINCE FREELANCER KARMABOARD DAYS
if __name__ == '__main__':
    app.debug = True    #Not legit for production or Blake.
    app.run(host='0.0.0.0') 
