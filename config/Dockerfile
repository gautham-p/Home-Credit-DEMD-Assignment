FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app/
COPY ../config/requirements.txt /app/
RUN pip install -r requirements.txt
ENV ENVIRONMENT production
COPY main.py /app/
COPY Home_Credit_Model.pkl /app/
CMD python3 main.py