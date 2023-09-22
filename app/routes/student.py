from flask import Blueprint, jsonify
from ..database import db
from ..models.models import Student
student_router = Blueprint('students', __name__)

@student_router.route("/")
def get_students():
    # Add logic to fetch students from the database here
    # students = [{"name": "Student 1"}, {"name": "Student 2"}]
    
    # return db.query(Student).all()
    return Student.query.all()
