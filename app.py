from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String(500),nullable=False)

    def __repr__(self) -> str:
        return f"{self.id} - {self.task}"
    
@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        task = request.form["task"]
        todo = Todo(task=task)
        db.session.add(todo)
        db.session.commit()
    alltodo = Todo.query.all()
    return render_template("index.html",alltodo=alltodo)
@app.route("/Delete/<int:id>")
def delete(id):
    task = Todo.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect("/")
if __name__=="__main__":
    app.run(debug=True)