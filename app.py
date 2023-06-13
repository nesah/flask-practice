from flask import Flask, render_template

# 1 - create flask app
app = Flask(__name__)

# 2 - create route / this will stand as the url-extension (?)
@app.route("/")
# 3 - define the function under "/"
def homePage():
    return render_template('index.html')

# para automatic mag run w/o 'flask run'
if __name__ == '__main__':

    #this is only local host
    app.run(host="0.0.0.0", debug=True)

