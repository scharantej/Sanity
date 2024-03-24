
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List of mental health resources
resources = [
    {'name': 'National Suicide Prevention Lifeline', 'phone': '1-800-273-8255'},
    {'name': 'Crisis Text Line', 'text': '741741'},
    {'name': 'The Trevor Project', 'phone': '1-866-488-7386'},
    {'name': 'Substance Abuse and Mental Health Services Administration (SAMHSA)', 'phone': '1-800-662-4357'},
    {'name': 'National Alliance on Mental Illness (NAMI)', 'website': 'https://www.nami.org/'},
]

@app.route('/')
def index():
    """Render the homepage with a list of resources."""
    return render_template('index.html', resources=resources)

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

@app.route('/anonymous', methods=['POST'])
def anonymous():
    """Handle the submission of anonymous thoughts and experiences."""
    # Get the submitted data
    thought = request.form['thought']

    # Save the data to a database or storage system

    # Redirect to the homepage
    return redirect(url_for('index'))

@app.route('/resources')
def get_resources():
    """Fetch the list of mental health resources from the database."""
    return resources

@app.route('/search')
def search_resources():
    """Allow users to search for specific mental health resources."""
    # Get the search parameters
    location = request.args.get('location')
    type = request.args.get('type')

    # Filter the list of resources based on the search parameters

    # Return the filtered list of resources
    return resources

if __name__ == '__main__':
    app.run(debug=True)
