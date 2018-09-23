from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

rotate_form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action = "/rotate" method="post">
            <label> Rotate by 
                <input type = "text" name="rot" value="0"/>
            </label>
            <textarea type = "text" name= "text">{0}</textarea> 
            <input type ="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/rotate", methods = ['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    new_text = rotate_string(text, rot)
    return "<h1>" + rotate_form.format(new_text)+ "</h1>"

@app.route("/")
def index():
    empty_string=""
    return rotate_form.format(empty_string)

app.run()