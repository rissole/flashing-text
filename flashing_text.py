from flask import *
#based64
import base64 as based64
app = Flask(__name__)

@app.route('/')
def main(): 
    return render_template("index.htm")

@app.route('/e/<base64_string>')
def show(base64_string):
    string = based64.urlsafe_b64decode(base64_string)
    return render_template("display.htm", string=string)

@app.route('/<gag>')
def show_gag(gag):
    #buuuut render_template can deal with unicode just fine.
    return render_template("display.htm", string=gag)

@app.errorhandler(404)
def custom404(e):
    #security=True
    return render_template("display.htm", safe=True, string="404 <br/>PAGE NOT FOUND"), 404

#LEGACY CODE BELOW, NOT CHANGED SINCE FREELANCER KARMABOARD DAYS
if __name__ == '__main__':
    app.run(host='0.0.0.0') 
