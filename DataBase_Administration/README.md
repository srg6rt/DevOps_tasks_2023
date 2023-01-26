## Database Administration


### PART 1
1. DownloadMySQL server for your OS on VM.
2. Install MySQL server on VM.
3. Select a subject area and describe the database schema, (minimum 3 tables)
4. Create a database on the server through the console.
5. Fill in tables.
6. Construct and execute SELECT operator with WHERE, GROUP BY and ORDER BY.
7. Execute other different SQL queries DDL, DML, DCL.
8. Create a database of new users with different privileges. Connect to the databaseas a new user and verify that the privileges allow or deny certain actions.
9. Make a selection from the main table DB MySQL.

<img src="./docs/images/install_mysql.png" />


<em>Check install</em>

<img src="./docs/images/check_install.png" />

<em>Set password</em>

$ sudo mysql_secure_installation

<em>Set remote user for Mysql Workbench</em>

<img src="./docs/images/set_remote_user.png" />

<em>Allow remote connections</em>

<img src="./docs/images/allow_remote_connections.png" />

$ sudo mysql -u root -p

mysql> CREATE DATABAS testo_db;

mysql> USE testo_db;

mysql> CREATE TABLE pizza(yeast VARCHAR(50) NOT NULL, water INT NOT NULL, oil VARCHAR(50) NOT NULL, powder VARCHAR(50) NOT NULL);

mysql> CREATE TABLE donut(yeast VARCHAR(50) NOT NULL, sugar INT NOT NULL, salt INT NOT NULL, water INT NOT NULL, powder VARCHAR(50) NOT NULL);

mysql> CREATE TABLE pancake(eggs INT NOT NULL, sugar INT NOT NULL, salt INT NOT NULL, milk INT NOT NULL, powder VARCHAR(50) NOT NULL), oil VARCHAR(50) NOT NULL;
 
mysql> SHOW DATABASES;

<img src="./docs/images/show_databases.png" />

<img src="./docs/images/describe_tables.png" />

<em>Database schema in MySQL Workbench</em>

<img src="./docs/images/database_schema.png" />

<em>Fill tables</em>

mysql> INSERT INTO pizza VALUE("one tea spoon", 200, "one spoon", "500");

mysql> INSERT INTO pancake VALUE(2, 200, 1, 500, "one cup", "one spoon");

mysql> INSERT INTO donut VALUE("two eggs", 200, 1, 500, "one cup", "one spoon");

<img src="./docs/images/fill_tables.png" />

<em>WHERE, GROUP BY and ORDER BY</em>

<img src="./docs/images/select_where.png" />

<img src="./docs/images/select_group_by.png" />

<img src="./docs/images/select_order_by.png" />

<em> DDL - Data Definition Language example: </em>

<img src="./docs/images/DDL_example.png" />

<em> DML - Data Manipulation Language example: </em>

<img src="./docs/images/DML_example.png" />

<em> DCL - Data Control Language example: </em>

<img src="./docs/images/DCL_example.png" />

<em>Create a database of new users with different privileges. Connect to the databaseas a new user and verify that the privileges allow or deny certain actions.</em>

Create users.

<img src="./docs/images/create_users.png" />

Grants for users.

<img src="./docs/images/grants_for_users.png" />

Deny DELETE command for user test2.

<img src="./docs/images/deny_delete_for_test2_user.png" />

<em>Make a selection from the main table DB MySQL.</em>

<img src="./docs/images/select_from_main_db.png" />

### PART 2

<em>Backup database</em>

<img src="./docs/images/backup_database.png" />

<em>Delete the table</em>

<img src="./docs/images/delete_table.png" />

<em>Restore one table from backup</em>

<img src="./docs/images/restore_one_table_from_backup.png" />

<em>Transfer your local database to RDS AWS.</em>

<em>Create AWS Database</em>

<img src="./docs/images/create_aws_database.png" />

<em>Test connection to AWS Database</em>

<img src="./docs/images/MySQLWorkbench_test_connection.png" />

<em>Import local db to RDS AWS</em>

<img src="./docs/images/import_local_db_to_RDS AWS.png" />

<img src="./docs/images/local_db_in_AWS_DB.png" />

<em>Execute SELECT operator</em>

<img src="./docs/images/SELECT_in_AWS.png" />

<em>Create the dump</em> 

<img src="./docs/images/create_dump.png" />

### PART 3 – MongoDB

<em>Create a database. Use the use command to connect to a new database</em> 

<em>Create a collection. Use db.createCollection to create a collection</em>

<img src="./docs/images/create_mongo_db_and_collection.png" />

<em>Create some documents. Insert a couple of documents into collection</em>

<em>Use find() to list documentsout.</em>

<img src="./docs/images/mongodb_create_documents_find.png" />