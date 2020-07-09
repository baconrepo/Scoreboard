from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/submitscore')
def new_student():
   return render_template('submitscore.html')

@app.route('/addrec',methods = ['POST','GET'])
def addrec():
  # if request.method == 'GET':
    #  try:
         name = request.form['name']
         score = request.form['score']



         with sql.connect("/var/www/ScorecardResearch/db/scores.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO scores (name,score) VALUES (?,?)",(name,score))

            con.commit()
            msg = "Record successfully added"
     # except:
    #     con.rollback()
    #     msg = "error in insert operation"

     # finally:
         #return render_template("results.html",msg = msg)
         con.close()
         con = sql.connect("/var/www/ScorecardResearch/db/scores.db")
         con.row_factory = sql.Row

         cur = con.cursor()
         cur.execute("select * from scores ORDER BY Score DESC")

         rows = cur.fetchall();
         return render_template("leaderboard.html",rows=rows)

         #return render_template("leaderboard.html")
         #con.close()
@app.route('/leaderboard')
def list():
   con = sql.connect("/var/www/ScorecardResearch/db/scores.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from scores ORDER BY Score DESC")

   rows = cur.fetchall();
   return render_template("leaderboard.html",rows=rows)

if __name__ == '__main__':
   app.run(host='192.168.1.16')
   #app.run(debug=True)
