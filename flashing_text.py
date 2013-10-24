from flask import *
#based64
import base64 as based64
app = Flask(__name__)

@app.route('/')
def main(): 
    return render_template("main.htm")

@app.route('/e/<base64_string>')
def show(base64_string):
    #Turns out the type of this string is "unicode" and the based64 module wants "str".
    string = based64.urlsafe_b64decode(str(base64_string)) #nailed it
    return render_template("display.htm", string=string)

@app.route('/<gag>')
def show_gag(gag):
    #buuuut render_template can deal with unicode just fine.
    return render_template("display.htm", string=gag)

@app.errorhandler(404)
def custom404(e):
    return render_template("display.htm", string="[404 PAGE NOT FOUND]"), 404

#LEGACY CODE BELOW, NOT CHANGED SINCE FREELANCER KARMABOARD DAYS
if __name__ == '__main__':
    app.debug = True    #Not legit for production or Blake.
    app.run(host='0.0.0.0') 
