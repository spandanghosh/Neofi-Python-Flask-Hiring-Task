# Neofi-Python-Flask-Hiring-Task
# Flask Note Taking API

## Running the Flask Project Locally

To run the Flask project on your computer, follow these steps:

### 1. Download or Clone the Project

- Download or clone the Flask project from the [GitHub repository](https://github.com/wpcodevo/flask-note-taking-api).
- Open the source code in your preferred code editor.

### 2. Create a Virtual Environment

- Create a virtual environment for the Flask project using the command:
  ```bash
  python3 -m venv venv
### 3. Install Dependencies

- Install the required dependencies for the Flask app by running the command:
  ```bash
  pip install -r requirements.txt
  
### 4. Launch PostgreSQL Server

To run the Flask project on your computer, you'll need to start a PostgreSQL server in a Docker container. Follow these steps:

- **Start PostgreSQL Server:**
  - Open a terminal.
  - Navigate to the root directory of the Flask project.
  - Run the following command:
    ```bash
    docker-compose up -d
    ```
    This command starts the PostgreSQL server in the background.

Now, the PostgreSQL server is running, and your Flask app can interact with the database. Proceed to the next steps to complete the setup.

### 5. Apply Database Migrations

After starting the PostgreSQL server, you'll need to apply SQLAlchemy migrations to set up the necessary tables and schema in the database. Follow these steps:

- **Apply Migrations:**
  - Open a terminal.
  - Navigate to the root directory of the Flask project.
  - Run the following command to apply migrations:
    ```bash
    flask db upgrade
    ```
    This command ensures that the database is configured with the required tables and schema.

Now, your Flask project is connected to the PostgreSQL database with the necessary structure. Move on to the next step to start the Flask development server.

### 6. Start Flask Development Server

With the PostgreSQL server configured and migrations applied, you can now start the Flask development server to run your application locally. Follow these steps:

- **Start Flask Server:**
  - Open a terminal.
  - Navigate to the root directory of the Flask project.
  - Run the following command to launch the Flask development server:
    ```bash
    flask run
    ```
    The Flask app will be accessible at [http://localhost:8000](http://localhost:8000).

Now, your Flask app is running locally, and you can interact with it through the provided endpoint. Move on to the final step for testing the endpoints.

### 7. Testing Endpoints

Now that the Flask app is running locally, it's time to test the endpoints. To simplify the testing process, an API collection is included in the source code.

- **Access API Collection:**
  - Import the provided `Note App.postman_collection.json` file into either [Postman](https://www.postman.com/) or the [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client) VS Code extension.

This collection contains pre-configured requests for testing various endpoints of the Flask app. Utilize these requests to ensure that your Flask API is functioning as expected.

You have successfully set up and run the Flask app locally, and now you can verify its functionality by testing the included endpoints.

# CRUD Operations with SQLAlchemy

In this section, we leverage SQLAlchemy to execute CRUD operations on the PostgreSQL database. To facilitate interaction with the database, we've implemented various route handlers in a `notes_routes.py` file located within the `src` directory. These route handlers cater to different types of requests, allowing us to manipulate data effectively:

1. **Create Note:**
   - Route: `POST /api/notes`
   - Description: Handles POST requests to the `/api/notes` endpoint, adding new notes to the database.

2. **Update Note:**
   - Route: `PATCH /api/notes/<string:note_id>`
   - Description: Manages PATCH requests to the `/api/notes/<string:note_id>` endpoint, editing an existing note in the database.

3. **Get Note:**
   - Route: `GET /api/notes/<string:note_id>`
   - Description: Processes GET requests to the `/api/notes/<string:note_id>` endpoint, retrieving a single note from the database.

4. **Delete Note:**
   - Route: `DELETE /api/notes/<string:note_id>`
   - Description: Handles DELETE requests to the `/api/notes/<string:note_id>` endpoint, deleting a note from the database.

5. **Get Notes:**
   - Route: `GET /api/notes`
   - Description: Manages GET requests to the `/api/notes` endpoint, fetching a paginated list of notes from the database.

These route handlers enable comprehensive control over the data in the Flask application, allowing for efficient management of notes through Create, Read, Update, and Delete (CRUD) operations.


