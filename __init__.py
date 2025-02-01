from flask import Flask, session, redirect, url_for, render_template
from flask_session import Session
from pymongo import MongoClient
from routes.auth import auth_bp
from routes.questions import questions_bp
from routes.analysis import analysis_bp
from routes.dbquestions import dbms_bp
from routes.learning_path import learning_path_bp
from routes.dbqueries import dbms_sql_bp # Import the new blueprint
from routes.tasks import tasks_bp  
from routes.company_questions import company_questions_bp
from routes.daily_tasks import daily_tasks_bp
from routes.chatbot import chatbot_bp
from routes.home import home_bp
from routes.admin import admin_bp
from routes.courses import courses_bp
from routes.resume import resume_bp

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['placementPrep']

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'  # Replace with your actual secret key
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.db = db

    Session(app)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(questions_bp)
    app.register_blueprint(analysis_bp)
    app.register_blueprint(dbms_bp)
    app.register_blueprint(learning_path_bp)
    app.register_blueprint(dbms_sql_bp)  # Register the SQL blueprint
    app.register_blueprint(tasks_bp)
    app.register_blueprint(company_questions_bp)
    app.register_blueprint(daily_tasks_bp)
    app.register_blueprint(chatbot_bp, url_prefix="/api")
    app.register_blueprint(home_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(resume_bp)
    
    @app.route('/')
    def home():
        if 'username' in session:
            return render_template('home.html')
        else:
            return redirect(url_for('auth.show_login'))
        
    @app.route('/learning_path')
    def learning_path():
        if 'username' not in session:
            return redirect(url_for('auth.show_login'))
        return render_template('learning_path.html')
    
    return app
