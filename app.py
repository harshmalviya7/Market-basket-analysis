from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=r'sqlite:///C:\Users\DELL\Desktop\robotronix\grocery\foo.db'
db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
	ante=[['cereals'], ['extra dark chocolate'], ['shrimp'], ['tomatoes'], ['grated cheese'], ['herb & pepper'], ['olive oil'], ['pepper'], ['salmon'], ['spaghetti'], ['ground beef'], ['soup'], ['whole wheat pasta'], ['pepper'], ['red wine'], ['tomato sauce'], ['burgers', 'chocolate'], ['burgers', 'french fries'], ['mineral water', 'burgers'], ['burgers', 'spaghetti'], ['burgers', 'milk'], ['cake', 'milk'], ['mineral water', 'chicken'], ['chocolate', 'chicken'], ['mineral water', 'chicken'], ['eggs', 'chocolate'], ['eggs', 'chocolate'], ['mineral water', 'escalope'], ['chocolate', 'frozen vegetables'], ['chocolate', 'ground beef'], ['frozen vegetables', 'ground beef'], ['chocolate', 'frozen vegetables'], ['chocolate', 'milk'], ['frozen vegetables', 'milk'], ['chocolate', 'spaghetti'], ['chocolate', 'ground beef'], ['mineral water', 'chocolate'], ['chocolate', 'spaghetti'], ['chocolate', 'ground beef'], ['mineral water', 'chocolate'], ['chocolate', 'spaghetti'], ['chocolate', 'olive oil'], ['soup', 'chocolate'], ['olive oil', 'chocolate'], ['chocolate', 'shrimp'], ['eggs', 'cooking oil'], ['mineral water', 'cooking oil'], ['spaghetti', 'cooking oil'], ['eggs', 'frozen vegetables'], ['eggs', 'milk'], ['eggs', 'ground beef'], ['mineral water', 'eggs'], ['eggs', 'ground beef'], ['eggs', 'spaghetti'], ['eggs', 'ground beef'], ['eggs', 'olive oil'], ['frozen vegetables', 'french fries'], ['french fries', 'milk'], ['spaghetti', 'french fries'], ['ground beef', 'french fries'], ['mineral water', 'french fries'], ['spaghetti', 'french fries'], ['mineral water', 'frozen smoothie'], ['spaghetti', 'frozen smoothie'], ['frozen smoothie', 'milk'], ['frozen vegetables', 'ground beef'], ['frozen vegetables', 'milk'], ['ground beef', 'milk'], ['mineral water', 'frozen vegetables'], ['mineral water', 'ground beef'], ['frozen vegetables', 'ground beef'], ['frozen vegetables', 'spaghetti'], ['frozen vegetables', 'ground beef'], ['spaghetti', 'ground beef'], ['mineral water', 'frozen vegetables'], ['mineral water', 'milk'], ['frozen vegetables', 'spaghetti'], ['frozen vegetables', 'milk'], ['spaghetti', 'milk'], ['mineral water', 'olive oil'], ['olive oil', 'frozen vegetables'], ['mineral water', 'shrimp'], ['mineral water', 'spaghetti'], ['mineral water', 'tomatoes'], ['olive oil', 'frozen vegetables'], ['olive oil', 'spaghetti'], ['shrimp', 'frozen vegetables'], ['shrimp', 'spaghetti'], ['tomatoes', 'frozen vegetables'], ['tomatoes', 'spaghetti'], ['mineral water', 'grated cheese'], ['green tea', 'spaghetti'], ['green tea', 'ground beef'], ['mineral water', 'herb & pepper'], ['herb & pepper', 'spaghetti'], ['herb & pepper', 'ground beef'], ['mineral water', 'ground beef'], ['mineral water', 'milk'], ['ground beef', 'milk'], ['spaghetti', 'milk'], ['ground beef', 'milk'], ['mineral water', 'olive oil'], ['pancakes', 'mineral water'], ['pancakes', 'ground beef'], ['mineral water', 'spaghetti'], ['mineral water', 'ground beef'], ['olive oil', 'spaghetti'], ['olive oil', 'ground beef'], ['pancakes', 'spaghetti'], ['pancakes', 'ground beef'], ['shrimp', 'spaghetti'], ['shrimp', 'ground beef'], ['tomatoes', 'spaghetti'], ['tomatoes', 'ground beef'], ['mineral water', 'herb & pepper'], ['mineral water', 'olive oil'], ['olive oil', 'milk'], ['mineral water', 'shrimp'], ['soup', 'mineral water'], ['soup', 'milk'], ['mineral water', 'spaghetti'], ['mineral water', 'tomatoes'], ['mineral water', 'turkey'], ['turkey', 'milk'], ['olive oil', 'spaghetti'], ['olive oil', 'milk'], ['tomatoes', 'spaghetti'], ['tomatoes', 'milk'], ['mineral water', 'olive oil'], ['mineral water', 'spaghetti'], ['mineral water', 'salmon'], ['salmon', 'spaghetti'], ['mineral water', 'shrimp'], ['soup', 'spaghetti'], ['mineral water', 'tomatoes']]

	cons=[['milk','chocolate'], ['mineral water'], ['frozen vegetables'], ['frozen vegetables'], ['ground beef'], ['ground beef'], ['ground beef'], ['ground beef'], ['ground beef'], ['ground beef'], ['spaghetti'], ['milk'], ['milk'], ['spaghetti'], ['spaghetti'], ['spaghetti'], ['spaghetti'], ['eggs'], ['milk'], ['milk'], ['spaghetti'], ['mineral water'], ['chocolate'], ['mineral water'], ['milk'], ['ground beef'], ['milk'], ['chocolate'], ['ground beef'], ['frozen vegetables'], ['chocolate'], ['milk'], ['frozen vegetables'], ['chocolate'], ['frozen vegetables'], ['milk'], ['ground beef'], ['ground beef'], ['spaghetti'], ['milk'], ['milk'], ['mineral water'], ['mineral water'], ['spaghetti'], ['spaghetti'], ['mineral water'], ['spaghetti'], ['mineral water'], ['milk'], ['frozen vegetables'], ['milk'], ['ground beef'], ['mineral water'], ['ground beef'], ['spaghetti'], ['mineral water'], ['milk'], ['frozen vegetables'], ['ground beef'], ['spaghetti'], ['pancakes'], ['pancakes'], ['milk'], ['milk'], ['spaghetti'], ['milk'], ['ground beef'], ['frozen vegetables'], ['ground beef'], ['frozen vegetables'], ['mineral water'], ['ground beef'], ['spaghetti'], ['frozen vegetables'], ['milk'], ['frozen vegetables'], ['milk'], ['spaghetti'], ['frozen vegetables'], ['frozen vegetables'], ['mineral water'], ['frozen vegetables'], ['frozen vegetables'], ['frozen vegetables'], ['spaghetti'], ['frozen vegetables'], ['spaghetti'], ['frozen vegetables'], ['spaghetti'], ['frozen vegetables'], ['spaghetti'], ['ground beef'], ['spaghetti'], ['ground beef'], ['ground beef'], ['spaghetti'], ['milk'], ['ground beef'], ['mineral water'], ['ground beef'], ['spaghetti'], ['ground beef'], ['ground beef'], ['mineral water'], ['ground beef'], ['spaghetti'], ['ground beef'], ['spaghetti'], ['ground beef'], ['spaghetti'], ['ground beef'], ['spaghetti'], ['ground beef'], ['spaghetti'], ['spaghetti'], ['milk'], ['mineral water'], ['milk'], ['milk'], ['mineral water'], ['milk'], ['milk'], ['milk'], ['mineral water'], ['milk'], ['spaghetti'], ['milk'], ['spaghetti'], ['spaghetti'], ['pancakes'], ['spaghetti'], ['mineral water'], ['spaghetti'], ['mineral water'], ['spaghetti']]
	itemlist=['pancakes', 'milk', 'cereals', 'escalope', 'pepper', 'burgers', 'soup', 'shrimp', 'mineral water', 'chicken', 'frozen smoothie', 'cooking oil', 'chocolate', 'red wine', 'green tea', 'eggs', 'frozen vegetables', 'ground beef', 'olive oil', 'cake', 'extra dark chocolate', 'spaghetti', 'whole wheat pasta', 'turkey', 'tomato sauce', 'tomatoes', 'herb & pepper', 'salmon', 'grated cheese', 'french fries']
	
	
	query=Todo.query.all()
	
	
	l=set()
	j=None
	for i in query:
		j=i.text
	for count,ele in enumerate(ante):
		if j in ele:
			for k in cons[count]:
				l.add(k)


	return render_template('index.html',itemlist=itemlist,text1=query,item_predict=l)
@app.route('/checkbox/<id>')
def checkbox(id):
	enteritem = Todo(text=id, complete=False)
	db.session.add(enteritem)
	db.session.commit()
	
	return redirect(url_for('index'))



@app.route('/delete')
def delete():
    query=Todo.query.all()
    for i in query:

    	db.session.delete(i)
    	db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/delete_item/<id>')
def delete_item(id):

    todo = Todo.query.filter_by(id=int(id)).first()
    db.session.delete(todo)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add():
    enteritem = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(enteritem)
    db.session.commit()


    return redirect(url_for('index'))

# @app.route('/add', methods=['POST'])
# def add():
# 	# if request.method == 'POST':
# 	text1=request.form['todoitem']
# 	query=Todo.query.all()
# 	return render_template('index.html',text1=query)
	
	#print(request.form.get("interest1") != None)
	#return redirect(url_for('index'))
   # tb=request.form.getlist('interest1')
    


if __name__ == '__main__':
    app.run(debug=True)
