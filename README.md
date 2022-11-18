# Python_course
Course made in collaboration between David Redondo and Mariano Álvarez.
The main objective was made a little introduction to some advanced points on python programming
such as OOP, how to work with some data formats, web services, github...
## Index
- OOP
- JSON
- CSV
- API
- HTTP
- GITHUB

## Relevant links and helpful resources:

## OOP (Classes)

https://realpython.com/python3-object-oriented-programming/

https://www.geeksforgeeks.org/python-oops-concepts/

## JSON
https://realpython.com/python-json/

## CSV

https://docs.python.org/3/library/csv.html

https://www.geeksforgeeks.org/working-csv-files-python/

## API

![image](https://user-images.githubusercontent.com/80169535/183763549-97fc9ff7-7398-4d97-af4e-381b1967de11.png)

## HTTP

![image](https://user-images.githubusercontent.com/80169535/183763444-89ec5aaf-28c0-4186-931f-f7f35027e669.png)

https://www.digitalocean.com/community/tutorials/how-to-get-started-with-the-requests-library-in-python-es#usar-la-api-de-traduccion

https://www.tutorialspoint.com/python_network_programming/python_http_authentication.htm#

https://j2logo.com/python/python-requests-peticiones-http/#requests-json

## GITHUB

![image](https://user-images.githubusercontent.com/80169535/183763297-14ca2004-bc6a-4790-ba92-20c9dd7dc5e5.png)

https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners

## List of useful commands

### GIT
- git init // Generate a git empty local repository in the path where you are 
- git status // Show the status files within the path
- git add <filename> // Add only the file called to the staging area
- git add . // Add all the files to the staging area
- git commit -m “ Write the commit purpose inside these quotation marks ” // This command records or snapshots the file permanently in the version history
- git diff // Show all the differences between working directory files and localrepo files
- git git diff –staged // Shows the differences between the files in the staging area and the latest version present
- git reset <file> // This command unstages the file, but it preserves the file contents
- git reset <commit id> // Undoes ALL the commits after the spacified commit and preserves the changes locally
- git reset –hard <commit id> // It does a hard reset which discard all history and goes back yo the specified commit
- git checkout -b <new branch name> // It creates a new branch and It switchs to the new branch
- git checkout <branch name> // It switchs to the branch specified
- git log --graph --all --oneline // This command is used to list the version history for the current branch summarized
- git branch -a // It lists all the local branches
- git branch -d // Delete the current branch
- git merge <branch name> // It merges the specified branch's histary inte the currente branch
### GITHUB 
- git clone <url> // It clones the url repository within the current path. This command it's pretty essential to establish a solid connection between both
- git remote add <branch name> <Remote Server Link> // It connects your local repository to your remote repository.
- git push origin <branch name destination> // It pushs the files commited to the branch specified
- git push --all // It pushs all the cahnages to the remote repository
- git pull origin <branch name destination> // It brings all the changes and new files uploaded to the specified branch

- In case that you are having troubles to push or fetch your documents, include de command --rebase. This will update the branch with lastest changes. 
 The command will have a sintax similar to this-> git push --rebase remote branch
 
![image](https://user-images.githubusercontent.com/80169535/202707128-4ff16fbc-9133-4326-9f1b-b2c9e37c5a76.png)
  
- If it doesn't work, try with the command -f to force it.
  The command will have a sintax similar to this-> git push -f <remote> <branch>



### Helpful links of youtube videos

https://www.youtube.com/watch?v=5g37NElQnCQ&list=WL&index=4

https://www.youtube.com/watch?v=9AflLDdSjkg

https://git-scm.com/book/id/v2/Git-Branching-Remote-Branches
