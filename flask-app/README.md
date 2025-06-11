# Flask Web Application

This is a simple Flask web application that demonstrates the basic structure and functionality of a Flask project.

## Project Structure

```
flask-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-app
   ```

2. **Create a virtual environment:**
   ```
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Flask application, execute the following command:

```
python run.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

Once the application is running, navigate to the root URL in your web browser to view the index page. You can modify the HTML template in `app/templates/index.html` to change the content displayed on the page.

## License

This project is licensed under the MIT License.