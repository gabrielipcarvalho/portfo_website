from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import csv
import os

app = Flask(__name__)

@app.route("/")
def my_home():
	return render_template("index.html")

@app.route("/<string:page_name>")
def html_home(page_name):
	return render_template(page_name)

def write_to_csv(data, time):
	file_path = "./database.csv"
	# Check if the file exists and if it is empty
	if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
		with open(file_path, mode="r", newline='') as file_check:
			has_header = csv.Sniffer().has_header(file_check.read(1024))
	else:
		has_header = False
	# Opening and writting to file
	with open(file_path, mode="a", newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		current_time = time
		csv_writer = csv.writer(database2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
		#checking for header
		if not has_header:
			csv_writer.writerow(["Time", "Email", "Subject", "Message"])
		#writing form to db
		csv_writer.writerow([current_time, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
			data = request.form.to_dict()
			write_to_csv(data, current_time)
			return redirect("/thankyou.html")
		except:
			return 'did not save to database'
	else:
		return 'somthing went wrong, try again!'