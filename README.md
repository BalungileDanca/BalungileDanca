Task Management API Project:
Task management system involve helping users organize, prioritize, and track their daily tasks. This project will allow operations for creating, updating, deleting, and marking tasks as complete or incomplete.

Project Objective:

User Authentication:

register user:Allows new users to register with a username, email, and password.
POST:http://127.0.0.1:8000/api/user_management/users/register/
retrieve user: provide list of user.
GET:http://127.0.0.1:8000/api/user_management/users/
Log in a user: uthenticates a user and returns a token
POST:http://127.0.0.1:8000/api/user_management/users/login/ 
{
token <returns token>
}

Task Management:

Create Tasks:Users can create tasks with details like title, description, due date, and priority.
POST: http://127.0.0.1:8000/api/Task_API/tasks/create/
{
   
    "title": "Serailizers basic.",
    "description": "Introduction",
    "due_date": "2025-01-31",
    "priority_level": "Low",
    "user": 19
}

Response
{
    "id": 16,
    "title": "Serailizers basic.",
    "description": "Introduction",
    "due_date": "2025-01-31",
    "priority_level": "Low",
    "status": "Complete",
    "completed_at": null,
    "user": 19
}
Update Tasks: user can update task like title, due date, priority.
PUST: http://127.0.0.1:8000/api/Task_API/tasks/id/update
Delete Tasks:  Permanently remove tasks.
DELETE: http://127.0.0.1:8000/api/Task_API/tasks/id/delete
Ready Tasks: allow user to retrieve a list of task, with option to filter by title or status
GET: http://127.0.0.1:8000/api/Task_API/tasks/

Task Status Management:
Mark tasks as complete or incomplete. created endpoint that allow user to mark tasks as complete or incomplete, once marked ad complete with provide you with timestamp(complete_at).
PATCH: http://127.0.0.1:8000/api/Task_API/tasks/id/status/ 

Task History:
Store task history to allow users to track completed tasks over time and retrieve a list of completed tasks.
GET: http://127.0.0.1:8000/api/Task_API/tasks/completed/

Authentication and Permision:
rest_framework.permissions.IsAuthenticated: restricts access to views or endpoints only to authenticated users.
'rest_framework.authentication.TokenAuthentication',: unique token is generated for a user when they log in, token acts as a stand-in for the user's credentials.
