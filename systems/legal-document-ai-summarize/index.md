

I need to design a system.
The system should have a slack integration so that lawyers can create a case. The form should allow them to define the details of the case in a text input, and select a due date, and add attachments.

After clicking the submit button, the form data is sent to the backend to process. The processing time can take up to 5 minutes. A case link is posted in the slack channel immediately and the user can check later.

The link will be automatically notified in slack via a webhook like:
"Your case Bewkafwe-eafewf-awef is submitted successfully, please wait a  few minutes for processing. You can check the case [here](http://localhost:3000/case/Bewkafwe-eafewf-awef) after a few minutes.

User should be able to click the link later to see the case summary and other information generated by AI.

Requirement:
* Design the end to end flow, create any backend service as needed. Focus on how the service interacts with each other and getting the functionality right. You can assume there is an OpenAI API (or any other AI services) for use. Talk about API and data model.
* Don’t need to worry about authentication.
* This is a low QPS service. Don’t need to do any traffic estimation.
The case processing will take 1 min~5 min.

-----

1. slack app with custom slash command like /create-case
    - opens modal with creation form
2. api gateway routes requests from slack and web FE
3. case creation service receives create requests from API
    - generates unique case ID
    - stores case data by ID in db
    - enqueue a task to process case
    - trigger slack webhook to post the case link in slack
4. datavase store case info - status, details, due date, file refs
5. message queue processes cases
    - ensures reliable order delivering cases to case processing serv
6. case processing service consumes tasks from message queue
    - processes case details (5 mins)
    - interfaces with AI service to summarize case
    - updates case status and information in database
7. AI service wraps openAI, langchain etc.
    - generates case summaries based on details
8. web frontend allows users to view processed cases.
    - fetches case info from API.
9. slack webhook post notifications back to slack channel.

# File storage
For file handling we can use object storage like s3. 

1. Whem the file is uploaded through slack, the files are sent through
the API gateway to the case creation service, which will upload them
to the s3 bucket.
    - This service will generate and return UUIds which the case creation service can store in the DB.
2. Case processing service needs access to the actual files during process. It retrieves files from s3 using storage IDs.
    - web frontend also needs access to files contents, when displaying case details. This can happen via pre-signed URls or through the API depending on security reqs.
3. data models updated to relect Files:

File:
id
name
s3_key
uploaded_at

Case:
id
status // submitted, processing, completed
details ...
due_date
files: List[File]
summary
created_at
processed_at

4. AI service can be a serverless function deployed on eg Lambda, which will be triggered by the case processing service.
    - this takes case details and file reference(s) as input.
5. In the lambda function, we make calls to openAI and langchain 
API's to generate case summary.
    - use env file to securely store API keys
6. First the case processing service needs to retrieve case details and file contents from s3.
    - it passes these elements to AI service
    - AI service calls openAI, processes info and returns generated summary to case processing service.