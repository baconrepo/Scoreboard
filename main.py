from flask import Flask, request, flash, url_for, redirect, render_template
#import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy
#from forms import ScoreForm
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///scores.db'
db=SQLAlchemy(app)
#db.Model.metadata.reflect(db.enginge)
class Scores(db.Model):
    __tablename__='scores'
    id=db.Column(db.Integer,primary_key=True)
    #title=db.Column(db.String)
    name=db.Column(db.String)
    score=db.Column(db.String)
def __init__(self,name,score):
    self.name=name
    self.score=score

@app.route('/') ##pinned to /
def home():
    return render_template('home.html')  ##submit score/view leaderboard

@app.route('/submit', methods=['GET','POST']) ##score submission page
def submit_score():
    #form=ScoreForm(request.form)
    if request_method=='POST':
        score=scores(request.form['name'],request.form['score'])
        db.session.add(score)
        db.session.commit()
        flash('Score saved successfully')
        return redirect('leaderboard')
    return render_template('submitscore.html')

@app.route('/leaderboard')
def leaderboard():
    con=sql.connect("scores.db")
    con.row_factory=sql.Row

    cur=con.cursor()
    cur.execute("select * from scores")
    #rows=cur.sort(fetchall())  ##may not work
    rows=cur.fetchall()
    return render_template("leaderboard.html",scores=scores.query.all())



"""
@app.route('/addrec',methods=['POST','GET'])
    def addrec():
        if request.method=='POST':
            try:
                name=request.form['name']
                score=request.form['score']

                with sql.connect("scores.db") as con:
                    cur=con.cursor()
                    cur.execute("INSERT INTO scores (name,score) VALUES (?,?)",(name,score))

                    con.commit()
                    msg= "Score successfully submitted"
            except:
                con.rollback()
                msg="Submission Error"
            finally:
                return render_template("leaderboard.html",msg=msg)
                con.close()
"""



if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
