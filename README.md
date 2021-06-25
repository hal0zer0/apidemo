# API for coding interview

This is the demo application for evaluation in API implementation with Django REST Framework.  

Of the project goals, the following have been completed:
1. All models are completed to spec
2. JWT Authentication fully implemented
3. api/auth/login fully implemented
4. api/auth/groups fully implemented
5. api/users fully implemented with search and filter to spec
6. api/users/{id} returns user details
7. api/users PATCHing in progress


## Using this application
For development settings, set the environment variable 
`DJANGO_SETTINGS_MODULE=dev_settings`
Without that, it will default to production settings (see below)

I have included a Dockerfile for production, though there is currently very little difference in the setup (see below) as there was no specification for what prod should look like.
You can build the container with something like `docker build -t apiassignment:0.1 .` and run with `docker run -p 8000:8000 apiassignment:0.1`

You have multiple user choices for login, to confirm the permissions system
- **apiadmin@youmighthireme.com** is an Administrator with Good Inc
- **apiviewer@youmighthireme.com** is a Viewer with Good Inc
- **apiuser@youmighthireme.com** is a User with Good Inc
- **eviladmin@evilinc.com** is an Administrator with Evil Inc

All have pass of 'swordfish'

## Notes on "Production" environment
I wasn't certain quite how deeply to go into production mode.  In a "real" application, I'd probably run Nginx and gunicorn.  I'd also use a real database and possibly something like S3 to store my static files.  

As it is, with no particular specs on how the production environment is meant to be, I simply used Django's recommended DJANGO_SETTINGS_MODULE environment variable to determine which settings file to use.  In this assignment, there's little difference between the two.

"Real" production environments would also have much improved security, such as removing the secrets from the settings files and verifying we pass Django's deployment checklist.

## Known caveats & weak points
Working on this project has highlighted a few gaps for me, such as using Groups for API permissions management.  My prior projects of this type had simpler authorization needs, and I suspect I could use some more practice in this regard.  

Similarly, it seems my git-flow is a bit rusty as I encountered some versioning conflicts.  I'll be studying where I went wrong.  
