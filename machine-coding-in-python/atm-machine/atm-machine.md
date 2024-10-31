# ATM Machine

## Requirements
- User should be able to authenticate using card and pincode
- User should be able to perform actions like see balance, 
withdraw balance, deposit cash
- machine should interact with bank to get the data


## Entities/ dbschema
```sql
CREATE TABLE Bank (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Branch (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address_id INT REFERENCES Address(id),
    bank_id INT REFERENCES Bank(id),
    ifsc_code VARCHAR(11) UNIQUE NOT NULL,
    manager_id INT REFERENCES User(id) -- References User if manager is a user
);

CREATE TABLE Address (
    id SERIAL PRIMARY KEY,
    street1 VARCHAR(255),
    street2 VARCHAR(255),
    city VARCHAR(100),
    pincode VARCHAR(10),
    country_id INT REFERENCES Country(id)
);

CREATE TABLE Country (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    code CHAR(2) -- e.g., 'IN' for India
);

CREATE TABLE User (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    address_id INT REFERENCES Address(id),
    pan_card VARCHAR(10) UNIQUE,
    aadhar_card VARCHAR(12) UNIQUE
);

CREATE TABLE Accounts (
    account_no VARCHAR(20) PRIMARY KEY, -- account_no as primary key
    user_id INT REFERENCES User(id),
    branch_id INT REFERENCES Branch(id),
    balance DECIMAL(15, 2) DEFAULT 0,
    type VARCHAR(20) -- e.g., ENUM for 'savings', 'checking'
);

CREATE TABLE Debit_Cards (
    card_no VARCHAR(16) PRIMARY KEY,
    user_name VARCHAR(100),
    cvv CHAR(3),
    expire_at DATE,
    type VARCHAR(20), -- e.g., ENUM for 'debit', 'credit'
    account_no_id VARCHAR(20) REFERENCES Accounts(account_no),
    status VARCHAR(10) -- e.g., ENUM for 'active', 'blocked'
);

CREATE TABLE ATM (
    id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES Bank(id),
    total_amount DECIMAL(15, 2) DEFAULT 0,
    no_of_100_notes INT DEFAULT 0,
    no_of_200_notes INT DEFAULT 0,
    no_of_500_notes INT DEFAULT 0
);

CREATE TABLE ATM_Transactions (
    id SERIAL PRIMARY KEY,
    card_no VARCHAR(16) REFERENCES Debit_Cards(card_no),
    total_amount DECIMAL(15, 2),
    atm_id INT REFERENCES ATM(id)
);

```

## APIs
```json
// authenticate user
POST: api/v1/auth/user
body {
    "account_no":"9980890",
    "pin": "1234"
}
response {
    "status": "success",
    "token": "jwt_token" 
}

// get balance
GET /api/v1/accounts/balance
header Authorization: Bearer jwt_token
response{
    "status": "success",
    "balance": 2500.00
}

// deposite balance
POST /api/v1/accounts/deposit
body {
    "amount": 1000.00
}

response {
    "status": "success",
    "total_amount": 1200
}

// withdraw
POST /api/v1/accounts/withdraw 
header Authorization: Bearer JWT_TOKEN
body {
    "amount": 500
}

response {
    "status": "success",
    "total_amount": 700
}

// transactions
GET /api/v1/accounts/transactions
Authorization: Bearer jwt_token
reponse {
    "status": "success",
    "transactions": [
        {
            "id": 1,
            "type": "deposit",
            "amount": 1000.00,
            "date": "2024-10-28T12:34:56Z"
        },
        {
            "id": 2,
            "type": "withdrawal",
            "amount": 500.00,
            "date": "2024-10-29T14:20:00Z"
        }
    ]
}
// atm Transaction
POST /api/v1/atm/transaction
body {
    "card_no": "1234567890123456",
    "pin": "1234",
    "type": "withdrawal",  // or "balance"
    "amount": 100.00       // only if type is "withdrawal"
}
response {
    "status": "success",
    "balance": 3000.00
}


```