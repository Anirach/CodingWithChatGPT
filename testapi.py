from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Student Class/Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Student Schema
class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age')

# Init schema
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


# Create a Student
@app.route('/student', methods=['POST'])
def add_student():
    name = request.json['name']
    age = request.json['age']

    new_student = Student(name, age)

    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student)


# Get All Students
@app.route('/student', methods=['GET'])
def get_students():
    all_students = Student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result)


# Get Single Student
@app.route('/student/<id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    return student_schema.jsonify(student)


# Update a Student
@app.route('/student/<id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)

    name = request.json['name']
    age = request.json['age']

    student.name = name
    student.age = age

    db.session.commit()

    return student_schema.jsonify(student)


# Delete Student
@app.route('/student/<id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()

    return student_schema.jsonify(student)

# Run Server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This will create tables defined by your models
    app.run(debug=True)