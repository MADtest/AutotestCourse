# -*- coding: utf-8 -*-

a = """CREATE TABLE Employees (
  Id char(20),
  Nam_e varchar(36) NOT NULL,
  Salary int default NULL,
  Department_id varchar(255) default NULL
);


INSERT INTO Employees (Id,Nam_e,Salary,Department_id) VALUES ('EMP-1','2E2B00C9-4E66-C37E-D59B-CB5AAAD1A823','835','d13');
INSERT INTO Employees (Id,Nam_e,Salary,Department_id) VALUES ('EMP-2','32C1FBBF-789C-B92E-B470-53A6659F39CA','1576','d16');
INSERT INTO Employees (Id,Nam_e,Salary,Department_id) VALUES ('EMP-3','DE391BA6-C635-3F40-B3FF-BC2AE7735982','532','d15');
INSERT INTO Employees (Id,Nam_e,Salary,Department_id) VALUES ('EMP-4','FA1672E8-B996-0EF4-CAA1-E46B03D6E4C4','1425','d14');
INSERT INTO Employees (Id,Nam_e,Salary,Department_id) VALUES ('EMP-5','5FD5A4E1-AEF0-64AA-FFD1-0D9ABA2AC88A','553','d12');
INSERT INTO Employees (Id,Nam_e,Salary,Department_id) VALUES ('EMP-6','B128F74A-CB66-C978-B08A-A5408CA6901C','1701','d12');
INSERT INTO Employees (Id,Nam_e,Salary,Department_id) VALUES ('EMP-7','F89E96D3-5329-E034-52AB-B8BA7732BE1A','1492','d19');
INSERT INTO Employees (Id,Nam_e,Salary,Department_id) VALUES ('EMP-8','9FB83288-57F5-1AAB-125C-3E991FDCA72E','1067','d16');
INSERT INTO Employees (Id,Nam_e,Salary,Department_id) VALUES ('EMP-9','771717FC-A748-59A1-4103-2B22695302C7','516','d4');
INSERT INTO Employees (Id,Nam_e,Salary,Department_id) VALUES ('EMP-10','826971F2-698C-B2C8-CBBC-DD9E08FA9DD6','582','d19');"""



for i in range(100):
    # print 'CREATE DATABASE Study{};'.format(i)
    print 'Use Study{};'.format(i)
    print a

