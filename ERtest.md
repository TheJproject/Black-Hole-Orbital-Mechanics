# ER Diagrams

## Intro

ER = Entity Relationship

Entity - An object we want to model and store information about

ER Diagram translate business need to actual database.

Attributes - Specific pieces of information abount an entity

Primary key - An attribute(s) that uniquely identify an entry in the database table. (always underlined)

Composite attribute - An attribute that can be broken up into sub-attributes

Multi-valued Attribute - An attribute that can have more than one value

Derived Attribute - An attribute that can be derived from the other attributes

Multiple Entities - You can define more than one entity in the diagram

Relationships - defines a relationship between two entities

Total Participation - All members must participate in the relationship

(ex : all class must be taken at least for one student to exist)

Relationship Cardinality - the number of instances of an entity from a relation that can be associated with the relation (ex: a student can take any number of classes. A class can be taken by any number of student) 1:1, 1:N, N:M

Weak entity - An entity that cannot be uniquely identified by its attribute alone (ex: an exam cannot exist without a class)

## Designing an ER Diagram

The company is organized into **branches**. Each branch has a unique number and a name.

![ER%20Diagrams%200b3e9d5283f34bafa59495e8bafbfa8e/Untitled_Document_(1).png](ER%20Diagrams%200b3e9d5283f34bafa59495e8bafbfa8e/Untitled_Document_(1).png)

The company makes it's money by selling to **clients**. Each **clients** has a name and unique number to identify it.

![ER%20Diagrams%200b3e9d5283f34bafa59495e8bafbfa8e/Untitled_Document.png](ER%20Diagrams%200b3e9d5283f34bafa59495e8bafbfa8e/Untitled_Document.png)

The fundation of the company is it's **employees**. Each **employee** has a name, birthday, sex, salary and a unique number to identify it.

![ER%20Diagrams%200b3e9d5283f34bafa59495e8bafbfa8e/Untitled_Document_(2).png](ER%20Diagrams%200b3e9d5283f34bafa59495e8bafbfa8e/Untitled_Document_(2).png)

An **employee** can work for one **branch** at a time. (Not rigorously defined in the doc)

Each **branch** will be managed by one of the **employees** that work there. We're also awant to eep trac of when the current manager started as manager

An **employee** can act as a supervisor for other **employees** at the branch, an **employee** may also act as the supervisor for **employees** at other branches. An **employee** can have at most one supervisor.

A branch may handle a number of **clients**, however a single **client** may only be handled by one **branch** at a time.

**Employees** can work with **clients** controlled by their branch to sell them stuff. If necessary multiple employees can work with the same client.

We'll want to keep track of how many dollars worth of stuff each employee sells to each client they work with.

Many **branches** will need to work with **suppliers** to buy inventory. For each supplier we'll keep track of their name and the type of product they're selling the **branch**. A single supplier may supply products to multiple branches.

![ER%20Diagrams%200b3e9d5283f34bafa59495e8bafbfa8e/Untitled_Document_(3).png](ER%20Diagrams%200b3e9d5283f34bafa59495e8bafbfa8e/Untitled_Document_(3).png)

Thick line means total participation.

## Converting ER Diagrams to Schemas

Step 1: Mapping of regular Entity Types

For each regular entity type create a relation (table) that includes all the simple attributes of that entity.

Step 2: Mapping of weak entity types 

For each weak entity type create a relation (table) that includes all simple attributes of the weak entity.

The primary key of the new relation should be partial key of the weak entity plus the primary key of its owner.

Step 3: Mapping of Binary 1:1 Relationships Types

Include one side of the relationship as a foreign key in the other. favor total participation.

Step 4: Mapping of Binary 1:N Relationships Types

Include the 1 side's primary key as a foreign key on the N side relation (table).

Step 5: Mapping of Binary M:N Relationships Types

Create a new relation (table) who's primary key is a combination of both entities' primary key's. Also include any relationship attributes.