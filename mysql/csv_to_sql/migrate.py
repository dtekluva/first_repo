import db

file_name = "application_data.csv"
file = open(file_name, 'r')

data = file.readlines()
print(data.pop(0))

for line in data:

    cols = line.split(',')
    
    (customerID,
    loanId,
    appilcationDate,
    LoanNumber,
    LoanAmount,
    InterestRate,
    TermDays,
    repaymentDueDate,
    repaymentPaidDate) = (cols[0],
                        cols[1],
                        cols[2].replace('\n', ''),
                        cols[3],
                        cols[4],
                        cols[5],
                        cols[6],
                        cols[7].replace('\n', ''),
                        cols[8].replace('\n', ''))

    
    db.add_datapoint(customerID,
                        loanId,
                        appilcationDate,
                        LoanNumber,
                        LoanAmount,
                        InterestRate,
                        TermDays,
                        repaymentDueDate,
                        repaymentPaidDate)