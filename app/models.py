from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Client(db.Model):
    __tablename__ = "clients"

    client_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    industry = db.Column(db.String(255))
    contact_email = db.Column(db.String(255))
    contact_phone = db.Column(db.String(50))
    address = db.Column(db.Text)

    # Relationships
    projects = db.relationship('Project', backref='client', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Client {self.name}>'


class Consultant(db.Model):
    __tablename__ = "consultants"

    consultant_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(150))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(255))

    # Relationships
    user = db.relationship('User', backref='consultant_profile', uselist=False)
    tasks = db.relationship('ProjectTask', backref='assigned_consultant')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f'<Consultant {self.full_name}>'


class Project(db.Model):
    __tablename__ = "projects"

    project_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(100))

    # Relationships
    tasks = db.relationship('ProjectTask', backref='project', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Project {self.title}>'


class ProjectTask(db.Model):
    __tablename__ = "project_tasks"

    task_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'), nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('consultants.consultant_id'))
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.Date)
    status = db.Column(db.String(100))

    def __repr__(self):
        return f'<ProjectTask {self.title}>'


class User(UserMixin, db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    consultant_id = db.Column(db.Integer, db.ForeignKey('consultants.consultant_id'))
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(100), default='consultant')

    # Override get_id method for Flask-Login
    def get_id(self):
        return str(self.user_id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
