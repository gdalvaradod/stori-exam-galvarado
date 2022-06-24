# Geovany Alvarado
## _Stori Exam_

---------------------------------------------

Requierements for execution:

- Python3 (3.10.4)
- Visual Studio 


## Functions

- Get total amount per credit movements
- Get total amount per debit movements
- Get total amount (credit + debit)
- Get total movements per month
- Send summary by email

This solution contains 2 simple files: main.py and sendmail.py. The first one use a CSV file to get information about movements and expenses of an account (the information is dummy). The CSV file is a template. For this exercise its structure is required. Please, don't modify the headers into the file.

The second file receives a html structure (this contains a table with information) and prepare and email using the library smtplib. The sender, receiver and subject are hardcoded (just for this quick version). Using the html received, generate a payload which is attached in the body email.

The server used to send the email is the gmail server (smtp.gmail.com with port 465) and a generic account was created for this exercise (please, feel free to use or validate this account, but don't change the password).

After the execution, you'll receive an email with a quick summary of your expense. You can modify the records and amounts in the CSV file for test.

## How to execute

Before the execution, please, be sure that the CSV file is in the root folder.

For execution, go to main.py file, open a console (or powershell in Windows) and run the next command:

```sh
python3 main.py
```

This will send an email. If you cannot see the email, please, validate your spam folder. Sometime the first execution sends the email to spam.
