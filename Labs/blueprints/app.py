from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound
from simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)


if __name__ == '__main__':
    app.run()
