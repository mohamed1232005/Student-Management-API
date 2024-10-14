from flask import Flask
from routes.students import studentss

app = Flask(__name__)

# Register the blueprint for items (student management routes)
app.register_blueprint(studentss,url_prefix='/students')

if __name__ == '__main__':
    app.run(port=3000)
