# API for coding interview

This is the demo application for evaluation in API implementation with Django REST Framework.  

Of the project goals, the following have been completed:
1. All models are completed to spec
2. JWT Authentication fully implemented
3. api/auth/login fully implemented
4. api/auth/groups fully implemented
5. api/users fully implemented with search and filter to spec

## Notes on "Production" environment
I wasn't certain quite how deeply to go into production mode.  In a "real" application, I'd probably run Nginx and gunicorn.  I'd also use a real database and possibly something like S3 to store my static files.  

As it is, with no particular specs on how the production environment is meant to be, I simply used Django's recommended DJANGO_SETTINGS_MODULE environment variable to determine which settings file to use.  In this assignment, there's little difference between the two.

"Real" production environments would also have much improved security, such as removing the secrets from the settings files and verifying we pass Django's deployment checklist.
 