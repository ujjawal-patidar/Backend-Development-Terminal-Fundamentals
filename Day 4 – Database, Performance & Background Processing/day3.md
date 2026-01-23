## Day 4 – Database, Performance & Background Processing

### Topics
- SQL vs NoSQL databases
- Schema design basics
- CRUD operations
- Indexing and query optimization
- Pagination and filtering
- Caching fundamentals (Redis concept)
- Background jobs and async tasks

### Hands-on
- Connect backend to database
- Build one CRUD API
- Implement basic caching logic

### Outcome
- Understanding of performance and scalability basics

---



## SQl VS NoSQL

SQL databases are primarily called Relational Databases (RDBMS).
whereas NoSQL databases are primarily called non-relational or distributed databases. 

### Relational Database Management Systems maintains data integrity by simulating the following features: 

*Entity Integrity*: No two records of the database table can be completely duplicate.
*Referential Integrity*: Only the rows of those tables can be deleted which are not used by other tables. Otherwise, it may lead to data inconsistency.
*User-defined Integrity*: Rules defined by the users based on confidentiality and access.
*Domain integrity*: The columns of the database tables are enclosed within some structured limits, based on default values, type of data or ranges.

###ACID: The "Reliability First" Model
ACID is a set of strict rules used by relational databases (like PostgreSQL and MySQL) to ensure that every transaction is absolutely reliable. It is the industry standard for financial systems where data corruption cannot be tolerated. 
**Atomicity ("All or Nothing")**: Every operation in a transaction is treated as a single unit. If any part of a multi-step request fails (e.g., deducting money from one bank account), the entire transaction is canceled (rolled back).
**Consistency**: The database only moves from one valid state to another, enforcing rules like "account balances cannot be negative". If a request violates a rule, it is rejected.
**Isolation**: Concurrent requests don't interfere with each other. Even if thousands of users are active, each request behaves as if it is the only one happening at that moment to prevent "dirty reads" or overlapping updates.
**Durability**: Once a transaction is confirmed, it is permanently saved to the disk and will survive a system crash or power outage. 

## BASE: The "Availability First" Model 
BASE is a more relaxed approach common in NoSQL databases (like Cassandra or DynamoDB). It prioritizes system uptime and speed over immediate, perfect accuracy. 
**Basically Available**: The system guarantees a response to every request, even if it means serving slightly outdated data or ignoring part of a request during a partial failure.
**Soft State**: The data is "fluid"; because it is replicated across many global servers, different users might see different versions of the same data for a brief period.
**Eventually Consistent**: While the system allows temporary mismatches (e.g., an Instagram "like" count not updating instantly for all followers), it guarantees that all copies of the data will eventually match once the updates finish propagating. 


## **1 line for 100 lines**
if you priorities you data intregity and consistency over faster read/write go with SQL, if no go with noSQL
if you will be changing you schema too much go with NoSQL 
if you want more horizontal scalling (more servers to handle multiple request) go with noSQl, else if you want vertical scaling (more hardware, CPU, memory) which ensure data consistency go with SQL
int noSQL you can easily increase the number of servers and each shrad will have it own primary writer but if you are increasing SQL servers the data will be sharded but there will be only one primary writer amoung all shard and rest will all reader (only one writer server rest all reader)

### CAP theorem in NOSQL
The **CAP theorem** in NoSQL states that a distributed data system can only provide two of three guarantees: Consistency (all nodes see the same data), Availability (every request gets a response), and Partition Tolerance (system works despite network failures). Because distributed systems must tolerate network partitions, they must choose between consistency and availability (CP or AP). 
Key Components of CAP:

Consistency (C): Every read receives the most recent write or an error.

Availability (A): Every request receives a (non-error) response, without the guarantee that it contains the most recent write.

Partition Tolerance (P): The system continues to operate despite arbitrary message loss or failure of part of the system. 

NoSQL Database Classifications based on CAP:

NoSQL databases generally prioritize Partition Tolerance (P) because they operate across distributed nodes. The trade-off is then between C and A. 

CP (Consistency + Partition Tolerance): The system prioritizes data consistency over availability during a network partition. Examples include MongoDB, HBase, Redis.

AP (Availability + Partition Tolerance): The system ensures all nodes are available for reads/writes, but some may return stale data, prioritizing uptime over immediate consistency. Examples include Cassandra, DynamoDB, CouchDB.

CA (Consistency + Availability): Theoretically possible, but not practical for distributed systems because they cannot handle network partitions, making this combination generally inapplicable to distributed NoSQL databases. 

Context in NoSQL:
While traditional SQL databases often prioritize strict consistency (ACID), NoSQL databases often favor the BASE model (Basically Available, Soft state, Eventual consistency) to achieve high availability and scalability. '



## Schema Design Basic
* A schema is a blueprint that defines how data is organized.
* Schema design is the process of planning this structure so that it supports efficient storage, retrieval, and integrity of data.




## **Indexing**
Indexing in a database is a data structure technique used to speed up data retrieval operations (SELECT queries) by reducing the number of disk accesses required

Rule of Thumb

Use indexes for: search-heavy, read-heavy columns, high-cardinality values, and frequent joins.

Avoid indexes for: write-heavy, low-selectivity, or rarely queried columns.






## Commands for setting up the project
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
uvicorn app:app --reload       ,for running server

And i have just runned a fastApi server in a virtual enviroment
