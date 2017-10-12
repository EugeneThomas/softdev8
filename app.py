from flask import Flask, request, render_template, session, redirect, url_for, flash
import os

app = Flask(__name__) #create instance of class
app.secret_key = os.urandom(32)

# Usernames and Passwords...

# CREDITS TO TMOI AND SLAU FOR THIS IDEA:

ACCOUNTS = {"Eugene": "Thomas", "Jennifer": "Zhang"} 

### The Root Route:

@app.route('/')
def hello():
    if 'user' in session.keys(): # If there is a session... 
        return render_template('two.html', name = session['user']) # Direct to the logged in page
    else: # IF NOT...
        return render_template('landing.html') # Log in 
        

### Authenticate Method
    
def aut(u, p):
    if (u in ACCOUNTS):
        if p == ACCOUNTS[u]:
            return 0 #All correct
        else:
            return 1 #Wrong Password
    else:
        return -1 #Wrong Username 
    
@app.route('/login', methods=["GET", "POST"])
def login():
    if 'user' not in session: 
        if aut(request.form['user'], request.form['pass']) == 0:
            session['user'] = request.form['user'] # Add user to the session. 
            print session.keys()
            flash('Logged Out') # For when you log out later in the session. 
            return render_template('two.html', name = session['user']) 
        elif aut(request.form['user'], request.form['pass']) == 1:
            flash('Wrong password') 
            return render_template('landing.html') 
        else:
            flash('Wrong Username') 
            return render_template('landing.html')
    else:
        return render_template('two.html', name = session['user'])
        

    

### After logging out:

@app.route('/logout')
def logout():
    if 'user' in session.keys(): 
        session.pop('user',None) ## Remove user from the session
    return redirect("/") 

if __name__=="__main__":
    app.debug = True
    app.run()
