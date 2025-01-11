Task Management API Project:
Task management system involve helping users organize, prioritize, and track their daily tasks. This project will allow operations for creating, updating, deleting, and marking tasks as complete or incomplete.

Project Objective:

User Authentication:

register user:Allows new users to register with a username, email, and password.
retrieve user: provide list of user.
Log in a user: uthenticates a user and returns a token

Task Management:

Create Tasks:Users can create tasks with details like title, description, due date, and priority.
Update Tasks: user can update task like title, due date, priority.
Delete Tasks:  Permanently remove tasks.
Ready Tasks: allow user to retrieve a list of task, with option to filter by title or status

Task Status Management:
Mark tasks as complete or incomplete. created endpoint that allow user to mark tasks as complete or incomplete, once marked ad complete with provide you with timestamp(complete_at).

Task History:
Store task history to allow users to track completed tasks over time and retrieve a list of completed tasks.

Authentication and Permision:
rest_framework.permissions.IsAuthenticated: restricts access to views or endpoints only to authenticated users.
'rest_framework.authentication.TokenAuthentication',: unique token is generated for a user when they log in, token acts as a stand-in for the user's credentials.
