from flask import Flask,render_template,request,redirect
from fun import*

app=Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    print("test get")
    if request.method=="POST":
        print("test post")
        print(request.form["user"],request.form["password"])
    return render_template("login.html")
@app.route("/registration", methods=["POST","GET"])
def registration():
    if request.method=="POST":
        register(request.form['name'],request.form['age'],request.form['course'],request.form['address'])
       
        
    data=read_json()    
    return render_template("register.html",stud_data=data)
@app.route("/delete/<id>")
def delete_stud(id):
    delete(id)
    return redirect("/registration")
@app.route("/update/<id>",methods=["POST","GET"])
def update_stud(id):
    
    if request.method=="POST":
        update(id,request.form['name'],request.form['age'],request.form['course'],request.form['address'])
        
    
    return redirect("/registration")
    





if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")