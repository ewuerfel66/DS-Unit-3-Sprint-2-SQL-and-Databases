import sqlite3

##############
### PART 2 ###
##############

# Make cursor & connection
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


# Make a function for queries
def query(string):
    curs.execute(string)

    

# What are the 10 most expensive items?
query("""SELECT ProductName, UnitPrice FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;""")

print('What are the 10 most expensive items?')
print('(Product, Unit Price)', curs.fetchall())
print('')


# Average age of employee at time of hiring
query("""SELECT AVG(HireDate - BirthDate) AS AvgHiringAge FROM Employee;""")

print('Average Hire Age:', curs.fetchall()[0])
print('')


# Average age of employee at time of hiring by City
query("""SELECT City, AVG(HireDate - BirthDate) AS AvgHiringAge FROM Employee
GROUP BY City
ORDER BY AvgHiringAge DESC;""")

print('Average age of employee at time of hiring by City')
print('(City, Average Hire Age)', curs.fetchall())
print('')


##############
### PART 3 ###
##############

# What are the 10 most expensive items and the supplier?
query("""SELECT CompanyName AS Supplier, ProductName, UnitPrice FROM Product, Supplier
WHERE Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;""")

print('What are the 10 most expensive items and the supplier?')
print('(Supplier, Product, Unit Price)', curs.fetchall())
print('')


# What is the largest category?
query("""SELECT CategoryName, MAX(Items) FROM
(SELECT Category.CategoryName, COUNT(Product.Id) AS Items
FROM Category, Product
WHERE Category.Id = Product.CategoryId
GROUP BY Category.Id);""")

print('Largest Category by Unique Items:')
print('(Category, Count of Items)', curs.fetchall())
print('')

query("""SELECT FirstName, LastName, MAX(Territories) FROM
(SELECT Employee.FirstName, Employee.LastName, COUNT(Territory.Id) AS Territories
FROM  Employee
JOIN EmployeeTerritory
JOIN Territory
WHERE Employee.Id = EmployeeTerritory.EmployeeId
AND EmployeeTerritory.TerritoryId = Territory.Id
GROUP BY Employee.Id);""")

print('Employee with most Territories:')
print('(First, Last, Territories)', curs.fetchall())