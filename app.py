from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/teachers")
def teachers():
	return render_template("teachers.html")


@app.route("/video")
def video():
	return render_template("video.html")

@app.route("/admin/delete", methods = ['GET', 'POST'])
def delete():
	Coms = query_all()
	if request.method == 'GET':
		return render_template('delete.html',Coms=Coms)
	else:
		id = request.form['id']
		delete_feedback(id)
		return redirect(url_for("feedback"))
	return render_template("delete.html")

@app.route("/admin", methods = ['GET', 'POST'])
def admin():
	Coms = query_all()
	if request.method == 'GET':
		return render_template('admin.html',Coms=Coms)
	else:



		response = request.form['response']
		id = request.form['id']

		editresponse(id, response)        
		return redirect(url_for("feedback"))



@app.route("/feedback")
def feedback():
	comments = query_all()
	# for product in products:
	# 	print(product.name)
	return render_template("feedback.html", Coms = comments)



@app.route("/courses")
def courses():
	return render_template("courses.html")


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
	
    if request.method == 'GET':
        return render_template('contact.html')
    else:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']


        add_feedback(name, email, subject, message)        
        return redirect("/feedback")
    




#####################


if __name__ == '__main__':
    app.run(debug=True)