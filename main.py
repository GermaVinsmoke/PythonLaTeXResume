from flask import Flask, redirect
from updater import update_resume

app = Flask(__name__, static_folder='')


@app.route('/')
def resume():
    update_resume()
    return app.send_static_file('vaibhav_resume.pdf')


if __name__ == '__main__':
    app.run()
