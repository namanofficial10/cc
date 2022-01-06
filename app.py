from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/user_log_in", methods=['GET', 'POST'])
def user_log_in():
    if request.method=="POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print(email, password)

        if email == "user@user" and password=="user":
            return redirect("success?type=user")
        else:
            return render_template("user_log_in.html", visibi="")

    else:
        return render_template("user_log_in.html", visibi="none")

@app.route("/admin_log_in", methods=['GET', 'POST'])
def admin_log_in():
    if request.method=="POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print(email, password)

        if email == "admin@admin" and password=="admin":
            return redirect("success?type=admin")
        else:
            return render_template("admin_log_in.html", visibi="")

    else:
        return render_template("admin_log_in.html", visibi="none")

@app.route("/success", methods=['GET', 'POST'])
def success():
    if request.method=="GET":
        user_type = request.args['type']
        
    if user_type:
        return render_template("success_login.html",who=user_type)
    else:
        return render_template("success_login.html",who="cc")

@app.route("/user_log_in")
def contractor_log_in():
    return render_template("contractor_log_in.html")

    
if __name__ == "__main__":
    app.run(debug=True,port=5001)
