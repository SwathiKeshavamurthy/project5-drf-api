<p align="center">
  <img src="static/images/favicon.JPG" alt="Fit&Fine Logo" style="width: 100px; height: auto;">
</p>
<h1 align="center">Fit&Fine</h1>

[Fit&Fine Django Rest Framework API Backend Live Link](https://fitandfine-drf-be560b223a3b.herokuapp.com/)

[Fit&Fine React Frontend Live Link](https://fitandfine-react-p5-f5d23da9d77c.herokuapp.com/)

[Fit&Fine React Frontend Github Repo](https://github.com/SwathiKeshavamurthy/fitandfine-react-p5)

## Project Goals

Fit&Fine is designed to be a comprehensive fitness companion for users of all levels, from beginners to seasoned athletes. The primary goals of the web app are to:
1) Provide users with tools to set fitness challenges, track daily routines, and monitor their progress, fostering a supportive and motivating community.
2) Deliver a user-friendly and engaging platform where users can create and share posts, follow other users, and collaborate on fitness activities.
3) Ensure a streamlined experience with essential features like personalized daily routines, community challenges, and the ability to manage profiles, posts, and comments.

The backend is implemented using Django Rest Framework API for the [Fit&Fine Website](https://fitandfine-react-p5-f5d23da9d77c.herokuapp.com/). It is designed to support both web and future mobile applications providing robust and secure APIs for the Fit&Fine React frontend application, ensuring seamless integration and future scalability.

## Table of contents
- [Project Goals](#project-goals)
- [Table of contents](#table-of-contents)
- [Planning](#planning)
  - [Project Overview](#project-overview)
  - [Objectives](#objectives)
  - [Timeline](#timeline)
- [Data Models](#data-models)
  - [1. Profiles Model](#1-profiles-model)
  - [2. Posts Model](#2-posts-model)
  - [3. Comments Model](#3-comments-model)
  - [4. Daily Routines Model](#4-daily-routines-model)
  - [5. Challenges Model](#5-challenges-model)
  - [6. Collaborate Model](#6-collaborate-model)
  - [7. Likes Model](#7-likes-model)
  - [8. Follower Model](#8-follower-model)
- [API Endpoints](#api-endpoints)
  - [Example Requests and Responses](#example-requests-and-responses)
- [Frameworks, Libraries, and Dependencies](#frameworks-libraries-and-dependencies)
  - [Django Framework and Extensions](#django-framework-and-extensions)
  - [Database Management](#database-management)
  - [Authentication and Security](#authentication-and-security)
  - [Storage and Image Handling](#storage-and-image-handling)
  - [Application Server](#application-server)
  - [Utility Libraries](#utility-libraries)
- [Testing and Validation](#testing-and-validation)
- [Bugs](#bugs)
  - [Solved Bugs](#solved-bugs)
  - [Known Bugs](#known-bugs)
  - [Unknown Bugs](#unknown-bugs)
- [Deployment](#deployment)
  - [1. GitHub](#1-github)
  - [2. Gitpod](#2-gitpod)
  - [3. Heroku](#3-heroku)
  - [4. ElephantSQL](#4-elephantsql)
  - [5. Cloudinary](#5-cloudinary)
  - [Deployment Steps](#deployment-steps)
- [Cloning and Forking](#cloning-and-forking)
  - [Cloning the Repository](#cloning-the-repository)
  - [Forking the Repository](#forking-the-repository)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
- [Acknowledgements](#acknowledgements)
  - [Inspiration](#inspiration)
  - [Project Guidance](#project-guidance)
  - [Personal Thanks](#personal-thanks)

## Planning

The planning phase for the Fit&Fine project encompasses several key areas to ensure the successful development and deployment of both the backend and frontend components. Here is a comprehensive plan to guide the development process:

### Project Overview

Fit&Fine is a comprehensive fitness platform designed to help users achieve their health and wellness goals. The platform includes features such as challenges, daily routines, and social interaction to create a supportive and motivating environment for users.

### Objectives

1. Develop a robust backend API using Django Rest Framework to handle data management and user authentication.
2. Build an intuitive and responsive frontend using React to provide a seamless user experience.
3. Integrate key features such as user profiles, posts, comments, likes, challenges, and daily routines.

### Timeline

1. **Week 1: Project Setup and Initial Development**
   - Set up backend and frontend repositories.
   - Configure Django Rest Framework for the backend.
   - Initialize React project for the frontend.
   - Set up initial project structure and environment configurations.

2. **Week 2: User Authentication and Profile Management**
   - Implement user registration, login, and logout functionality.
   - Develop user profile creation and editing features.
   - Ensure secure password handling and authentication processes.

3. **Week 3: Core Features Development**
   - Develop the functionality for creating, editing, and deleting posts.
   - Implement comments and likes features for posts.
   - Develop daily routines and challenges features, including creation and management.

4. **Week 4: Frontend Integration and Styling**
   - Integrate backend API with the frontend.
   - Develop responsive and user-friendly UI components.
   - Apply consistent styling using CSS modules or a CSS framework.

5. **Week 5: Testing and Debugging**
   - Conduct thorough testing of all features.
   - Fix any bugs or issues identified during testing.
   - Perform user acceptance testing (UAT) to ensure the platform meets user needs.

6. **Week 6: Deployment and Documentation**
   - Deploy the backend API to a cloud service (e.g., Heroku, AWS).
   - Deploy the frontend application to a hosting service (e.g., Netlify, Vercel).
   - Write comprehensive documentation, including setup instructions, API documentation, and user guides.

## Data Models

The Fit&Fine backend project is organized into several key models, each representing different aspects of the Fit&Fine platform. Below is an overview of the primary data models used in the project:

### 1. Profiles Model
   - **Profile**: Stores user-specific information such as username, password, profile image, bio, email, and birthday.

**Fields**:
  - `user`: ForeignKey to the User model
  - `bio`: TextField
  - `image`: ImageField
  - `email`: EmailField
  - `birthday`: DateField
  - `followers_count`: IntegerField
  - `following_count`: IntegerField
  - `posts_count`: IntegerField

### 2. Posts Model
   - **Post**: Represents user-generated content, including fields for the title, content, image, tags, creation date, and owner.
   
**Fields**:
  - `owner`: ForeignKey to Profile
  - `title`: CharField
  - `content`: TextField
  - `image`: ImageField
  - `tags`: CharField
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField
  - `comments_count`: IntegerField
  - `likes_count`: IntegerField

### 3. Comments Model
  - **Comment**: Allows users to comment on posts, with fields for the content, creation date, post it belongs to, and owner.
  - 
**Fields**:
  - `owner`: ForeignKey to Profile
  - `post`: ForeignKey to Post
  - `content`: TextField
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField

### 4. Daily Routines Model
   - **DailyRoutine**: Tracks daily activities and health metrics, including fields for date, wake-up time, meal times, calorie intake, water intake, workout minutes, sleep time, junk food consumption, and mood.
  
**Fields**:
  - `owner`: ForeignKey to Profile
  - `date`: DateField
  - `wake_up_time`: TimeField
  - `breakfast_time`: TimeField
  - `lunch_time`: TimeField
  - `dinner_time`: TimeField
  - `total_calorie_intake`: IntegerField
  - `water_intake`: IntegerField
  - `sleep_time`: TimeField
  - `workout_minutes`: IntegerField
  - `junk`: BooleanField
  - `mood`: CharField

### 5. Challenges Model
   - **Challenge**: Represents fitness challenges that users can participate in, with fields for title, description, start and end dates, sport type, and an associated image.
   - **Participant**: Tracks users who are participating in a particular challenge.

**Fields**:
  - `title`: CharField
  - `description`: TextField
  - `start_date`: DateField
  - `end_date`: DateField
  - `sport`: CharField
  - `image`: ImageField

### 6. Collaborate Model
   - **Collaborate**: Handles collaboration requests and messages between users, including fields for the name, email, message content, and date of submission.

**Fields**:
  - `name`: CharField
  - `email`: EmailField
  - `message`: TextField
  - `submitted_at`: DateTimeField

### 7. Likes Model
- **Like**: Tracks which users have liked a particular post.
and Followers Models

**Fields**:
  - `owner`: ForeignKey to Profile
  - `post`: ForeignKey to Post
   
### 8. Follower Model   
- **Follower**: Manages follower-following relationships between users.

**Fields**:
  - `owner`: ForeignKey to Profile
  - `following`: ForeignKey to Profile

Sure, here's the updated API Endpoints section with CRUD operation and View Type columns added:

Here's the table formatted for a README.md file:

## API Endpoints

The Fit&Fine backend provides a RESTful API to interact with the various models. Below is a list of the primary API endpoints for each model, including their respective HTTP methods and descriptions.

| Endpoint                    | HTTP Method | CRUD Operation | View Type         | Description                                               |
|-----------------------------|-------------|----------------|-------------------|-----------------------------------------------------------|
| **Authentication Endpoints**                                                                 |
| `/dj-rest-auth/login/`      | POST        | Create         | Auth              | Log in a user and obtain authentication tokens.           |
| `/dj-rest-auth/logout/`     | POST        | Delete         | Auth              | Log out a user and invalidate their authentication tokens.|
| `/dj-rest-auth/registration/`| POST       | Create         | Auth              | Register a new user.                                      |
| **Profile Endpoints**                                                                       |
| `/profiles/`                | GET         | Read           | List              | Retrieve a list of profiles.                              |
|                             | POST        | Create         | Create            | Create a new profile (admin only).                        |
| `/profiles/<id>/`           | GET         | Read           | Detail            | Retrieve a specific profile by ID.                        |
|                             | PUT         | Update         | Update            | Update a specific profile by ID.                          |
|                             | PATCH       | Update         | Partial Update    | Partially update a specific profile by ID.                |
|                             | DELETE      | Delete         | Delete            | Delete a specific profile by ID (admin only).             |
| **Post Endpoints**                                                                          |
| `/posts/`                   | GET         | Read           | List              | Retrieve a list of posts.                                 |
|                             | POST        | Create         | Create            | Create a new post.                                        |
| `/posts/<id>/`              | GET         | Read           | Detail            | Retrieve a specific post by ID.                           |
|                             | PUT         | Update         | Update            | Update a specific post by ID.                             |
|                             | PATCH       | Update         | Partial Update    | Partially update a specific post by ID.                   |
|                             | DELETE      | Delete         | Delete            | Delete a specific post by ID.                             |
| **Comment Endpoints**                                                                       |
| `/comments/`                | GET         | Read           | List              | Retrieve a list of comments.                              |
|                             | POST        | Create         | Create            | Create a new comment.                                     |
| `/comments/<id>/`           | GET         | Read           | Detail            | Retrieve a specific comment by ID.                        |
|                             | PUT         | Update         | Update            | Update a specific comment by ID.                          |
|                             | PATCH       | Update         | Partial Update    | Partially update a specific comment by ID.                |
|                             | DELETE      | Delete         | Delete            | Delete a specific comment by ID.                          |
| **Daily Routine Endpoints**                                                                |
| `/dailyroutines/`           | GET         | Read           | List              | Retrieve a list of daily routines.                        |
|                             | POST        | Create         | Create            | Create a new daily routine.                               |
| `/dailyroutines/<id>/`      | GET         | Read           | Detail            | Retrieve a specific daily routine by ID.                  |
|                             | PUT         | Update         | Update            | Update a specific daily routine by ID.                    |
|                             | PATCH       | Update         | Partial Update    | Partially update a specific daily routine by ID.          |
|                             | DELETE      | Delete         | Delete            | Delete a specific daily routine by ID.                    |
| **Challenge Endpoints**                                                                   |
| `/challenges/`              | GET         | Read           | List              | Retrieve a list of challenges.                            |
|                             | POST        | Create         | Create            | Create a new challenge.                                   |
| `/challenges/<id>/`         | GET         | Read           | Detail            | Retrieve a specific challenge by ID.                      |
|                             | PUT         | Update         | Update            | Update a specific challenge by ID.                        |
|                             | PATCH       | Update         | Partial Update    | Partially update a specific challenge by ID.              |
|                             | DELETE      | Delete         | Delete            | Delete a specific challenge by ID.                        |
| `/challenges/<id>/join/`    | POST        | Create         | Action            | Join a specific challenge.                                |
| `/challenges/<id>/leave/`   | POST        | Create         | Action            | Leave a specific challenge.                               |
| **Collaborate Endpoints**                                                                 |
| `/collaborate/`             | GET         | Read           | List              | Retrieve a list of collaboration messages.                |
|                             | POST        | Create         | Create            | Create a new collaboration message.                       |
| `/collaborate/<id>/`        | GET         | Read           | Detail            | Retrieve a specific collaboration message by ID.          |
|                             | DELETE      | Delete         | Delete            | Delete a specific collaboration message by ID.            |
| **Like Endpoints**                                                                         |
| `/likes/`                   | GET         | Read           | List              | Retrieve a list of likes.                                 |
|                             | POST        | Create         | Create            | Create a new like.                                        |
| `/likes/<id>/`              | DELETE      | Delete         | Delete            | Delete a specific like by ID.                             |
| **Follower Endpoints**                                                                     |
| `/followers/`               | GET         | Read           | List              | Retrieve a list of followers.                             |
|                             | POST        | Create         | Create            | Follow a user.                                            |
| `/followers/<id>/`          | DELETE      | Delete         | Delete            | Unfollow a user by ID.                                    |

### Example Requests and Responses

**Example: Create a Post**

**Request:**
```http
POST /posts/
{
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "tags": "fitness, health"
}
```

**Response:**
```json
201 Created
{
  "id": 1,
  "owner": "username",
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "tags": "fitness, health",
  "created_at": "2023-05-30T12:34:56.789Z",
  "updated_at": "2023-05-30T12:34:56.789Z",
  "comments_count": 0,
  "likes_count": 0
}
```

**Example: Retrieve Profile**

**Request:**
```http
GET /profiles/1/
```

**Response:**
```json
200 OK
{
  "id": 1,
  "user": "username",
  "bio": "This is a sample bio.",
  "image": "http://example.com/media/profile_images/sample.jpg",
  "email": "user@example.com",
  "birthday": "1990-01-01",
  "followers_count": 10,
  "following_count": 5,
  "posts_count": 3
}
```
## Frameworks, Libraries, and Dependencies

The Fit&Fine project leverages a variety of frameworks, libraries, and dependencies to ensure robust functionality and performance. Below is a detailed list of the key components used:

### Django Framework and Extensions

1. **Django** (`Django==3.2.25`):
   - A high-level Python web framework that encourages rapid development and clean, pragmatic design. Django handles much of the complexity of web development, allowing developers to focus on writing their app without needing to reinvent the wheel.

2. **Django REST Framework** (`djangorestframework==3.15.1`):
   - A powerful and flexible toolkit for building Web APIs in Django. It provides various features such as serialization, authentication, and view sets that simplify API development.

3. **Django Allauth** (`django-allauth==0.44.0`):
   - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

4. **Django REST Auth** (`dj-rest-auth==2.1.9`):
   - Provides a set of REST API endpoints for handling user registration and authentication tasks. It’s built on top of Django Allauth and Django REST Framework.

5. **Django Filter** (`django-filter==2.4.0`):
   - Simplifies the process of filtering querysets in Django REST Framework.

6. **Django CORS Headers** (`django-cors-headers==4.3.1`):
   - A Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).

### Database Management

7. **dj-database-url** (`dj-database-url==0.5.0`):
   - Allows you to utilize the DATABASE_URL environment variable to configure your Django application.

8. **psycopg2** (`psycopg2==2.9.9`):
   - PostgreSQL database adapter for Python.

### Authentication and Security

9. **djangorestframework-simplejwt** (`djangorestframework-simplejwt==4.7.2`):
   - Provides JSON Web Token (JWT) authentication for Django REST Framework.

10. **oauthlib** (`oauthlib==3.2.2`):
    - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python.

11. **requests-oauthlib** (`requests-oauthlib==2.0.0`):
    - OAuthlib support for Python-Requests, the ubiquitous HTTP library for Python.

12. **PyJWT** (`PyJWT==2.8.0`):
    - A Python library which allows you to encode and decode JSON Web Tokens (JWT).

### Storage and Image Handling

13. **Pillow** (`Pillow==8.2.0`):
    - Python Imaging Library (PIL) fork that supports opening, manipulating, and saving many different image file formats.

14. **Cloudinary** (`cloudinary==1.40.0`):
    - A library that integrates your application with the Cloudinary service for managing media assets such as images and videos.

15. **django-cloudinary-storage** (`django-cloudinary-storage==0.3.0`):
    - Facilitates the integration of Django with Cloudinary for storing media files.

### Application Server

16. **Gunicorn** (`gunicorn==22.0.0`):
    - A Python WSGI HTTP Server for UNIX that serves your Django application and allows it to handle multiple requests simultaneously.

### Utility Libraries

17. **asgiref** (`asgiref==3.8.1`):
    - A reference implementation of ASGI, the emerging Python standard for asynchronous web servers and applications.

18. **sqlparse** (`sqlparse==0.5.0`):
    - A non-validating SQL parser for Python.

19. **python3-openid** (`python3-openid==3.2.0`):
    - A set of Python packages to support OpenID authentication.

20. **pytz** (`pytz==2024.1`):
    - World timezone definitions, modern and historical.

This combination of frameworks, libraries, and dependencies ensures that Fit&Fine is robust, scalable, and secure, providing a seamless user experience for managing fitness routines and social interactions.

## Testing and Validation

For all testing and validation, please refer to the [TESTING.md](TESTING.md) file.

## Bugs

### Solved Bugs  

| No. | Bug | Solved | Fix | Solution Credit |
| --- | ---------------- | ---- | ------------- | -------------- | 
| 1   | Error when trying to save profile pictures | Yes | Added media URL and root configurations in settings.py and ensured correct file path in the models.py | [Django Documentation](<https://docs.djangoproject.com/en/3.2/ref/settings/#media-root>) |
| 2  | Comments not appearing under posts | Yes | Corrected the foreign key relationships and ensured the comment form was being properly handled in views.py | [StackOverflow](<https://stackoverflow.com/questions/18797740/foreign-key-is-not-updating>) |
| 3   | Notifications not marking as read | Yes | Added logic to update notification status upon user interaction in views.py | [Django Project](<https://docs.djangoproject.com/en/3.2/topics/db/queries/#making-queries>) |
| 4   | Daily routine activities not saving | Yes | Debugged the model save method and fixed form validation errors to ensure proper saving of activities | [Django Forms](<https://docs.djangoproject.com/en/3.2/topics/forms/>) |


### Known Bugs

| No. | Bug | Description | 
| --- | ---- | ----------- | 
| 1   | Post upload does not display any message | When users upload posts, the upload occasionally fails without displaying any error message or confirmation for the user. This lack of feedback can lead to confusion about whether the post was successfully uploaded. Debugging has focused on the post submission and response handling logic, but the problem persists intermittently. |

### Unknown Bugs

I am not aware of any remaining bugs.

## Deployment

The deployment process for Fit and Fine DRF API involves multiple platforms, including GitHub, Gitpod, Heroku, ElephantSQL, and Cloudinary. Below is a detailed explanation of how each platform fits into the deployment process along with the respective URLs for the platforms and services used in deploying and managing the Fit and Fine DRF API.

### 1. GitHub

**Purpose:** 
- Version control and collaboration.

**Process:**
- The source code for Fit and Fine DRF API is hosted on GitHub. Developers can collaborate, track changes, and manage different versions of the application.
- The repository is used as the central hub for the project, where all updates and changes are committed and pushed.

**URL:**
- [GitHub Repository](https://github.com)

### 2. Gitpod

**Purpose:**
- Online IDE for development.

**Process:**
- Gitpod is used for development and testing. It provides a cloud-based development environment that is pre-configured with the necessary tools and dependencies.
- Developers can open the GitHub repository in Gitpod and start coding immediately without worrying about local setup.

**URL:**
- [Gitpod Workspace](https://gitpod.io/)

### 3. Heroku

**Purpose:**
- Platform as a Service (PaaS) for hosting the application.

**Process:**
- The Fit and Fine DRF API application is deployed on Heroku. Heroku manages the server, deployment, and scaling of the application.
- Continuous deployment is set up from the GitHub repository to Heroku, ensuring that any changes pushed to the main branch are automatically deployed to the live site.

**URL:**
- [Heroku Dashboard](https://dashboard.heroku.com/)

**Setting up on Heroku:**
1. Create a new app on Heroku.
2. Connect the Heroku app to the GitHub repository.
3. Set up Config Vars in Heroku including `DATABASE_URL`, `SECRET_KEY`, `CLOUDINARY_URL`, `ALLOWED_HOST`  and `DISABLE_COLLECTSTATIC=1` (this is temporary and can be removed for the final deployment).
4. Deploy the main branch using the Heroku dashboard or enable automatic deployments for every push to the main branch.

**For deployment, Heroku needs two additional files in order to deploy properly:**
- `requirements.txt`
- `Procfile`

You can install this project's requirements (where applicable) using:
- `pip install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs to be updated using:
- `pip freeze --local > requirements.txt`

**The Procfile can be created with the following command:**
- `echo web: gunicorn app_name.wsgi > Procfile`

Then add these lines to Procfile

`web: gunicorn app_name.wsgi`

`release: python manage.py makemigrations && python manage.py migrate`

Replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located.

### 4. ElephantSQL

**Purpose:**
- Database as a Service for PostgreSQL.

**Process:**
- ElephantSQL provides the PostgreSQL database for the Fit and Fine DRF API application. The database is used to store all application data, including user information, posts, comments, and other relevant data.
- Heroku is configured to use the ElephantSQL database through environment variables.

**URL:**
- [ElephantSQL Dashboard](https://customer.elephantsql.com/login)

To obtain your own PostgreSQL Database, sign-up with your GitHub account, then follow these steps:
1. Click **Create New Instance** to start a new database.
2. Provide a name (commonly the name of the project: `fitandfine`).
3. Select the **Tiny Turtle (Free)** plan.
4. You can leave the **Tags** blank.
5. Select the **Region** and **Data Center** closest to you.
6. Once created, click on the new database name, where you can view the database URL and Password.

### 5. Cloudinary

**Purpose:**
- Media management and storage.

**Process:**
- Cloudinary is used for storing and managing media files, such as images and videos uploaded by users.
- The application is configured to upload media files directly to Cloudinary, where they are stored and served.

**URL:**
- [Cloudinary Dashboard](https://cloudinary.com/users/login)

**Integration:**
1. Set up a Cloudinary account.
2. Configure the Cloudinary settings in the Django settings file with the API keys provided by Cloudinary.
3. Use Django’s storage backend for Cloudinary to handle media uploads.

### Deployment Steps

1. **Clone the Repository:**
   - Clone the GitHub repository to your local machine or open it in Gitpod for development.

2. **Configure Environment Variables:**
   - Set up the necessary environment variables in your local `.env` file or in the Heroku dashboard. These include database URL (ElephantSQL), Cloudinary API keys, and other sensitive information.

3. **Install Dependencies:**
   - Install the required dependencies using `pip install -r requirements.txt`.

4. **Run Migrations:**
   - Apply database migrations using `python manage.py migrate` to set up the PostgreSQL database schema.

5. **Test the Application:**
   - Run the application locally or in Gitpod to ensure it works as expected.

6. **Deploy to Heroku:**
   - Push the changes to the GitHub repository, which triggers the continuous deployment to Heroku.
   - Ensure that the Heroku app is properly configured with the necessary environment variables and add-ons (such as ElephantSQL).

7. **Manage Media Files:**
   - Configure Cloudinary in the Django settings and ensure that media files are uploaded and managed correctly.

## Cloning and Forking

### Cloning the Repository

**Local Setup:**
1. Clone the repository: [GitHub repository](https://github.com/SwathiKeshavamurthy/FitandFine-P5). 
   - `git clone https://github.com/SwathiKeshavamurthy/FitandFine-P5`
2. Navigate into the project directory: `cd fitandfine_drf`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up local environment variables in a `.env` file.
5. Run migrations: `python manage.py makemigrations`and`python manage.py migrate`
6. Start the development server: `python manage.py runserver`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/SwathiKeshavamurthy/FitandFine-P5)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

### Forking the Repository

**For Contributions:**
1. Fork the repository on [GitHub repository](https://github.com/SwathiKeshavamurthy/FitandFine-P5).
2. Clone your forked repository to your local machine.
3. Follow the local setup steps as above.
4. Make changes and push them back to your fork.
5. Create a pull request from your fork back to the original repo.

By following these steps and utilizing the aforementioned platforms, the deployment and management of the Fit and Fine DRF API application are streamlined and efficient, ensuring a robust and scalable application.

## Credits

### Code

The development of the Fit and Fine application was supported by various resources and contributions from the community. Here are the key references and sources of inspiration for the Fit and Fine project:

- The technique to limit the size of image uploads to Cloudinary is adapted from this [Cloudinary Support Article](https://support.cloudinary.com/hc/en-us/community/posts/360009752479-How-to-resize-before-uploading-pictures-in-Django).
- A replacement for the deprecated `django.conf.urls.url()` was implemented as per this [StackOverflow Article](https://stackoverflow.com/questions/70319606/importerror-cannot-import-name-url-from-django-conf-urls-after-upgrading-to).
- How to access URL arguments as kwargs in generic APIViews is from this [StackOverflow Article](https://stackoverflow.com/questions/51042871/how-to-access-url-kwargs-in-generic-api-views-listcreateapiview-to-be-more-spec).
- The fix for the Django Rest Framework bug that prevents user's cookies from being cleared on logout is from the Code Institute Django Rest Framework walkthrough project.
- The technique for overriding the `to_representation` method of a serializer to make a change to the outgoing JSON data used in `profiles/serializers.py` is from this [testdriven.io Tip](https://testdriven.io/tips/ed79fa08-6834-4827-b00d-2609205129e0/).
- The method to set up user authentication with JWT in Django Rest Framework is adapted from this [StackOverflow Article](https://stackoverflow.com/questions/44697872/django-rest-framework-jwt-user-login).
- The technique to handle file uploads in Django Rest Framework is from this [StackOverflow Article](https://stackoverflow.com/questions/45232352/file-upload-with-django-rest-framework).
- The method to test Django Rest Framework endpoints using the APIClient is adapted from this [Django Rest Framework Documentation](https://www.django-rest-framework.org/api-guide/testing/).

In addition, the following documentation was extensively referenced throughout development:

- [Django Documentation](https://www.djangoproject.com)
- [Django Rest Framework Documentation](https://www.django-rest-framework.org)
- [django-filter Documentation](https://django-filter.readthedocs.io/en/stable/)
- [django-recurrence Documentation](https://django-recurrence.readthedocs.io/en/latest/)
- [Python datetime Documentation](https://docs.python.org/3/library/datetime.html)
- [dateutil Documentation](https://dateutil.readthedocs.io/en/stable/index.html)
- [Django Rest Framework JWT Documentation](https://jpadilla.github.io/django-rest-framework-jwt/)

These resources provided invaluable insights and guidance, significantly contributing to the successful development of the Fit and Fine DRF API application.

### Media

The following sites were used to gather the photographic media used:
- [Freepik](https://www.freepik.com/)

## Acknowledgements

The development of Fit&Fine has been an exciting journey, and I am grateful for the inspiration, guidance, and resources that have contributed to the project. 

### Inspiration
- **Strava**: The idea for Fit&Fine was inspired by [Strava](https://www.strava.com/), a leading platform for fitness enthusiasts to track their activities, compete with others, and share their fitness journeys. Strava's robust features and community-centric approach motivated me to create a similar platform focused on comprehensive fitness tracking and community engagement.

### Project Guidance
**Moments DJANGO REST DRF API and Moments REACT Walkthrough Project** I utilized the Moments Walkthrough Project as a foundational guide. This project provided valuable insights into structuring the application, implementing various features, and ensuring a seamless user experience.
The Moments project had several ideas and functionalities similar to what I envisioned for Fit&Fine, which helped streamline my development process.


### Personal Thanks
- Many thanks to **my husband** for his incredible support and encouragement throughout this journey.
- My heartfelt gratitude to **my son**, who is 18 months old, for bringing joy and motivation into my life.
- Thanks to **Kristyna, Cohort facilitator** at Code Institute, for always being there to provide all the information needed and for keeping the positive energy up.
- Thanks to  my Code Institute **mentor** and my **fellow students** for constantly inspiring me on Slack and being there for each other to help in times of trouble.