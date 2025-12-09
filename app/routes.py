from flask import Blueprint, render_template, redirect, url_for, request
from . import db
from .models import Client, Project, ProjectTask, Consultant, User

main = Blueprint('main', __name__)

# Dashboard route
@main.route('/')
def dashboard():
    clients = Client.query.all()
    projects = Project.query.all()
    tasks = ProjectTask.query.all()
    consultants = Consultant.query.all()
    
    return render_template('dashboard.html', 
                         clients=clients, 
                         projects=projects,
                         tasks=tasks,
                         consultants=consultants)

# Add client route
@main.route('/clients/new', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        client = Client(
            name=request.form['name'],
            contact_email=request.form['contact_email'],
            contact_phone=request.form['contact_phone'],
            industry=request.form['industry'],
            address=request.form.get('address', '')
        )
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('clients/form.html')

# Edit client route
@main.route('/clients/<int:id>/edit', methods=['GET', 'POST'])
def edit_client(id):
    client = Client.query.get_or_404(id)
    if request.method == 'POST':
        client.name = request.form['name']
        client.contact_email = request.form['contact_email']
        client.contact_phone = request.form['contact_phone']
        client.industry = request.form['industry']
        client.address = request.form.get('address', '')
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('clients/form.html', client=client)

# Delete client route
@main.route('/clients/<int:id>/delete', methods=['POST'])
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('main.dashboard'))

