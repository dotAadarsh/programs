### Bash Points

- While working with simple texts and string, there will be no differences either we use a single quote or double quote.
- It should be noted that the shell variable expansion will only work with double-quotes.
- Bash don't have to define the data type of any variable at the time of variable declaration. Bash variables are untyped, which means just type the variable name by assigning its value, and it will automatically consider that data type.
- To read the Bash user input, we use the built-in Bash command called read. 
- If we don't pass any variable with the read command, then we can pass a built-in variable called REPLY (should be prefixed with the $ sign) while displaying the input.
- use the `date` command to display or change the current date and time value of the system.
- Sleep is a command-line utility which allows us to suspend the calling process for a specified time. In other words, Bash sleep command is used to insert a delay or pause the execution for a specified period of time.
- There are 11 arithmetic operators which are supported by Bash Shell.
- The Bash case statement is the simplest form of IF-THEN-ELSE with many ELIF elements.
- Each case statement in bash starts with the 'case' keyword, followed by the case expression and 'in' keyword. The case statement is closed by 'esac' keyword.
- We can apply multiple patterns separated by | operator. The ) operator indicates the termination of a pattern list.
- A pattern containing the statements is referred to as a clause, and it must be terminated by double semicolon (;;).
- An asterisk symbol (*) is used as a final pattern to define the default case. It is used as a default case when used as the last case.