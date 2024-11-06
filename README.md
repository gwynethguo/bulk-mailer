# Smart Mailer Backend

## Architecture Diagram
![Architecture Diagram](https://github.com/user-attachments/assets/b137d9e4-1935-4e5a-877b-4d1a5130b326)
This backend is designed to be used with the CLI program available at [smart-mailer CLI program](https://github.com/cmang12/smart-mailer/tree/feat/use-api).

## Technology Stack
<img height="50" alt="Flask" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" />&nbsp;
<img height="50" alt="Supabase" src="https://github.com/user-attachments/assets/e40fc76b-c8d8-47c3-bb53-c7795abaf596" />&nbsp;
<img height="50" alt="Vercel" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vercel/vercel-original.svg" />&nbsp;
### Languages
Python
### Frameworks
Flask
### Libraries
#### Python Standard Libraries
[base64](https://docs.python.org/3/library/base64.html), [functools](https://docs.python.org/3/library/functools.html), [os](https://docs.python.org/3/library/os.html), [datetime](https://docs.python.org/3/library/datetime.html), [uuid](https://docs.python.org/3/library/uuid.html)
#### External Libraries
[flask](https://pypi.org/project/Flask/), [dotenv](https://pypi.org/project/python-dotenv/), [pydantic](https://pypi.org/project/pydantic/), [typing](https://pypi.org/project/typing/)
#### Tools & Deployment
[Vercel](https://vercel.com)

### Why Flask, Supabase, and Vercel?

#### **Fast Development & Deployment**
- **Flask**: Flask is a lightweight Python web framework that allows for quick backend development with minimal overhead. It’s perfect for building APIs and small-to-medium applications rapidly.
- **Supabase**: Supabase manages backend infrastructure, including authentication, database management, and real-time data sync, which reduces the need for manual setup.
- **Vercel**: Vercel offers serverless functions and requires minimal configuration, making deployments fast and seamless. Its automatic deployment from Git repositories ensures continuous integration without deployment issues.

#### **Scalability**
- Flask, Supabase, and Vercel are all scalable solutions. Flask allows for flexibility in adding additional routes and features, while Supabase’s PostgreSQL backend can handle growing data needs. Vercel scales automatically with traffic, making it ideal for applications with fluctuating demand.

#### **Cost-effective**
- Both **Supabase** and **Vercel** offer generous free tiers that provide access to a wide range of features without incurring additional costs. This makes them great choices for startups or small projects with limited budgets.

#### **Relational Data**
- Supabase is built on top of **PostgreSQL**, which is perfect for applications that require relational data management. This is especially useful for querying and analyzing email history analytics, ensuring that data relationships are well-structured and easy to access.


## API Endpoints
| HTTP Verb | Endpoint            | Action                                      |
| --------- | ------------------- | -------------------------------------------- |
| POST      | /email-history      | Create a record of a newly sent email        |
| GET       | /email-count-by-dept| Retrieve the count of sent emails by department |
| GET       | /tracking/pixel     | Retrieve the tracking pixel for email opens  |
| GET       | /tracking/counter   | Retrieve the open count for each mass email sent |

### 1. Create Sent Email Record
- **Endpoint**: `POST /email-history`
- **Description**: Creates a new record for a sent email, storing information about the recipient, department, and email details.
- **Request Body** (example):
    ```json
    {
        "email_id": "94fce105-cf0a-400d-92ee-bf16f3a8066d",
        "recipient_email": "johndoe@mail.com",
        "department_code": "ALL",
        "email_subject": "Greetings!"
    }
    ```
- **Response**: Returns a confirmation of the new email record, typically with a status indicating success or failure.

### 2. Retrieve Email Count by Department
- **Endpoint**: `GET /email-count-by-dept`
- **Description**: Retrieves the count of sent emails, categorized by department. Useful for monitoring email distribution across different departments.
- **Request Parameters**: None.
- **Response**: Returns a JSON object containing counts grouped by department code.

### 3. Retrieve Email Tracking Pixel
- **Endpoint**: `GET /tracking/pixel`
- **Description**: Provides a tracking pixel to be embedded in emails, allowing tracking of email opens.
- **Query Parameters**:
    - `email_id` (string): Unique identifier of the email to track.
    - `recipient_email` (string): Email address of the recipient.
- **Example**:
    ```
    /tracking/pixel?email_id=94fce105-cf0a-400d-92ee-bf16f3a8066d&recipient_email=johndoe@mail.com
    ```
- **Response**: Returns the pixel image that, when accessed, records an open event for the specified email.

### 4. Retrieve Opened Email Count for Each Mass Email Sent
- **Endpoint**: `GET /tracking/counter`
- **Description**: Retrieves the count of opened emails for each mass email campaign. This is helpful for assessing engagement.
- **Request Parameters**: None.
- **Response**: Returns a JSON object listing email IDs along with their respective open counts.

## Acknowledgements

### **Open-source Libraries and Tools**
- **Flask**: A lightweight web framework for Python, used to build the backend of this application. [Flask Documentation](https://flask.palletsprojects.com/)
- **Supabase**: A backend-as-a-service platform built on PostgreSQL, providing real-time data syncing and authentication. [Supabase Documentation](https://supabase.com/docs)
- **Vercel**: A platform for deployment with serverless functions and automatic Git integration, used for deploying the application. [Vercel Documentation](https://vercel.com/docs)
- **pydantic**: A data validation and parsing library used to enforce data structure integrity. [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- **dotenv**: Loads environment variables from a `.env` file to manage configuration securely. [python-dotenv Documentation](https://pypi.org/project/python-dotenv/)

### **Code Generation Tools**
- **OpenAI GPT**: Used to assist with generating boilerplate code and providing programming solutions. [OpenAI](https://openai.com/)

### **Contributions**
- Special thanks to the open-source community for providing free libraries and frameworks that helped in the development of this project. 
- Additional code snippets and guidance were provided by various StackOverflow threads, tutorials, and documentation that aided in troubleshooting and solving specific implementation challenges.
