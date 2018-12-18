"""
Ordering by a Single Column:
To sort the result output by a field, we use the .order_by() method. By default, the .order_by() method sorts from
lowest to highest on the supplied column. You just have to pass in the name of the column you want sorted to
.order_by().

In the video, for example, Jason used stmt.order_by(census.columns.state) to sort the result output by the state column.

Instructions:
*   Select all records of the state column from the census table. To do this, pass census.columns.state as a list to
    select().
*   Append an .order_by() to sort the result output by the state column.
*   Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
*   Print the first 10 rows of results.
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

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by the state column
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])
