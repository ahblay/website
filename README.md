# Personal Static Website

This is a personal static website built using Python Flask with Jinja2 templating, CSS, and HTML5. The website is deployed on Netlify, which is linked to GitHub to automatically deploy changes or updates. It can be found at https://www.abelromer.com.

The CSS styling used in this website is original and scalable to mobile and tablet devices. Flask-Frozen is used to freeze the web application into a set of static files that are easily rendered in a browser.

## Installation and Usage

To clone the repository to your personal machine and install all dependencies, follow these steps:

1. Clone the repository from GitHub to your local machine.
2. Navigate to the root directory of the cloned repository.
3. Install all dependencies from the `requirements.txt` file by running the command `pip install -r requirements.txt`.
4. Run the Flask application using the command `flask run`.
5. The application should now be running locally on your machine. You can access the website by opening your web browser and navigating to `http://localhost:5000`.

## Deployment

This website is deployed on Netlify and linked to the GitHub repository. Any changes made to the repository will be automatically deployed to the live website. To deploy the website to Netlify, follow these steps:

1. Sign up for a Netlify account at https://www.netlify.com/.
2. Create a new site in Netlify and link it to the GitHub repository.
3. Configure the build settings to use Flask-Frozen to generate the static files.
4. Netlify will automatically deploy the website whenever changes are pushed to the GitHub repository.

## Credits

This website was built by Abel Romer. Feel free to use the code as a template for your own personal website.
