# Linkedin

## Requirements
- User and recruiters should be able to register on the platform
- Recruiters can post jobs on the platform and users should be able to apply for those
- Users should have personal info, experiece, education and certification sections in the profile
- User and recruiters can have post and that post can have likes and comments(optional)

## Entities
- Company
    - name
    - email
    - description
    - Address

- Job
    - Title
    - Description
    - Company_id
    - recruiter_id(fk)

- User
    - id
    - name
    - email
    - phone
    - designation
    - current_company_id(fk)

- Skills
    - name
    - description
    - certificate_url

- Experience
    - User_id
    - title
    - company_id
    - to
    - from

- Application
    - job_id
    - user_id
    - current_ctc
    - expected_ctc
    - resume_url
    - status

- Relationships
    - a company has many users, and user belongs to company
    - a company has many jobs, and a job belongs to a company
    - a job has a recuiter through company's users
    - a job has many applications and an application belong to a job
    - a user can have many application and an application belongs to a job
    - A user can have many experience and an experience belongs to a user

    ```json
    // POST: api/v1/users/signup
    request = {
        "name": "name",
        "email": "email.com",
        "password": "hashed-password"
    }
    response = {
        "name":"name",
        "email":"email"
    }

    // POST: api/v1/users/login
    request = {
        "email": "email",
        "password": "password"
    }

    response = {
        "status": "success",
        "jwt-token": "jwt-token"
    }

    // GET: api/v1/users/:id
    Headers: jwt/session-token
    response = {
        "name": "name",
        "email": "email",
        "company": "company",
    }

    // GET: api/v1/users
    Headers: jwt/session-token
    response = {
        "users": [
            {"name": "name1","email": "email", "company": "company"}, ...
        ],
        "pagination": {
            "page_no": 1,
            "total": 100,
            "per_page": 10
        }
    }
    ```