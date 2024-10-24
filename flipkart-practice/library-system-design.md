# Library Management System Design

## 1. Requirements Gathering

### Functional Requirements
- Users should be able to search and browse books
- Users can check out and return books
- Librarians can add/remove/update books
- Users can reserve unavailable books
- System should track due dates and fines
- Users can review and rate books
- System should send notifications for due dates

### Non-Functional Requirements
- High availability (99.9%)
- Low latency for search (<200ms)
- Scalable to handle millions of books
- Secure user data
- Data consistency for transactions

## 2. Class Design

```python
from datetime import datetime
from enum import Enum
from typing import List, Optional

class BookStatus(Enum):
    AVAILABLE = "available"
    CHECKED_OUT = "checked_out"
    RESERVED = "reserved"
    LOST = "lost"

class UserRole(Enum):
    MEMBER = "member"
    LIBRARIAN = "librarian"
    ADMIN = "admin"

class User:
    def __init__(self, user_id: int, name: str, email: str, role: UserRole):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role
        self.membership_date = datetime.now()
        self.books_checked_out: List[BookCopy] = []
        self.fines_due: float = 0.0

class Book:
    def __init__(self, isbn: str, title: str, author: str, category: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.category = category
        self.publication_date = datetime.now()
        self.average_rating: float = 0.0
        self.total_copies: int = 0
        self.available_copies: int = 0

class BookCopy:
    def __init__(self, copy_id: int, book: Book):
        self.copy_id = copy_id
        self.book = book
        self.status = BookStatus.AVAILABLE
        self.condition = "Good"
        self.current_borrower: Optional[User] = None
        self.due_date: Optional[datetime] = None

class Reservation:
    def __init__(self, user: User, book: Book):
        self.reservation_id = id
        self.user = user
        self.book = book
        self.reservation_date = datetime.now()
        self.status = "Pending"

class Transaction:
    def __init__(self, user: User, book_copy: BookCopy):
        self.transaction_id = id
        self.user = user
        self.book_copy = book_copy
        self.checkout_date = datetime.now()
        self.due_date = datetime.now()  # + timedelta(days=14)
        self.return_date: Optional[datetime] = None
        self.fine_amount: float = 0.0

class Review:
    def __init__(self, user: User, book: Book, rating: int, comment: str):
        self.review_id = id
        self.user = user
        self.book = book
        self.rating = rating
        self.comment = comment
        self.review_date = datetime.now()
```

## 3. Database Schema

```sql
-- Users table
CREATE TABLE users (
    user_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(20) NOT NULL,
    membership_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fines_due DECIMAL(10,2) DEFAULT 0.00,
    CONSTRAINT valid_role CHECK (role IN ('member', 'librarian', 'admin'))
);

-- Books table
CREATE TABLE books (
    isbn VARCHAR(13) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    publication_date DATE,
    average_rating DECIMAL(3,2) DEFAULT 0.00,
    total_copies INT DEFAULT 0,
    available_copies INT DEFAULT 0
);

-- Book copies table
CREATE TABLE book_copies (
    copy_id BIGSERIAL PRIMARY KEY,
    isbn VARCHAR(13) REFERENCES books(isbn),
    status VARCHAR(20) DEFAULT 'available',
    condition VARCHAR(50) DEFAULT 'Good',
    current_borrower BIGINT REFERENCES users(user_id),
    due_date TIMESTAMP,
    CONSTRAINT valid_status CHECK (status IN ('available', 'checked_out', 'reserved', 'lost'))
);

-- Reservations table
CREATE TABLE reservations (
    reservation_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(user_id),
    isbn VARCHAR(13) REFERENCES books(isbn),
    reservation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'pending',
    CONSTRAINT valid_reservation_status CHECK (status IN ('pending', 'fulfilled', 'cancelled'))
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(user_id),
    copy_id BIGINT REFERENCES book_copies(copy_id),
    checkout_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    due_date TIMESTAMP NOT NULL,
    return_date TIMESTAMP,
    fine_amount DECIMAL(10,2) DEFAULT 0.00
);

-- Reviews table
CREATE TABLE reviews (
    review_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(user_id),
    isbn VARCHAR(13) REFERENCES books(isbn),
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_books_title ON books(title);
CREATE INDEX idx_books_author ON books(author);
CREATE INDEX idx_transactions_user ON transactions(user_id);
CREATE INDEX idx_book_copies_status ON book_copies(status);
```

## 4. API Contracts

### User Management
```
POST /api/users
Request:
{
    "name": string,
    "email": string,
    "password": string,
    "role": string
}
Response: 201 Created
{
    "user_id": integer,
    "name": string,
    "email": string,
    "role": string,
    "membership_date": timestamp
}

GET /api/users/{user_id}
Response: 200 OK
{
    "user_id": integer,
    "name": string,
    "email": string,
    "role": string,
    "books_checked_out": array,
    "fines_due": float
}
```

### Book Management
```
POST /api/books
Request:
{
    "isbn": string,
    "title": string,
    "author": string,
    "category": string,
    "total_copies": integer
}
Response: 201 Created
{
    "isbn": string,
    "title": string,
    "author": string,
    "category": string,
    "total_copies": integer,
    "available_copies": integer
}

GET /api/books?search={query}&category={category}
Response: 200 OK
{
    "books": [
        {
            "isbn": string,
            "title": string,
            "author": string,
            "category": string,
            "available_copies": integer,
            "average_rating": float
        }
    ],
    "total": integer,
    "page": integer
}
```

### Transactions
```
POST /api/transactions/checkout
Request:
{
    "user_id": integer,
    "copy_id": integer
}
Response: 201 Created
{
    "transaction_id": integer,
    "checkout_date": timestamp,
    "due_date": timestamp,
    "book": {
        "isbn": string,
        "title": string
    }
}

POST /api/transactions/return
Request:
{
    "transaction_id": integer
}
Response: 200 OK
{
    "transaction_id": integer,
    "return_date": timestamp,
    "fine_amount": float
}
```

### Reservations
```
POST /api/reservations
Request:
{
    "user_id": integer,
    "isbn": string
}
Response: 201 Created
{
    "reservation_id": integer,
    "reservation_date": timestamp,
    "status": string
}

GET /api/reservations/user/{user_id}
Response: 200 OK
{
    "reservations": [
        {
            "reservation_id": integer,
            "book": {
                "isbn": string,
                "title": string
            },
            "status": string,
            "reservation_date": timestamp
        }
    ]
}
```

## 5. Common Interview Questions & Answers

1. **How would you handle concurrent checkouts?**
   - Use database transactions with row-level locking
   - Implement optimistic locking using version numbers
   - Update available_copies atomically
   - Example:
   ```sql
   BEGIN TRANSACTION;
   UPDATE books 
   SET available_copies = available_copies - 1 
   WHERE isbn = ? AND available_copies > 0;
   -- If rows affected = 0, throw error
   COMMIT;
   ```

2. **How would you implement the search functionality?**
   - For basic search: Use database indexes on title and author
   - For advanced search: Implement Elasticsearch
   - Consider using trigram indexes for fuzzy matching
   - Cache frequent searches

3. **How would you handle overdue notifications?**
   - Use a message queue (e.g., RabbitMQ)
   - Schedule daily batch jobs to check due dates
   - Implement exponential backoff for reminders
   - Use email service with retry mechanism

4. **How would you scale the system?**
   - Implement caching using Redis
   - Use read replicas for search queries
   - Shard database by geographical location
   - Use CDN for static content

5. **How would you ensure data consistency?**
   - Use ACID compliant database
   - Implement compensating transactions
   - Use event sourcing for audit trail
   - Regular data reconciliation jobs

6. **How would you handle book recommendations?**
   - Use collaborative filtering
   - Analyze user borrowing patterns
   - Create category-based recommendations
   - Implement a recommendation cache

## 6. System Architecture Considerations

1. **Caching Strategy**
   - Cache book metadata
   - Cache user profiles
   - Cache search results
   - Use Redis with TTL

2. **Security**
   - Implement JWT authentication
   - Role-based access control
   - Input validation
   - Rate limiting

3. **Monitoring**
   - Track failed transactions
   - Monitor API latency
   - Alert on high error rates
   - Track system resources

4. **Data Backup**
   - Daily incremental backups
   - Weekly full backups
   - Point-in-time recovery
   - Geo-replicated storage
