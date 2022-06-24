import csv
import json
import sendmail
from datetime import datetime

with open('movimientos.csv') as file:

    csvreader = csv.DictReader(file)

    jsonData = []
    for row in csvreader:
        jsonData.append(row)

jsonString = json.dumps(jsonData, indent=4)

credit = 0.00
debit = 0.00
totalAmount = 0.00

for i in jsonData:
    totalAmount = float(totalAmount) + float(i['Amount'])
    if(i['Account'] == 'Credit'):
        credit = float(credit) + float(i['Amount'])
    elif(i['Account'] == 'Debit'):
        debit = float(debit) + float(i['Amount'])

jan = 0
feb = 0
mar = 0
apr = 0
may = 0
jun = 0
jul = 0
aug = 0
sep = 0
oct = 0
nov = 0
dec = 0


for m in jsonData:
    date = datetime.strptime(m['OperationDate'], '%d/%m/%y')
    if(date.month == 1):
        jan = jan + 1
    elif(date.month == 2):
        feb = feb + 1
    elif(date.month == 3):
        mar = mar + 1
    elif(date.month == 4):
        apr = apr + 1
    elif(date.month == 5):
        may = may + 1
    elif(date.month == 6):
        jun = jun + 1
    elif(date.month == 7):
        jul = jul + 1
    elif(date.month == 8):
        aug = aug + 1
    elif(date.month == 9):
        sep = sep + 1
    elif(date.month == 10):
        oct = oct + 1
    elif(date.month == 11):
        nov = nov + 1
    elif(date.month == 12):
        dec = dec + 1

html = """\
<html>
<body>
    <p><h2>Here's a quick summary of your expenses:</h2><br>
    <table style='border:1px solid'>
        <tr style='border:1px solid'>
            <th style='border:1px solid'>Credit Movements</th>
            <th style='border:1px solid'>Debit Movements</th>
            <th style='border:1px solid'>Total Amount</th>
        </tr>
            <tr style='border:1px solid'>
            <td style='border:1px solid'>$"""+str(credit)+""" MXN</td>
            <td style='border:1px solid'>$"""+str(debit)+""" MXN</td>
            <td style='border:1px solid'>$"""+str(totalAmount)+""" MXN</td>
        </tr>
    </table>
    </br>
    </br>
    <table style='border:1px solid'>
        <tr style='border:1px solid'>
            <th style='border:1px solid'>Jan Mov</th>
            <th style='border:1px solid'>Feb Mov</th>
            <th style='border:1px solid'>Mar Mov</th>
            <th style='border:1px solid'>Apr Mov</th>
            <th style='border:1px solid'>May Mov</th>
            <th style='border:1px solid'>Jun Mov</th>
            <th style='border:1px solid'>Jul Mov</th>
            <th style='border:1px solid'>Aug Mov</th>
            <th style='border:1px solid'>Sep Mov</th>
            <th style='border:1px solid'>Oct Mov</th>
            <th style='border:1px solid'>Nov Mov</th>
            <th style='border:1px solid'>Dec Mov</th>
        </tr>
            <tr style='border:1px solid'>
            <td style='border:1px solid'>"""+str(jan)+"""</td>
            <td style='border:1px solid'>"""+str(feb)+"""</td>
            <td style='border:1px solid'>"""+str(mar)+"""</td>
            <td style='border:1px solid'>"""+str(apr)+"""</td>
            <td style='border:1px solid'>"""+str(may)+"""</td>
            <td style='border:1px solid'>"""+str(jun)+"""</td>
            <td style='border:1px solid'>"""+str(jul)+"""</td>
            <td style='border:1px solid'>"""+str(aug)+"""</td>
            <td style='border:1px solid'>"""+str(sep)+"""</td>
            <td style='border:1px solid'>"""+str(oct)+"""</td>
            <td style='border:1px solid'>"""+str(nov)+"""</td>
            <td style='border:1px solid'>"""+str(dec)+"""</td>
        </tr>
    </table>
    </p>
</body>
</html>
"""

sendmail.SendEmail(html)

file.close()