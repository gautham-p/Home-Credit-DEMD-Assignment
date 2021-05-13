# Home Credit DEMD Assignment
Home Credit Default Risk is a financial risk modelling problem.It is a classification problem of whether a customer will default on his credit or not.We will be building a model to predict defaults and then we export this model using a file.Using this exported model, we build and deploy a web application that will accept input parameters.The web app with help of model will prdict the default status.The web app will be bulit using FastAPI as web framework.Docker is used for transporting and deploying the application.The production application will be hosted on the web using GCloud servers.Version Control is maintained using GitHub.

Initially, the main branch has no files or data,except readme,giattribute,gitignore.We make a branch to load data and process it.

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

and then we run the powershell file using command ".\environ.ps1".A virtual environment is set up and activated.Then the required libraries for model is install using file /config/Libraries.txt.

### Building Web App
The fastapi,uvicorn libraries are installed using pip.The we create a main.py file and make the application run on ip 0.0.0.0 and port 5000.We use Form and POST to get input values for single prediction(/creditcheck) because when we use GET,all the variable values are visible in address bar and we will exposing critical financial information.We also use Form and POST to get a File with multiple inputs so that we perform batch predictions(/bulkcreditcheck).