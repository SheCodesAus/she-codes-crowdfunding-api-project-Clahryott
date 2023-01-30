# {{ PLAYFUNDING }}
​
{{ Playfunding helps generate funding for afterschool programs for children, youth and families.

After-school activities like sport, music, craft and dance build children's confidence, help them make friends and learn to get along with people, keep them fit and healthy, and help them develop new skills and discover talents and interests 

Promote positive youth development and support social, emotional, cognitive, and academic development, reduce risky behaviors, promote physical health, and provide a safe and supportive environment for children and youth.}}
​
## Features
​
### User Accounts
​
- [X] Username
- [X] Email Address
- [X] Password   -******* Have we done authenticated? do we ?
​
### Project
​
- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [] Image
  - [X] Target Amount to Fundraise
  - [] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy
- Pledge
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [ ] Update - user can only update their own profile, not others
  - [ ] Destroy - user can only delete their own profile, not others
​
### Implement suitable permissions
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Limit who can create
  - [ ] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete
- Pledge
  - [X] Limit who can create
  - [ ] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete
- User
  - [ ] Limit who can retrieve
  - [ ] Limit who can update - user can only update their own profile, not others
  - [ ] Limit who can delete - user can only delete their own profile, not others
​
### Implement relevant status codes
​
- [x] GET returns 200
- [x] Create returns 201
- [ ] Not found returns 404
​
### Handle failed requests gracefully 
​
- [] 404 response returns JSON rather than text  
​
### Use token authentication
​
- [X] implement /api-token-auth/
​
## Additional features
​
- [ ] {Title Feature 1}
​
{{ description of feature 1 }}
​
- [ ] {Title Feature 2}
​
{{ description of feature 2 }}
​
- [ ] {Title Feature 3}
​
{{ description of feature 3 }}
​
### External libraries used
​
- [ ] django-filter    **** downloaded and added to installed apps, not sure what else to add it ***
​
​
## Part A Submission
​
- [ ] A link to the deployed project.
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Your refined API specification and Database Schema.
​
### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell

curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"email": "mary@admin.com",
	"username": "Mary",
	"password": "maryspassword"
}'

```
​
2. Sign in User
​
```shell

curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "Mary",
	"password": "maryspassword"
}'

```
​
3. Create Project
​
```shell

curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token  c044fd0b94a3abb664aca51cb089d278268b8d9c' \
  --header 'Content-Type: application/json' \
  --data '{
	
"title": "Girls Netball",
"description": "Netball for 10-11 yr olds, near Ballajura. Contributions will go towards court fees, umpire and team requirements such as uniform",
"goal":10000,
"image": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.gannett-cdn.com%2Fpresto%2F2019%2F05%2F02%2FPDEM%2F1ac9d821-1fc3-4603-8fbd-23acc93b2250-IMG_8908.JPG&imgrefurl=https%3A%2F%2Fwww.desmoinesregister.com%2Fstory%2Fnews%2Fcrime-and-courts%2F2019%2F05%2F01%2F24-severely-sick-cats-rescued-des-moines-days-after-26-others-saved-animal-rescue-league-iowa-arl%2F3648147002%2F&tbnid=bOhZ-L5cX07VAM&vet=12ahUKEwiMrsSFz9f8AhVsLrcAHYP7BOoQMygAegUIARDdAQ..i&docid=7RXs0wAS4FbggM&w=4032&h=3024&itg=1&q=sick%20cats&ved=2ahUKEwiMrsSFz9f8AhVsLrcAHYP7BOoQMygAegUIARDdAQ",
"is_open": true,
"date_created": "2023-01-30T09:05:10.729Z"
}'

```