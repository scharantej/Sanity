## Flask Application Design for a Mental Health Resources Web App

### HTML Files

- **index.html**: This file will serve as the homepage of the application. It will contain:
    - A friendly welcome message and a brief overview of the app's purpose.
    - A list of mental health resources, such as hotlines, support websites, and therapy centers.
    - A section where users can share their thoughts and experiences anonymously.

- **contact.html**: This file will provide contact information for the app's creators. It will include:
    - Email address or contact form for reaching the team.
    - Social media links to connect with the app's community.
    - Disclaimer and privacy policy for the app's data usage.

### Routes

- **@app.route('/')**: This route will render the **index.html** file, displaying the homepage of the application.

- **@app.route('/contact')**: This route will render the **contact.html** file, providing contact information and other relevant details.

- **@app.route('/anonymous')**: This route will handle the submission of anonymous thoughts and experiences shared by users. It will save the submitted data to a designated database or storage system.

- **@app.route('/resources')**: This route will fetch the list of mental health resources from the database and display them on the homepage (**index.html**).

- **@app.route('/search')**: This route will allow users to search for specific mental health resources based on criteria such as location, type of support, etc. It will return a filtered list of resources that match the search parameters.