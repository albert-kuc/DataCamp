"""
Ordering by Multiple Columns:

We can pass multiple arguments to the .order_by() method to order by multiple columns. In fact, we can also sort in
ascending or descending order for each individual column. Each column in the .order_by() method is fully sorted from
left to right. This means that the first column is completely sorted, and then within each matching group of values in
the first column, it's sorted by the next column in the .order_by() method. This process is repeated until all the
columns in the .order_by() are sorted.

Instructions:
*   Select all records of the state and age columns from the census table.
*   Use .order_by() to sort the output of the state column in ascending order and age in descending order. (NOTE: desc
    is already imported).
*   Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
*   Print the first 20 results.
"""

# Import create_engine, MetaData, Table, select
from sqlalchemy import create_engine, MetaData, Table, select
# Create an engine and connection that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///../_datasets/census.sqlite')
connection = engine.connect()
# Load MetaData()
metadata = MetaData()
# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)
# ********************************************

# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])
# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, census.columns.age.desc())
# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()
# Print the first 20 results
print(results[:20])
