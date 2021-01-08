from flask import Flask
import six
app = Flask(__name__)


app.route("/")
def index():
    return "hello, World"

if __name__ == "__main__":
    if isinstance(value, six.string_types):
        handle_string(value)
    app.run()