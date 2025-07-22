# Developed simple Bank data application using python

## Project Overview

This project is a simple Python application for managing bank data. The application allows the user to:

* Add new bank records (name, account number, balance)
* Update existing records
* Delete bank records

This is a basic implementation for educational purposes, and the data is stored in memory (using a list of dictionaries) instead of a database.

## Features

* **Add Bank Record**: Adds a new bank record with account details (name, account number, balance).
* **Update Bank Record**: Allows updating of existing records by account number.
* **Delete Bank Record**: Deletes an existing bank record by account number.
* **View Bank Records**: Lists all current bank records stored.

## Requirements

* Python 3.6 or higher

## Project Setup

1. **Clone or Download the Repository**:

   ```bash
   git clone 
   https://github.com/nileshbaithwar/Bank_Account_System/edit/main/README.md
   ```

2. **Install Dependencies** (Optional - if you use additional libraries):

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Project**:

   ```bash
   python bank_data_manager.py
   ```

## File Structure

```
simple-bank-data-management/
├── bank_data_manager.py   # Main Python script for managing bank records
├── requirements.txt       # List of dependencies (if any)
└── README.md              # Project documentation
```

## Usage

### 1. Add Bank Record

To add a new bank record, input the following details:

* **Account Holder Name** (string)
* **Account Number** (string)
* **Balance** (float)

Example:

```python
add_bank_record('John Doe', '123456', 1500.50)
```

### 2. Update Bank Record

To update an existing bank record, input the **Account Number** and the new values for **Account Holder Name** and **Balance**.

Example:

```python
update_bank_record('123456', 'John Doe', 2000.00)
```

### 3. Delete Bank Record

To delete an existing bank record, input the **Account Number**.

Example:

```python
delete_bank_record('123456')
```

### 4. View Bank Records

To view all current bank records, simply call:

```python
view_bank_records()
```

## Example Code

```python
bank_data = []

def add_bank_record(name, account_number, balance):
    record = {'name': name, 'account_number': account_number, 'balance': balance}
    bank_data.append(record)
    print(f"Record added for {name}.")

def update_bank_record(account_number, new_name, new_balance):
    for record in bank_data:
        if record['account_number'] == account_number:
            record['name'] = new_name
            record['balance'] = new_balance
            print(f"Record updated for account number {account_number}.")
            return
    print("Account not found.")

def delete_bank_record(account_number):
    for record in bank_data:
        if record['account_number'] == account_number:
            bank_data.remove(record)
            print(f"Record deleted for account number {account_number}.")
            return
    print("Account not found.")

def view_bank_records():
    if not bank_data:
        print("No bank records available.")
    else:
        for record in bank_data:
            print(f"Name: {record['name']}, Account Number: {record['account_number']}, Balance: {record['balance']}")
```

## Example Interaction

```python
add_bank_record('Alice', '987654', 3000)
add_bank_record('Bob', '123456', 1500)
view_bank_records()

# Output:
# Name: Alice, Account Number: 987654, Balance: 3000
# Name: Bob, Account Number: 123456, Balance: 1500

update_bank_record('123456', 'Bob Martin', 1800)
view_bank_records()

# Output:
# Name: Alice, Account Number: 987654, Balance: 3000
# Name: Bob Martin, Account Number: 123456, Balance: 1800

delete_bank_record('987654')
view_bank_records()

# Output:
# Name: Bob Martin, Account Number: 123456, Balance: 1800
