from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
# from requests import request
from better_hack1 import classify


app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
def home():

    return render_template("home.html")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    print(request.files)
    if 'the_image' not in request.files:
        return 'oh no'
    the_image = request.files['the_image']
    the_image.save('./the_image.png')
    return classify()
    # return 'all done' # "recived: {}".format(request.form)


if __name__ == "__main__":
    app.run(debug = True)
    
    
    
