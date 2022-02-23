# Practice
As per the requirement, I defined a set of 5 roles and 5 users.
The program takes an input of user ID in integers and return a list of all the subordinates and the subordinates' subordinate.
If the userID is invalid, it will output an error statement.
If the userID has no parent, the output will be nothing.
If the userID has no subordinate, the output will be blank.
If 0 is pressed, the code will exit the execution.


Here is the sample run will all the inputs:

Enter User Id for which you want to print the Subordinates or 0 to offer a contract
Enter -> 5
-------------------------------------------------------------------------------------
Enter User Id for which you want to print the Subordinates or 0 to offer a contract
Enter -> 4
Id : 2, Name : Emily Employee, Role : 4
Id : 3, Name : Sam Supervisor, Role : 3
Id : 5, Name : Steve Trainer, Role : 5
-------------------------------------------------------------------------------------
Enter User Id for which you want to print the Subordinates or 0 to offer a contract
Enter -> 3
Id : 2, Name : Emily Employee, Role : 4
Id : 5, Name : Steve Trainer, Role : 5
-------------------------------------------------------------------------------------
Enter User Id for which you want to print the Subordinates or 0 to offer a contract
Enter -> 2
-------------------------------------------------------------------------------------
Enter User Id for which you want to print the Subordinates or 0 to offer a contract
Enter -> 1
Id : 2, Name : Emily Employee, Role : 4
Id : 3, Name : Sam Supervisor, Role : 3
Id : 4, Name : Mary Manager, Role : 2
Id : 5, Name : Steve Trainer, Role : 5
-------------------------------------------------------------------------------------
Enter User Id for which you want to print the Subordinates or 0 to offer a contract
Enter -> 0
You Entered 0, I hope the code is up to the mark and contract is on the way !!!
Exiting!!!
