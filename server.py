from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html') 


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name) 


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_file(data)
		return redirect('thankyou.html')
	else:
		return "FOUT"


def write_to_file(data):
	with open('database.csv',newline='',mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2,delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])



def write_to_csv(data):
	pass

# @app.route('/works.html')
# def works():
#     return render_template('works.html') 

# @app.route('/index.html')
# def show_index():
#     return render_template('index.html') 

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html') 

# @app.route('/components.html')
# def show_components():
#     return render_template('components.html') 

# @app.route('/about.html')
# def about_website():
#     return render_template('about.html') 

# @app.route('/work.html')
# def workwork():
#     return render_template('work.html') 


# @app.route('/favicon.ico')
# def faviconSet():
#     return faviconSet('bolt.ico')