aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 567256470679.dkr.ecr.ap-southeast-1.amazonaws.com
docker tag home_credit_demd:latest 567256470679.dkr.ecr.ap-southeast-1.amazonaws.com/home-demd:v1
docker push 567256470679.dkr.ecr.ap-southeast-1.amazonaws.com/home-demd:v1