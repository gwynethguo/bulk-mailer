# Smart Mailer Backend

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
        "recipient_email": "gwyneth.guo@u.nus.edu",
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
    /tracking/pixel?email_id=94fce105-cf0a-400d-92ee-bf16f3a8066d&recipient_email=gwyneth.guo@u.nus.edu
    ```
- **Response**: Returns the pixel image that, when accessed, records an open event for the specified email.

### 4. Retrieve Opened Email Count for Each Mass Email Sent
- **Endpoint**: `GET /tracking/counter`
- **Description**: Retrieves the count of opened emails for each mass email campaign. This is helpful for assessing engagement.
- **Request Parameters**: None.
- **Response**: Returns a JSON object listing email IDs along with their respective open counts.
