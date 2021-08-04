from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/my-link/')
def my_link():
  os.system("echo stevejobs")
  os.system("python3 main.py")
  return 'The eye-tracking is started!'


if __name__ == '__main__':
  app.run(debug=True)
