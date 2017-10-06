from flask import Flask, request, render_template, session, redirect, url_for
import os

app = Flask(__name__) #create instance of class
app.secret_key = os.urandom(32)

### The Root Route:

@app.route("/") 
def hello():

if __name__=="__main__":
    app.debug = True
    app.run()
