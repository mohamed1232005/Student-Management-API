from flask import Blueprint, jsonify, request
from middleware.auth import authenticate_token

studentss = Blueprint('students', __name__)

# Sample data representing students
students = [
    {'id': 1, 'name': 'John Doe', 'age': 21, 'major': 'Computer Science'},
    {'id': 2, 'name': 'Jane Smith', 'age': 22, 'major': 'Physics'},
    {'id': 3, 'name': 'Mike Johnson', 'age': 20, 'major': 'Mathematics'}
]


# Endpoint 1
# GET /students - Get a list of all students
@studentss.route('/', methods=['GET'])
def get_students():
    auth_response = authenticate_token()
    if auth_response:
        return auth_response
    return jsonify(students)


# Endpoint 2
# GET /students/<id> - Get student details by ID
@studentss.route('/<int:id>', methods=['GET'])
def get_student(id):
    auth_response = authenticate_token()
    if auth_response:
        return auth_response
    
    student = next((student for student in students if student['id'] == id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({'message': 'Student not found'}), 404


# Endpoint 3
# POST /students - Add a new student
@studentss.route('/', methods=['POST'])
def add_student():
    auth_response = authenticate_token()
    if auth_response:
        return auth_response
    
    new_student = request.get_json()
    new_student['id'] = students[-1]['id'] + 1 if students else 1  # Assign new ID
    students.append(new_student)
    return jsonify(new_student), 201


# Endpoint 4
# PUT /students/<id> - Update a student's details
@studentss.route('/<int:id>', methods=['PUT'])
def update_student(id):
    auth_response = authenticate_token()
    if auth_response:
        return auth_response
    
    student = next((student for student in students if student['id'] == id), None)
    if student:
        data = request.get_json()
        student.update(data)
        return jsonify(student)
    else:
        return jsonify({'message': 'Student not found'}), 404


# Endpoint 5
# DELETE /students/<id> - Delete a student's record
@studentss.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    auth_response = authenticate_token()
    if auth_response:
        return auth_response
    
    global students
    students = [student for student in students if student['id'] != id]
    return jsonify({'message': 'Student deleted'})
