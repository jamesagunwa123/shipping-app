from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index.php')
def index():
	return render_template('index.html')

@app.route('/about.php')
def about():
	return render_template('about.html')

@app.route('/air-freight.php')
def air_freight():
	return render_template('air-freight.html')

@app.route('/contact-us.php')
def contact_us():
	return render_template('contact-us.html')

@app.route('/custom-clearance.php')
def custom_clearance():
	return render_template('custom-clearance.html')

@app.route('/land-freight.php')
def land_freight():
	return render_template('land-freight.html')

@app.route('/removals-relocation.php')
def removals_relocation():
	return render_template('removals-relocation.html')

@app.route('/sea-freight.php')
def sea_freight():
	return render_template('sea-freight.html')

@app.route('/service.php')
def service():
	return render_template('service.html')

@app.route('/tracking.php')
def tracking():
	if request.args.get('track') == 'invalidcode' :
		return render_template('tracking.html', invalidcode=True)
	return render_template('tracking.html', invalidcode=False)

@app.route('/tracking1.php', methods=['GET', 'POST'])
def tracking1():
	# example code 630dbf0713f2a

	trackcode = request.form.get('trackcode')
	url_get = 'https://www.fastairwaycouriers.com/tracking.php'
	url_post = 'https://www.fastairwaycouriers.com/tracking1.php'

	if request.method == 'GET':
		return render_template('tracking1.html')

	data = {'trackcode': trackcode, 'track': ''}

	res = requests.post(url_post, data=data)
	print(res.history)
	if res.history and res.history[0].status_code == 302:
		return redirect('/tracking.php?track=invalidcode')
	print('you entered an invalid tracking code please check' in res.text)
	
	return res.text

@app.route('/warehouse.php')
def warehouse():
	return render_template('warehouse.html')

@app.route('/<path:path>')
def static_file(path):
  return app.send_static_file(path)

if __name__ == '__main__':
	app.run(debug=True)