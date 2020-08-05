import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='csv_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_table():

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "create TABLE application (id INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY, customerID VARCHAR(20), loanId VARCHAR(20), appilcationDate DATE, LoanNumber VARCHAR(20), LoanAmount INT(10),InterestRate DECIMAL(30,2), TermDays INT(10),repaymentDueDate DATE ,repaymentPaidDate DATE)";
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        

    finally:
        print("Successfully created Database..!!")
        # connection.close()

    return True


def add_datapoint(customerID, loanId, appilcationDate, LoanNumber, LoanAmount, InterestRate, TermDays, repaymentDueDate, repaymentPaidDate):
    
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO application (customerID, loanId , appilcationDate , LoanNumber , LoanAmount ,InterestRate , TermDays ,repaymentDueDate ,repaymentPaidDate) VALUES('{customerID}', '{loanId}' , '{appilcationDate}' , '{LoanNumber}' , {LoanAmount} ,{InterestRate} , {TermDays} ,'{repaymentDueDate}' ,'{repaymentPaidDate}');"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        pass
        # print("Successfully Added User..!!")
