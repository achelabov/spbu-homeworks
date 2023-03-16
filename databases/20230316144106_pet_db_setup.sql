-- +goose Up
-- +goose StatementBegin
SELECT 'up SQL query';
-- +goose StatementEnd
CREATE TABLE Person(
    Person_ID         INTEGER      NOT NULL,
    Last_Name	      VARCHAR(20)  NOT NULL,
    First_Name	      VARCHAR(20),
    Phone	      VARCHAR(15)  NOT NULL,
    Address	      VARCHAR(50)  NOT NULL,
CONSTRAINT Person_PK PRIMARY KEY (Person_ID)
)
;
CREATE TABLE Owner(
    Owner_ID                INTEGER         NOT NULL,
    Description	            VARCHAR(50),
    Person_ID               INTEGER         NOT NULL,
CONSTRAINT Owner_PK PRIMARY KEY (Owner_ID)
)
;
CREATE TABLE Employee(
    Employee_ID           INTEGER         NOT NULL,
    Spec	          VARCHAR(15),
    Person_ID             INTEGER         NOT NULL,
CONSTRAINT Employee_PK PRIMARY KEY (Employee_ID)
)
;
CREATE TABLE Pet_Type(
    Pet_Type_ID           INTEGER      NOT NULL,
    Name	          VARCHAR(15)  NOT NULL,
CONSTRAINT Pet_Type_PK PRIMARY KEY (Pet_Type_ID)
)
;
CREATE TABLE Pet(
    Pet_ID                  INTEGER      NOT NULL,
    Nick	            VARCHAR(15)  NOT NULL,
    Breed                   VARCHAR(20),
    Age                     INTEGER,
    Description             VARCHAR(50),
    Pet_Type_ID             INTEGER         NOT NULL,
    Owner_ID                INTEGER         NOT NULL,
CONSTRAINT Pet_PK PRIMARY KEY (Pet_ID)
)
;
CREATE TABLE Service(
    Service_ID              INTEGER         NOT NULL,
    Name	            VARCHAR(15)  NOT NULL,
CONSTRAINT Service_PK PRIMARY KEY (Service_ID)
)
;
CREATE TABLE Employee_Service(
    Employee_ID                   INTEGER         NOT NULL,
    Service_ID                    INTEGER         NOT NULL,
    Is_Basic	                  INTEGER
)
;
CREATE TABLE Order1(
    Order_ID                      INTEGER         NOT NULL,
    Owner_ID                      INTEGER         NOT NULL,
    Service_ID                    INTEGER         NOT NULL,
    Pet_ID                        INTEGER         NOT NULL,
    Employee_ID                   INTEGER         NOT NULL,
    Time_Order                    TIMESTAMP       WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    Is_Done	                  INTEGER         DEFAULT 0           NOT NULL,
    Mark	                  INTEGER,
    Comments                      VARCHAR(50),
CONSTRAINT Order_Is_Done CHECK (Is_Done in (0,1)),
CONSTRAINT Order_PK PRIMARY KEY (Order_ID)
)
;

ALTER TABLE Owner ADD CONSTRAINT FK_Owner_Person 
    FOREIGN KEY (Person_ID)
    REFERENCES Person(Person_ID)
;
ALTER TABLE Employee ADD CONSTRAINT FK_Employee_Person 
    FOREIGN KEY (Person_ID)
    REFERENCES Person(Person_ID)
;
ALTER TABLE Pet ADD CONSTRAINT FK_Pet_0wner 
    FOREIGN KEY (Owner_ID)
    REFERENCES Owner(Owner_ID)
;
ALTER TABLE Pet ADD CONSTRAINT FK_Pet_Pet_Type 
    FOREIGN KEY (Pet_Type_ID)
    REFERENCES Pet_Type(Pet_Type_ID)
;
ALTER TABLE Employee_Service ADD CONSTRAINT FK_Empl_Serv_Employee 
    FOREIGN KEY (Employee_ID)
    REFERENCES Employee(Employee_ID)
;
ALTER TABLE Employee_Service ADD CONSTRAINT FK_Empl_Serv_Service 
    FOREIGN KEY (Service_ID)
    REFERENCES Service(Service_ID)
;
ALTER TABLE Order1 ADD CONSTRAINT FK_Order_Employee 
    FOREIGN KEY (Employee_ID)
    REFERENCES Employee(Employee_ID)
;
ALTER TABLE Order1 ADD CONSTRAINT FK_Order_0wner 
    FOREIGN KEY (Owner_ID)
    REFERENCES Owner(Owner_ID)
;
ALTER TABLE Order1 ADD CONSTRAINT FK_Order_Pet 
    FOREIGN KEY (Pet_ID)
    REFERENCES Pet(Pet_ID)
;
ALTER TABLE Order1 ADD CONSTRAINT FK_Order_Service 
    FOREIGN KEY (Service_ID)
    REFERENCES Service(Service_ID)
;
-- +goose Down
-- +goose StatementBegin
SELECT 'down SQL query';
-- +goose StatementEnd
DROP TABLE Order1;
DROP TABLE Employee_Service;
DROP TABLE Service;
DROP TABLE Pet;
DROP TABLE Pet_Type;
DROP TABLE Employee;
DROP TABLE Owner;
DROP TABLE Person;
