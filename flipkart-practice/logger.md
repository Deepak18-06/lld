API for Log Query:
GET /api/v1/logs: Fetch logs based on filters.
Request:
http
Copy code
GET /api/v1/logs?start_time=2024-10-01T00:00:00Z&end_time=2024-10-22T23:59:59Z&level=ERROR&source=auth-service
Response:
json
Copy code
[
  {
    "timestamp": "2024-10-22T10:00:00Z",
    "level": "ERROR",
    "message": "Service crashed",
    "source": "auth-service"
  },
  {
    "timestamp": "2024-10-22T11:00:00Z",
    "level": "ERROR",
    "message": "Database connection failed",
    "source": "auth-service"
  }
]
4. API Contracts
Log Submission API:
For applications to submit logs to the centralized logging system.

POST /api/v1/logs:
Request:
json
Copy code
{
  "timestamp": "2024-10-22T10:00:00Z",
  "level": "ERROR",
  "message": "Service crashed",
  "source": "auth-service"
}
Response:
json
Copy code
{
  "status": "success"
}
Log Query API:
To retrieve logs based on filters like time, level, and source.

GET /api/v1/logs:
Query Parameters: start_time, end_time, level, source
Response:
json
Copy code
[
  {
    "timestamp": "2024-10-22T10:00:00Z",
    "level": "ERROR",
    "message": "Service crashed",
    "source": "auth-service"
  }
]