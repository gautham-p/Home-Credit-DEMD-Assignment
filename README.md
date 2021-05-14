# Home Credit DEMD Assignment
Home Credit Default Risk is a financial risk modelling problem.It is a classification problem of whether a customer will default on his credit or not.We will be building a model to predict defaults and then we export this model using a file.Using this exported model, we build and deploy a web application that will accept input parameters.The web app with help of model will prdict the default status.The web app will be bulit using FastAPI as web framework.Docker is used for transporting and deploying the application.The production application will be hosted on the web using GCloud servers.Version Control is maintained using GitHub.

Initially, the main branch has no files or data,except readme,giattribute,gitignore.We make a branch to load data and process it.The project data was downloaded for the below URL.

[Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk/data)

Execution Order:

/scripts/Data Processing.ipynb

/scripts/Model Building & Export.ipynb

.\environ.ps1

main.py

.\docker.ps1

aws configure

.\aws.ps1

/aws proof

## Preprocessing Branch
This is the branch made to load data and process it.We load the trainig data to the working directory.Extracting the data file leads to a file size of 166MB.Github has a file size limit of 100MB.So we perform some EDA and feature importance measurements to get a reduce dataset that is still good at predicting results.The reduced dataset is saved as a csv file.Three files(Data Processing.ipynb, application_train.csv.zip, final_train.csv) are created in this branch and then merged into the main branch.

There was no pull requests made to merge this branch with main.It was done in local repository and the files are properly merged in github as well.Eventhough the merge happened properly and all files were pushed to github, github does not show any indication of merge happening.

## Modelling Branch
After merging the Preprocessing branch with main branch,we then split the main to a Modelling branch.In this branch,we fit a model to the data and export the model as a pickle file.Two files(Home_Credit_Model.pkl,Model Building & Export.ipynb) are created in this branch and a pull request will be raised.The Readme file has been edited in this branch.

After,the pull request was accepted,the modelling branch merged with main branch.Unlike with preprocessing, github for this branch merge now shows that the merge happened and its safe to delete the branch

## WebApp Branch

### Virtual Environment
The virtual environment must have the same Python version as our notebbok to avoid compatibility issues.Hence Model Building & Export was modified to export the python version/path and library versions.We need to install the version found in /config/Python.txt.So we created a powershell script environ.ps1 to load the directory from Python.txt, create a virtual environment and then activate it through shell scripting.Before running the script,the below line must be executed.

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

and then we run the powershell file using command ".\environ.ps1".A virtual environment is set up and activated.The powershell script also installs libraries required for model(/config/Libraries.txt).It also installs libraries needed for Web App as well(uvicorn,fastapi).

### Building Web App
We create a main.py file and make the application run on ip 0.0.0.0 and port 5000.We use Form and POST to get input values for single prediction(/creditcheck) because when we use GET,all the variable values are visible in address bar and we will exposing critical financial information.We also use Form and POST to get a File with multiple inputs so that we perform batch predictions(/bulkcreditcheck).

### Testing Web App
We use the first 20 rows of X_test table created in Model Building & Export File.Go to the end of file to see testing and verification data.The application is tested using Postman using ip 0.0.0.0:5000.For credit path,we use 16th row of test data to check if api is working.The entire test data is then uploaded as file and test using Body->form-data
tab of postman.The only issue that occurs is when using a browser.The browsers cannot detect the webapp running at 0.0.0.0.The base route also works when given GET and when run in postman.

## Docker Container
We freeze pip and get list of packages in requirements file.Then we update the main.py file to run certain commands depending on whether environment is production and make it run on port 5000.

We write and store our Dockerfile in the config folder.In the Dockerfile,we use the tiangolo fastapi image.We set the working directory as /app and copy the pickle,main,requirements file into it.We run the pip command to install all packages in requirements.txt.Then we set the environment to production and then run main.py.

Running power shell script .\docker.ps1 generates the requirements file.It also builds an image using the docker file and names it to home_demd.After that,its runs the image binding the ports 5000:5000.The results were tested using postman.After exiting using Ctrl+C, we must kill the docker container manually.

## AWS Deployment
Since I did not have any auto-debit option on my debit cards,I was not possible to get activate a Google Cloud account.I tried other cards,but my account was flagged and I was requested to submit a picture of my Debit card for manual approval.The process was taking too long and hence I opted to work with an AWS account.I used the Elastic Container Registry(ECR) to store my image in aws server.ECS(Elastic Container Service) and EC2(Elastic Compute Cloud) were used to deploy the application.The docker image in our local repository was tagged and the pused to ECR.Then using a t2.micro EC2 instance and ECS service,the application was deployed.The webapp was tested using postman and screenshots are present in the aws proof folder.

