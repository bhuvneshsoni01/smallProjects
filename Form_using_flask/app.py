from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class s_list(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    s_name = db.Column(db.String(200), nullable=False)
    s_college = db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return 'Task %r' % self.id


@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        s_name = request.form['s_name']
        s_college = request.form['s_college']
        new_s = s_list(s_name=s_name, s_college=s_college)
        try:
            db.session.add(new_s)
            db.session.commit()
            return redirect('/')
        except:
            return "Their is an error in uploading!"
        # return "HELLO"
    else:
        students = s_list.query.order_by(s_list.s_name).all()
        return render_template('index.html', students=students)
    # return "Hello world!"
    # return render_template('index.html')

def mmain():
    with app.app_context():
       db.create_all()

if __name__ == '__main__':
    # mmain()
    app.run(debug=True)