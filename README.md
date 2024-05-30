# Furrbook - API

## Project description
Furrbook is a social media platform all about showing off your furry friends. It has been designed for its users to share their pets' most interesting, funny and beautiful moments. The application consists of the React app and an API. Welcome to the Django Rest Framework API project section.

[Furrbook - API live site](https://drf-api-ach-34946935b146.herokuapp.com/)

## Features

### User stories
|    as   |            I want to           |                                           so that I can                                          |                                mapping API feature                                |
|:-------:|:------------------------------:|:------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| user    | register for an account        | have a personal profile with a picture                                                           | dj-rest-auth<br>Create profile (signals)                                          |
| user    | register for an account        | create, like and comment on posts                                                                | Create post<br>Create comment<br>Create like<br>Create dislike<br>Create bookmark |
| user    | register for an account        | follow users                                                                                     | Create follower                                                                   |
| visitor | view a list of posts           | browse the most recent uploads                                                                   | List/ Filter posts                                                                |
| visitor | view an individual post        | see user feedback, i.e. likes and read comments                                                  | Retrieve post                                                                     |
| visitor | search a list of posts         | find a post by a specific artist or a title                                                      | List/ Filter posts                                                                |
| visitor | scroll through a list of posts | browse the site more comfortably                                                                 | List/ Filter posts                                                                |
| user    | edit and delete my post        | correct or hide any mistakes                                                                     | Update property<br>Destroy property                                               |
| user    | create a post                  | share my moments with others                                                                     | Create post                                                                       |
| user    | view liked posts               | go back often to my favourite posts                                                              | List/ Filter posts                                                                |
| user    | view followed users' posts     | keep up with my favourite users' moments                                                         | List/ Filter posts                                                                |
| user    | like a post                    | express my interest in someone's shared moment                                                   | Create like                                                                       |
| user    | unlike a post                  | express that my interest in someone's shared moment has faded away                               | Destroy like                                                                      |
| user    | dislike a post                 | express my disinterest in someone's shared moment                                                | Create dislike                                                                    |
| user    | undislike a post               | express that my disinterest in someone's shared moment has faded away                            | Destroy dislike                                                                   |
| user    | bookmark a post                | express my interest in saving someone's shared moment                                            | Create bookmark                                                                   |
| user    | unbookmark a post              | express that my interest in saving someone's shared moment has faded away                        | Destroy bookmark                                                                  |
| user    | create a comment               | share my thoughts on other people's content                                                      | Create comment                                                                    |
| user    | edit and delete my comment     | correct or hide any mistakes                                                                     | Update comment<br>Destroy comment                                                 |
| user    | view a profile                 | see a user's recent posts + post, followers, following count data                                | Retrieve profile<br>List/ filter posts                                            |
| user    | edit a profile                 | update my profile information                                                                    | Update profile                                                                    |
| user    | follow a profile               | express my interest in someone's content                                                         | Create follower                                                                   |
| user    | unfollow a profile             | express that my interest in someone's content has faded away and remove their posts from my feed | Destroy follower                                                                  |

### Content Management:
- Admin/Owner can manage all functions from the Django admin interface.

## Entity Relationship Diagram

![ERD](https://res.cloudinary.com/dgzf4ydy2/image/upload/v1717089653/ERD_vyo7zb.png)

## Models and CRUD breakdown

|   model   |           endpoints          |     create    | retrieve | update | delete |                       filter                       | text search |
|:---------:|:----------------------------:|:-------------:|:--------:|:------:|:------:|:--------------------------------------------------:|:-----------:|
| users     | users/<br>users/:id/         | yes           | yes      | yes    | no     | no                                                 | no          |
| profiles  | profiles/<br>profiles/:id/   | yes (signals) | yes      | yes    | no     | following<br>followed                              | name        |
| likes     | likes/<br>likes/:id/         | yes           | yes      | no     | yes    | no                                                 | no          |
| dislikes  | dislikes/<br>dislikes/:id/   | yes           | yes      | no     | yes    | no                                                 | no          |
| bookmarks | bookmarks/<br>bookmarks/:id/ | yes           | yes      | no     | yes    | no                                                 | no          |
| comments  | comments/<br>comments/:id/   | yes           | yes      | yes    | yes    | post                                               | no          |
| followers | followers/<br>followers/:id/ | yes           | yes      | no     | yes    | no                                                 | no          |
| posts     | posts/<br>posts/:id/         | yes           | yes      | yes    | yes    | profile<br>liked<br>disliked<br>bookmarked<br>feed | title       |

## Technologies Used
- Python, Django Framework

## Tests
**Automated Testing:** Unit tests were written to ensure core functionalities works as expected.
### Posts app:
    - logged out users can list posts
    - logged in users can create a post
    - logged out users can't create a post
    - logged out users can retrieve a post with a valid id
    - logged out users can't retrieve a post with an invalid id
    - logged in users can update a post they own
    - logged in users can't update a post they don't own

**Manual Testing:** Extensive manual testing involved clicking through all functionalities, verifying form submissions, and confirming page loads.
### All apps:
- logged out users can list posts, bookmarks, likes, comments, followers and profiles
- logged in users can create posts, bookmarks, likes, comments, followers and profiles
- logged out users can't create posts, bookmarks, likes, comments, followers and profiles
- logged out users can retrieve posts, bookmarks, likes, comments, followers and profiles with a valid id
- logged out users can't retrieve posts, bookmarks, likes, comments, followers and profiles with an invalid id
- logged in users can update posts, bookmarks, likes, comments, followers and profiles they own
- logged in users can't update posts, bookmarks, likes, comments, followers and profiles they don't own

**Pep8:** Too many files to upload but all the ones I edited came out with this:

![PEP8](https://res.cloudinary.com/dgzf4ydy2/image/upload/v1717104096/PEP8_qt8vgq.png)

## Project Setup and Configuration
This section details the steps taken to configure the project for deployment:

### Database Connection:

- Installed psycopg2 library to connect to the PostgreSQL database.
- Integrated dj-database-url to manage database URLs from environment variables.

### Authentication:

- Configured dj-rest-auth library to utilize JSON Web Tokens (JWTs) for authentication.

### Security:

- Defined allowed hosts in project settings to restrict access.
- Configured Cross-Origin Resource Sharing (CORS) using allowed_origins to control acceptable origins for API requests.

### API Response Format:

- Set the default renderer to JSON for a consistent API response format.

### Deployment

This project can be deployed on various cloud platforms. Here are generic instructions for deploying on Heroku:

1. **Heroku Setup:** Create a Heroku account and install the Heroku CLI following their instructions [Heroku Documentation Link](https://devcenter.heroku.com/).
2. **Git Integration:** Initialize a Git repository in your project directory and push your code to Heroku. Refer to the Heroku documentation for details [Heroku Git Deployment Guide](https://devcenter.heroku.com/articles/deploying-python).
3. **Requirements:** Create a `requirements.txt` file listing all your project dependencies. Heroku will install them automatically during deployment.
4. **Configuration:** Set environment variables for any sensitive information like database credentials. Heroku provides ways to manage these securely.
    - set the following environment variables:
       - CLIENT_ORIGIN
       - CLOUDINARY_URL
       - DATABASE_URL
       - DISABLE_COLLECTSTATIC
       - SECRET_KEY
5. **Procfile:** Create a `Procfile` file specifying the command to run your Django application. A simple example: `web: gunicorn myproject.wsgi:application --log-file -`.
6. **Deploy:** Once everything is set up, run `heroku deploy` to deploy your application to Heroku or log in to your Heroku Dashboard and manually Deploy Branch from the Deploy tab.

**Note:** These are general guidelines. Refer to Heroku's documentation for the latest and most accurate instructions.