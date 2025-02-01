from __init__ import create_app

app = create_app()  # Create the Flask app instance using the create_app function

if __name__ == '__main__':
    app.run(debug=True)
