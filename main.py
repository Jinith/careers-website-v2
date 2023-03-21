from flask import Flask, render_template,jsonify
app = Flask(__name__)

JOBS=[
{
  'id':1,
  'title':'Data Analyst',
  'location': ' Melbourne, Australia',
  'salary':'$100,000'
},
  {
  'id':2,
  'title':'Data Scientist',
  'location':' Sydney,Australia',
  'salary':' $150,000'},
  {
  'id':3,
  'title':' Frontend engineer',
  'location': ' Remote',
  },
  {
  'id':4,
  'title':' Backend Engineer',
  'location': ' Bengaluru,India',
  'salary':' Rs.150,000'}
  
]

@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS) 

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)



  