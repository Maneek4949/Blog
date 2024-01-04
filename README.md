# Blog App using Django, Bootstrap, and MySQL

## Overview
This project is a comprehensive blog application developed using Django, Bootstrap, and MySQL. The application allows users to sign up and log in, with email uniqueness enforced through AJAX calls. It incorporates a forgot password feature for added user convenience.

## Features

1. **User Authentication:**
   - Users can sign up and log in securely.
   - Email uniqueness is enforced through AJAX calls during the signup process.

2. **Password Recovery:**
   - Forgot password functionality ensures users can regain access to their accounts.

3. **Blog Categories:**
   - Users can create unique blog categories, with category uniqueness verified using AJAX calls.

4. **Blog Creation:**
   - Blogs include essential fields such as category, title, author, creation date, description (utilizing a rich text editor), and an image upload option.

5. **Blog Management:**
   - Users can edit their blogs, like, dislike, and comment on any blog (authentication required).
   - Blogs are initially private; users can choose to publish them, making them visible to all.

6. **Blog List and Detail Pages:**
   - Everyone can read blogs, and the application provides user-friendly blog list and detail pages.

7. **Blog Visibility Control:**
   - Users can enable or disable their blogs after publishing.
   - A publish button becomes available once a blog is ready for public viewing.

8. **Blog Deletion:**
   - Users have the option to delete their blogs when needed.

## Getting Started

To set up the project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/blog-app.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the MySQL database and update the database configurations in `settings.py`.

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

Access the application at [http://localhost:8000/](http://localhost:8000/) in your web browser.



Happy Blogging!
