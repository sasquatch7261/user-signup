from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def welcome_form():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    email = request.form["email"]

    if len(username) < 3 or len(username) > 20:
        error = "That's not a valid username"
        return redirect("/?error=" + error)
    elif len(username) >= 3 or len(username) <= 20:
        error = "That's not a valid username"
        for char in username:
            if char == " ":
                return redirect("/?error=" + error)

    if len(password1) < 3 or len(password1) > 20:
        error1 = "That's not a valid password"
        return redirect("/?error=" + error1)
    elif len(password1) >= 3 or len(password1) <= 20:
        error1 = "That's not a valid password"
        for char in password1:
            if char == " ":
                return redirect("/?error=" + error1)

    if password2 != password1:
        error2 = "Passwords don't match"
        return redirect("/?error=" + error2)

    
    if len(email) <= 3 or len(email) >= 20:
        error3 = "That's not a valid email"
        return redirect("/?error=" + error3)
    elif "." not in email:
        error3 = "That's not a valid email"
        return redirect("/?error=" + error3)
    elif "@" not in email:
        error3 = "That's not a valid email"
        return redirect("/?error=" + error3)
        
    return render_template('welcome-form.html', username=username)

@app.route("/")
def login():
    username_error = request.args.get("error")
    password1_error = request.args.get("error")
    password2_error = request.args.get("error")
    email_error = request.args.get("error")
    if username_error == "That's not a valid username":
        return render_template('login-form.html', error=username_error, error1=password1_error, error2=password2_error, error3=email_error)
    elif password1_error == "That's not a valid password":
        return render_template('login-form.html', error1=password1_error)
    elif password2_error == "Passwords don't match":
        return render_template('login-form.html', error2=password2_error)
    elif email_error == "That's not a valid email":
        return render_template('login-form.html', error3=email_error)

    return render_template('login-form.html')
    

app.run()