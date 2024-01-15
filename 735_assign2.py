import mysql.connector
import pandas as pd
import os


def mysql_connect():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root123',
        database='dbms_lab_iiit'
    )

    return mydb


def db_initialize():
    tables = ['DEPARTMENT', 'EMPLOYEE', 'DEPT_LOCATIONS', 'PROJECT', 'WORKS_ON', 'DEPENDENT']

    if os.path.exists('emp_data.txt'):
        employee_data = []
        data = pd.read_csv('emp_data.txt', skipinitialspace=True)
        data.columns = data.columns.str.replace(' ', '')
        data['SALARY'] = pd.to_numeric(data['SALARY'])
        data['DNO'] = pd.to_numeric(data['DNO'])
        for idx, row in data.iterrows():
            employee_data.append(list(row.values))
    else:
        employee_data = [   # EMPLOYEE (FNAME, MINIT, LNAME, SSN, BDATE, ADDRESS, SEX, SALARY, SUPERSSN, DNO)
            ["Aarav", "K", "Sharma", "123-45-6789", "1992-05-15", "456 Rajpath, Delhi", "M", 60000, "987-65-4321", 4],
            ["Ananya", "R", "Kapoor", "234-56-7890", "1988-08-21", "789 MG Road, Mumbai", "F", 75000, "876-54-3210", 2],
            ["Siddharth", "S", "Verma", "345-67-8901", "1985-02-12", "234 Cantonment, Bangalore", "M", 80000, "765-43-2109", 1],
            ["Kriti", "P", "Naidu", "456-78-9012", "1996-11-30", "567 Brigade Road, Kolkata", "F", 55000, "654-32-1098", 2],
            ["Arjun", "V", "Pillai", "567-89-0123", "1990-07-04", "890 Whitefield, Bangalore", "M", 35000, "543-21-0987", 3],
            ["Saanvi", "A", "Reddy", "678-90-1234", "1993-09-18", "123 Koramangala, Bangalore", "F", 25000, "432-10-9876", 3],
            ["Aditya", "K", "Iyer", "789-01-2345", "1984-04-25", "456 Anna Salai, Chennai", "M", 29000, "321-09-8765", 1],
            ["Isha", "R", "Nair", "890-12-3456", "1997-06-08", "789 T Nagar, Chennai", "F", 70000, "210-98-7654", 5],
            ["Rohan", "S", "Menon", "901-23-4567", "1989-03-17", "890 Race Course Road, Indore", "M", 80000, "109-87-6543", 5],
            ["Niharika", "P", "Khanna", "012-34-5678", "1994-01-02", "234 Malabar Hill, Mumbai", "F", 60000, "098-76-5432", 6],
            ["Kabir", "V", "Rajput", "123-45-6780", "1983-10-05", "567 Juhu, Mumbai", "M", 65000, "987-65-4320", 2],
            ["Diya", "S", "Deshmukh", "234-56-7891", "1996-12-20", "890 Kalyani Nagar, Pune", "F", 28000, "876-54-3219", 2],
            ["Advait", "K", "Banerjee", "345-67-8902", "1987-08-15", "123 Aundh, Pune", "M", 55000, "765-43-2108", 6],
            ["Amara", "A", "Joshi", "456-78-9013", "1992-04-10", "456 Wakad, Pune", "F", 75000, "654-32-1097", 4],
            ["Rishabh", "V", "Singh", "567-89-0124", "1986-07-23", "789 Hadapsar, Pune", "M", 60000, "543-21-0986", 5],
            ["Aanya", "P", "Patel", "678-90-1235", "1990-09-05", "234 Patel Chowk, Delhi", "F", 55000, "432-10-9875", 1],
            ["Arnav", "K", "Mishra", "789-01-2346", "1981-02-28", "567 C.G. Road, Ahmedabad", "M", 26000, "321-09-8764", 6],
            ["Anvi", "R", "Chatterjee", "890-12-3457", "1993-06-14", "890 S.G. Highway, Ahmedabad", "F", 75000, "210-98-7653", 6],
            ["Vihaan", "S", "Reddy", "901-23-4568", "1984-11-27", "123 Begumpet, Hyderabad", "M", 30000, "109-87-6542", 4],
            ["Myra", "A", "Kumar", "012-34-5679", "1997-03-03", "456 Jubilee Hills, Hyderabad", "F", 65000, "098-76-5431", 3],
        ]

    if os.path.exists('dept_data.txt'):
        department_data = []
        data = pd.read_csv('dept_data.txt', skipinitialspace=True)
        data.columns = data.columns.str.replace(' ', '')
        data['DNUMBER'] = pd.to_numeric(data['DNUMBER'])
        for idx, row in data.iterrows():
            department_data.append(list(row.values))
    else:
        department_data = [   # DEPARTMENT (DNAME, DNUMBER, MGRSSN, MGRSTARTDATE)
            ["Human Resources", 1, "321-09-8765", "2005-03-15"],
            ["Finance", 2, "876-54-3210", "2008-06-20"],
            ["IT", 3, "098-76-5431", "2016-02-01"],
            ["Marketing", 4, "654-32-1098", "2007-09-10"],
            ["Operations", 5, "543-21-0987", "2012-04-05"],
            ["Research", 6, "432-10-9876", "2014-11-22"],
        ]

    if os.path.exists('deptloc_data.txt'):
        dept_locations_data = []
        data = pd.read_csv('deptloc_data.txt', skipinitialspace=True)
        data.columns = data.columns.str.replace(' ', '')
        data['DNUMBER'] = pd.to_numeric(data['DNUMBER'])
        for idx, row in data.iterrows():
            dept_locations_data.append(list(row.values))
    else:
        dept_locations_data = [   # DEPT_LOCATIONS (DNUMBER, DLOCATION)
            [1, "Mumbai"],
            [2, "Delhi"],
            [3, "Bangalore"],
            [4, "Kolkata"],
            [5, "Hyderabad"],
            [6, "Chennai"],
        ]

    if os.path.exists('project_data.txt'):
        project_data = []
        data = pd.read_csv('project_data.txt', skipinitialspace=True)
        data.columns = data.columns.str.replace(' ', '')
        data['DNUM'] = pd.to_numeric(data['DNUM'])
        for idx, row in data.iterrows():
            project_data.append(list(row.values))
    else:
        project_data = [   # PROJECT (PNAME, PNUMBER, PLOCATION, DNUM)
            ["Space Exploration", 'P-01', "Bengaluru", 6],
            ["Ganges Revival", 'P-02', "Varanasi", 2],
            ["Silicon Valley", 'P-03', "Bengaluru", 3],
            ["Taj Mahal Restoration", 'P-04', "Agra", 1],
            ["Project Everest", 'P-05', "Leh", 2],
            ["Tech Innovation", 'P-06', "Hyderabad", 6],
            ["Artificial Intelligence Project", 'P-07', "Bengaluru", 3],
            ["Smart City Development", 'P-08', "Kolkata", 2],
            ["Historical Monument Preservation", 'P-09', "Kolkata", 1],
            ["Green Energy Initiative", 'P-10', "Kolkata", 2],
            ["Cultural Exchange Program", 'P-11', "Kolkata", 4],
            ["Fashion Show", 'P-12', "Mumbai", 5],
            ["Project Himalaya", 'P-13', "Shimla", 1]
        ]

    if os.path.exists('works.txt'):
        works_on_data = []
        data = pd.read_csv('works.txt', skipinitialspace=True)
        data.columns = data.columns.str.replace(' ', '')
        data['HOURS'] = pd.to_numeric(data['HOURS'])
        for idx, row in data.iterrows():
            works_on_data.append(list(row.values))
    else:
        works_on_data = [   # WORKS_ON (ESSN, PNO, HOURS)
            ["123-45-6789", 'P-01', 40],
            ["234-56-7890", 'P-02', 30],
            ["345-67-8901", 'P-03', 45],
            ["456-78-9012", 'P-01', 35],
            ["567-89-0123", 'P-02', 25],
            ["678-90-1234", 'P-04', 40],
            ["789-01-2345", 'P-03', 20],
            ["890-12-3456", 'P-01', 30],
            ["901-23-4567", 'P-02', 35],
            ["012-34-5678", 'P-03', 40],
            ["123-45-6780", 'P-04', 25],
            ["234-56-7891", 'P-04', 30],
            ["345-67-8902", 'P-01', 38],
            ["456-78-9013", 'P-02', 28],
            ["567-89-0124", 'P-03', 42],
            ["678-90-1235", 'P-04', 22],
            ["789-01-2346", 'P-03', 33],
            ["890-12-3457", 'P-01', 36],
            ["901-23-4568", 'P-02', 26],
            ["012-34-5679", 'P-03', 38],
        ]

    if os.path.exists('dependent_data.txt'):
        dependent_data = []
        data = pd.read_csv('dependent_data.txt', skipinitialspace=True)
        data.columns = data.columns.str.replace(' ', '')
        for idx, row in data.iterrows():
            dependent_data.append(list(row.values))
    else:
        dependent_data = [   # DEPENDENT (ESSN, DEPENDENT_NAME, SEX, BDATE, RELATIONSHIP)
            ["123-45-6789", "Aaradhya Sharma", "F", "2000-08-15", "Daughter"],
            ["234-56-7890", "Arjun Kapoor", "M", "1998-05-20", "Son"],
            ["456-78-9012", "Aryan Naidu", "M", "2010-11-30", "Son"],
            ["567-89-0123", "Ananya Pillai", "F", "1995-07-04", "Daughter"],
            ["678-90-1234", "Rohan Reddy", "M", "2002-09-18", "Son"],
            ["789-01-2345", "Kavya Iyer", "F", "2008-04-05", "Daughter"],
            ["123-45-6780", "Nia Rajput", "F", "2003-03-10", "Daughter"],
            ["234-56-7891", "Yuvan Deshmukh", "M", "2012-08-25", "Son"],
            ["345-67-8902", "Kiara Banerjee", "F", "2010-01-28", "Daughter"],
            ["456-78-9013", "Advait Joshi", "M", "2009-04-14", "Son"],
            ["567-89-0124", "Aisha Singh", "F", "2015-09-07", "Daughter"],
            ["678-90-1235", "Vihaan Patel", "M", "2011-11-02", "Son"],
            ["890-12-3457", "Kian Chatterjee", "M", "2001-02-08", "Son"],
            ["901-23-4568", "Aarohi Reddy", "F", "2013-05-13", "Daughter"],
            ["012-34-5679", "Kabir Kumar", "M", "2008-12-26", "Son"],
        ]

    for t in tables[::-1]:
        try:
            cursor.execute(f'DROP TABLE {t};')
            conn.commit()
        except Exception as err:
            # print(f'Error {err}!')
            pass

    sql_querries = [
        '''CREATE TABLE DEPARTMENT(
                DNAME VARCHAR(50),
                DNUMBER INT PRIMARY KEY,
                MGR_SSN VARCHAR(50),
                MGR_START_DATE DATE
        );''',
        '''CREATE TABLE EMPLOYEE(
                FNAME VARCHAR(50),
                MINIT VARCHAR(50),
                LNAME VARCHAR(50),
                SSN VARCHAR(50) PRIMARY KEY,
                BDATE DATE,
                ADDRESS VARCHAR(50),
                SEX CHAR(1),
                SALARY INT,
                SUPER_SSN VARCHAR(50),
                DNO INT,

                FOREIGN KEY (DNO)
                REFERENCES DEPARTMENT(DNUMBER)
                ON DELETE CASCADE
        );''',
        '''CREATE TABLE DEPT_LOCATIONS(
                DNUMBER INT PRIMARY KEY,
                DLOCATION VARCHAR(50),

                FOREIGN KEY (DNUMBER)
                REFERENCES DEPARTMENT(DNUMBER)
                ON DELETE CASCADE
        );''',
        '''CREATE TABLE PROJECT(
                PNAME VARCHAR(50),
                PNUMBER VARCHAR(10)  PRIMARY KEY,
                PLOCATION VARCHAR(50),
                DNUM INT,
                
                FOREIGN KEY (DNUM)
                REFERENCES DEPARTMENT(DNUMBER)
                ON DELETE CASCADE
        );''',
        '''CREATE TABLE WORKS_ON(
                ESSN VARCHAR(50) PRIMARY KEY,
                PNO VARCHAR(10),
                HOURS INT,

                FOREIGN KEY (ESSN)
                REFERENCES EMPLOYEE(SSN)
                ON DELETE CASCADE,
                FOREIGN KEY (PNO)
                REFERENCES PROJECT(PNUMBER)
                ON DELETE CASCADE
        );''',
        '''CREATE TABLE DEPENDENT(
                ESSN VARCHAR(50) PRIMARY KEY,
                DEPENDENT_NAME VARCHAR(50),
                SEX CHAR(1),
                BDATE DATE,
                RELATIONSHIP VARCHAR(50),

                FOREIGN KEY (ESSN)
                REFERENCES EMPLOYEE(SSN)
                ON DELETE CASCADE
        );'''
    ]
    for t in range(len(sql_querries)):
        cursor.execute(sql_querries[t])

    in_dept_query = 'INSERT INTO DEPARTMENT VALUES(%s, %s, %s, %s);'
    in_emp_query = 'INSERT INTO EMPLOYEE VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
    in_deptloc_query = 'INSERT INTO DEPT_LOCATIONS VALUES(%s, %s);'
    in_proj_query = 'INSERT INTO PROJECT VALUES(%s, %s, %s, %s);'
    in_workson_query = 'INSERT INTO WORKS_ON VALUES(%s, %s, %s);'
    in_depend_query = 'INSERT INTO DEPENDENT VALUES(%s, %s, %s, %s, %s);'
    cursor.executemany(in_dept_query, department_data)
    cursor.executemany(in_emp_query, employee_data)
    cursor.executemany(in_deptloc_query, dept_locations_data)
    cursor.executemany(in_proj_query, project_data)
    cursor.executemany(in_workson_query, works_on_data)
    cursor.executemany(in_depend_query, dependent_data)
    conn.commit()


def db_close():
    conn.commit()
    conn.close()


def display(res):
    if not res: return
    widths = []
    columns = []
    tavnit = '|'
    separator = '+' 

    for index, cd in enumerate(cursor.description):
        max_col_length = max(list(map(lambda x: len(str(x[index])), res)))
        widths.append(max(max_col_length, len(cd[0])))
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in res:
        print(tavnit % row)
    print(separator)



conn = mysql_connect()
cursor = conn.cursor()

db_initialize()

print('\n1. Display all employees (Fname, Lname) whose salary is in between 20K and 30K.')
sql_cmd = 'SELECT FNAME, LNAME FROM EMPLOYEE WHERE Salary BETWEEN 20000 AND 30000;'
print(f'SQL QUERY : {sql_cmd}')
print('RESULT:')
cursor.execute(sql_cmd)
display(cursor.fetchall())

print('\n2. Display all employees (Fname, Lname) whose salary is in between 20K and 30K and works in the department “Research”.')
sql_cmd = 'SELECT FNAME, LNAME FROM EMPLOYEE, DEPARTMENT WHERE (DNAME = "Research") AND (DNUMBER = DNO) AND (Salary BETWEEN 20000 AND 30000);'
print(f'SQL QUERY : {sql_cmd}')
print('RESULT:')
cursor.execute(sql_cmd)
display(cursor.fetchall())

print('\n3. Display all employee names who are from DELHI and their department location is KOLKATA.')
sql_cmd = 'SELECT FNAME, LNAME FROM EMPLOYEE, DEPT_LOCATIONS WHERE (DLOCATION = "Kolkata") AND (DNUMBER = DNO) AND (ADDRESS LIKE "%Delhi%");'
print(f'SQL QUERY : {sql_cmd}')
print('RESULT:')
cursor.execute(sql_cmd)
display(cursor.fetchall())

print('\n4. Which employees are working in department “Research” and project number “P-01”.')
sql_cmd = 'SELECT FNAME, LNAME FROM EMPLOYEE, DEPARTMENT, PROJECT WHERE (DNAME = "Research") AND (DNUMBER = DNO) AND (PNUMBER = "P-01") AND (DNUM = DNUMBER);'
print(f'SQL QUERY : {sql_cmd}')
print('RESULT:')
cursor.execute(sql_cmd)
display(cursor.fetchall())

print('\n5. Display list of employees who are either from DELHI or working in a department located at DELHI.')
sql_cmd = 'SELECT FNAME, LNAME FROM EMPLOYEE, DEPT_LOCATIONS WHERE (DNUMBER = DNO) AND ((DLOCATION = "Delhi") OR (ADDRESS LIKE "%Delhi%"));'
print(f'SQL QUERY : {sql_cmd}')
print('RESULT:')
cursor.execute(sql_cmd)
display(cursor.fetchall())

print('\n6. Count number of employees working in department “Research”.')
sql_cmd = 'SELECT COUNT(*) AS "Employess in Research Dept" FROM EMPLOYEE, DEPARTMENT WHERE (DNUMBER = DNO) AND (DNAME = "Research");'
print(f'SQL QUERY : {sql_cmd}')
print('RESULT:')
cursor.execute(sql_cmd)
display(cursor.fetchall())

print('\n7. Display all employee names who have no dependent.')
sql_cmd = 'SELECT FNAME, LNAME FROM EMPLOYEE WHERE NOT EXISTS (SELECT * FROM DEPENDENT WHERE SSN = ESSN);'
print(f'SQL QUERY : {sql_cmd}')
print('RESULT:')
cursor.execute(sql_cmd)
display(cursor.fetchall())

print('\n8. Display all employee names from department “Research” who have no dependent or have all dependents born after 01/01/2010.')
sql_cmd = 'SELECT FNAME, LNAME FROM EMPLOYEE, DEPARTMENT WHERE (DNAME = "Research") AND (DNUMBER = DNO) AND ((SSN NOT IN (SELECT SSN FROM EMPLOYEE, DEPENDENT WHERE (SSN = ESSN))) OR (SSN IN (SELECT SSN FROM EMPLOYEE, DEPENDENT WHERE (SSN = ESSN) AND DEPENDENT.BDATE > "2010-01-01")));'
print(f'SQL QUERY : {sql_cmd}')
print('RESULT:')
cursor.execute(sql_cmd)
display(cursor.fetchall())

print('\n9. What is the average salary of employees in “Research” department.')
sql_cmd = 'SELECT ROUND(AVG(SALARY), 2) AS "Average Salary of Emp in Research" FROM EMPLOYEE, DEPARTMENT WHERE (DNAME = "Research") AND (DNUMBER = DNO);'
print(f'SQL QUERY : {sql_cmd}')
print('RESULT:')
cursor.execute(sql_cmd)
display(cursor.fetchall())

print('\n10. How many employees are there in the organization who are working as managers and have started the managerial job after 01/01/2016.')
sql_cmd = 'SELECT COUNT(*) AS "No. of Emp in Managerial Role" FROM EMPLOYEE, DEPARTMENT WHERE (DNUMBER = DNO) AND (SUPER_SSN = MGR_SSN) AND (MGR_START_DATE > "2016-01-01");'
print(f'SQL QUERY : {sql_cmd}')
print('RESULT:')
cursor.execute(sql_cmd)
display(cursor.fetchall())

print()
db_close()