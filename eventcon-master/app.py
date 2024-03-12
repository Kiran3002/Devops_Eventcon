from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Define database connection parameters
DB_NAME = 'Kiran'
DB_USER = 'Kiran'
DB_PASSWORD = 'goneMad@1900'
DB_HOST = 'local_pgdb'
DB_PORT = '5432'

# Define a function to connect to the PostgreSQL database
def connect_to_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

# Route to render HTML page (contact form)
@app.route('/')
def contact_form():
    return render_template('contact.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Connect to the database
    conn = connect_to_db()
    cur = conn.cursor()
    # Extract form data
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Insert data into the table
    cur.execute("INSERT INTO contact_details (name, email, subject, message) VALUES (%s, %s, %s, %s)", (name, email, subject, message))

    # Commit changes
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

    return 'Data submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)
