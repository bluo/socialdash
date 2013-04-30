import os
import facebook
from flask import Flask, render_template, send_from_directory

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)

app.config.update(
    DEBUG = True,
)

#----------------------------------------
# controllers
#----------------------------------------

@app.errorhandler(404)
def printtest():
    token = 'BAACEdEose0cBAPP3MdyQ3LYNvv4spBtnwxXxu9y9HRZAvmX8rzPquvD2oZBba8cMYKB753ZA4ON4zsJFKlY1ZCwKbzMZCe3Q5FwM3TSyWbZASqw4ZAChhGLKUDfDIbYZCce3acEU39OsfZAp0gUdzox53eleBgYbOuyvc16NuVGNjRHK6oWwQ7hbwqd3LGISAzQhkqYKQBz3BDGWjO0eFwokdKyufQZCjUsXIZD'

    graph = facebook.GraphAPI(token)
    profile = graph.get_object("me")
    #friends = graph.get_connections("me", "friends")
    
    #friend_list = [friend['name'] for friend in friends['data']]
    
    #print friend_list
    
    g_profile = graph.get_object("grainger")
    num_likes = g_profile['likes']
    
    return num_likes

def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html', title=printtest())

@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)