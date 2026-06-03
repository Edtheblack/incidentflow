"""
IncidentFlow - IT Incident Management System
Flask application entry point
"""

from flask import Flask, render_template


def create_app():
    """
    Application factory for Flask app initialization.
    
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    app.config['DEBUG'] = True
    
    # Register routes
    @app.route('/')
    def home():
        """
        Home page route.
        
        Returns:
            str: Rendered home page template
        """
        return render_template('index.html')
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5000, debug=True)
