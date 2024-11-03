from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
	return open('./static/main_page.html').read()


@app.route('/software')
def software_page():
	return open('./static/software.html').read()


if __name__ == '__main__':
	app.run(debug=True)
