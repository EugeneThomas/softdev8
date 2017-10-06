from flask import Flask, request, render_template, session, redirect, url_for
import os

app = Flask(__name__) #create instance of class
app.secret_key = os.urandom(32)

# Usernames and Passwords...

# For person 1... 
user1 = "Jennifer"
pass1 = "Zhang"

#For person 2... 
user2 = "Eugene"
pass2 = "Thomas"

#encrypts the values that you put in our cookie
app.secret_key = os.urandom(32)

### The Root Route:

@app.route("/", methods = ['GET', 'POST'])
def hello():
    if request.method == 'POST':
        if (request.form['pass'] == pass1 and request.form['username'] == user1) or (request.form['pass'] == pass2 and request.form['username'] == user2): #If the username-password pair matches...
            session['user'] = request.form['username'] ## Add username to the session 
            name = request.form['username']
            return redirect('/logged_in') ## redirect to the welcome page
            ## return redirect(url_for("ur_in")) has the same effect. 
    return render_template('landing.html') # If the username/password don't match, redirect to the landing page. 

### The logged in page:

@app.route('/logged_in')
def ur_in():
    return render_template('two.html') ## Render to the welcome page. 

### After logging out:

@app.route('/logout')
def logout():
    session.pop('user',None) ## Remove user from the session
    return redirect("/") 

if __name__=="__main__":
    app.debug = True
    app.run()
