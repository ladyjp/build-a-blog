from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:launchcode@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'randomish8key'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blogtitle = db.Column(db.String(200))
    body = db.Column(db.Text)
    

    def __init__(self, blogtitle, body):
        self.blogtitle = blogtitle
        self.body = body


@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def index():
    return render_template('index.html')
       
@app.route('/blog')
def blog():
    blogs = Blog.query.all()
    return render_template('blog.html', blogs=blogs)

@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    return render_template('newpost.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    blogtitle = request.form['blogtitle']
    body = request.form['body']
    
    title_error = ''
    body_error = ''
    
    if blogtitle == "":
        title_error = 'Enter blog title'
   
    if body == "":
        body_error = 'Enter blog post'
    
    if not title_error and not body_error:
        new_blog = Blog(blogtitle=blogtitle, body=body)

        db.session.add(new_blog)
        db.session.commit()
        
        return redirect('/blog')
    
    else:
        return render_template('newpost.html', title_error=title_error, 
        body_error=body_error)

  


@app.route('/single')
def single():
    blog_id = request.args.get('id') 
    blogid = Blog.query.filter_by(id=blog_id).first()
    
    return render_template('single.html', b=blogid)

if __name__ == '__main__':
    app.run()




