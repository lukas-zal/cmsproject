from flask import Blueprint, render_template, redirect, url_for, request
from . import db
from .models import Client

main = Blueprint('main', __name__)

# Dashboard route
@main.route('/')
def dashboard():
    clients = Client.query.all()
    return render_template('dashboard.html', clients=clients)

# Add client route
@main.route('/clients/new', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        client = Client(
            name=request.form['name'],
            contact_email=request.form['contact_email'],
            phone=request.form['phone'],
            company_size=request.form['company_size'],
            industry=request.form['industry'],
            assigned_consultant=request.form['assigned_consultant']
        )
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('clients/form.html')
