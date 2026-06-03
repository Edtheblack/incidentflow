# IncidentFlow

**IT Incident Management System**

A professional web-based incident management application built with Python, Flask, and SQLite. Designed for IT Support, Digital Systems, and IT Operations roles.

## Overview

IncidentFlow is a portfolio project that demonstrates full-stack web development capabilities including:
- Backend development with Python and Flask
- Database design with SQLite
- Frontend development with Bootstrap 5
- Clean code architecture and best practices

## Features

### Current (Phase 1)
- [x] Flask application setup
- [x] Project structure initialization
- [ ] Database implementation
- [ ] Incident CRUD operations
- [ ] Search functionality
- [ ] Dashboard with statistics

### Planned Features
- Create, read, update, and delete incident tickets
- Ticket priorities: Low, Medium, High, Critical
- Ticket statuses: Open, In Progress, Resolved, Closed
- Search and filter incidents
- Dashboard with key metrics
- Responsive Bootstrap 5 UI
- Assignment tracking

## Tech Stack

- **Backend**: Python 3.10+, Flask 2.3.x
- **Database**: SQLite 3
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **ORM**: SQLAlchemy (planned)
- **Testing**: Pytest (planned)

## Project Structure

```
incidentflow/
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── templates/             # Jinja2 HTML templates
│   └── index.html         # Home page
├── static/                # Frontend assets
│   └── style.css          # Custom styles
└── database/              # Database files (generated at runtime)
```

## Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Edtheblack/incidentflow.git
   cd incidentflow
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Linux/macOS
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:5000`
   - You should see the IncidentFlow home page

## Development

### Running the Development Server

```bash
python app.py
```

The application runs in debug mode on `http://127.0.0.1:5000` with automatic reloading.

### Project Roadmap

**Phase 1: Foundation & Setup** ✅
- Flask application factory
- Project structure
- Home page template

**Phase 2: Database Layer** (In Progress)
- SQLAlchemy ORM setup
- Incident model
- Database initialization

**Phase 3: Service Layer** (Planned)
- Business logic implementation
- Validation layer
- Search functionality

**Phase 4: API Routes** (Planned)
- CRUD endpoints
- Blueprint organization
- Error handling

**Phase 5: Frontend Templates** (Planned)
- Dashboard
- Incident list
- Create/Edit forms
- Detail views

**Phase 6: User Experience** (Planned)
- Custom styling
- Form validation
- Flash notifications
- Pagination

**Phase 7: Testing & Documentation** (Planned)
- Unit tests
- Integration tests
- API documentation

**Phase 8: Deployment** (Planned)
- Production configuration
- Docker containerization
- Deployment guide

## File Descriptions

### `app.py`
Main Flask application entry point. Contains:
- Application factory (`create_app()`) for creating Flask instances
- Route definitions
- Configuration settings

### `requirements.txt`
List of Python package dependencies. Install with:
```bash
pip install -r requirements.txt
```

### `templates/index.html`
Base HTML template for the home page. Uses:
- Bootstrap 5 for responsive design
- Semantic HTML5
- Jinja2 template syntax

### `static/style.css`
Custom CSS styles extending Bootstrap 5 defaults.

### `database/`
Directory for SQLite database file (created during Phase 2).

## Contributing

This is a portfolio project. For improvements or suggestions, please open an issue or contact the repository owner.

## License

This project is open source and available under the MIT License.

## Author

**Edtheblack**
- GitHub: [@Edtheblack](https://github.com/Edtheblack)

## Acknowledgments

- Flask documentation and community
- Bootstrap 5 framework
- Python software foundation
