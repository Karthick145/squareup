# Square API Example

A collection of command-line samples for the Square API.

### Setup

1. Download Square APIs Client Library for Python SDK:
    https://github.com/square/square-python-sdk.git

  or use pip:

  ```bash
  $ pip install squareup
  ```
  
2. Make sure you can import the client library:

  ```
  $ python
  >>> import square
  ```
  
3. Clone the repo and execute below command to add it to PYTHONPATH:

  ```bash
  $ git clone https://github.com/Karthick145/squareup.git
  $ cd squareup
  $ source system.conf
  ```

4. Make sure you can import the current package:

  ```python
  >>> import squareup
  ```

5. Execute any of the scripts to begin syncing payments:

  ```bash
  $ python sync_payments.py -m list_payments
  ```
  
6. The script will output:

  Pulls transaction information so for happened and dumps into ``data/payments/dump.json``
 
 
 
#### Note: Update your Sandbox or Production account credentials `config.ini`
