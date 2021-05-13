pip freeze > ./config/requirements.txt
docker build -f config/Dockerfile -t home_credit_demd .
docker run -p 5000:5000 home_credit_demd