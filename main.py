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
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('blog.html', title="A Black Woman's Blog")

       
@app.route('/blog')
def blog():
    blogtitle = request.form['blogtitle']
    body = request.form['body']
   
    return render_template('blog.html', blogtitle=blogtitle, body=body)

@app.route('/newpost',methods=['POST', 'GET'])
def newpost():
    if request.method == 'POST':
        blogtitle = request.form['blogtitle']
        body = request.form['body']
        new_blog = Blog(title_post, blog_post)
        db.session.add(new_blog)
        db.session.commit()

    else:
        return render_template('newpost.html')


@app.route('/addpost', methods=['POST'])
def addpost():
    blogtitle = request.form['blogtitle']
    body = request.form['body']
    return '<h1>Title: {} Blog: {} </h1>'.format(blogtitle, body)
    
#@app.route('/', methods=['POST'])
#def blog_page():
   



if __name__ == '__main__':
    app.run()

#@app.route('/', methods=['POST'])
#def view_post():
   # title_post = request.form['title']
    #blog_post = request.form['blog']
    #return title_post

    #blogs = Blog.query.filter_by(completed=False).all()
    #completed_blogs = Blog.query.filter_by(completed=True).all()
    #return render_template('blog.html',title="Black Woman Blog!", 
       # blogs=blogs, completed_blogs=completed_blogs)

#@app.route('/blog', methods=['POST'])
#def blog():






#@app.route('/delete-post', methods=['POST'])
#def delete_post():

    #task_id = int(request.form['task-id'])
    #task = Task.query.get(task_id)
    #task.completed = True
    #db.session.add(task)
    #db.session.commit()

   # return redirect('/')


