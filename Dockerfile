FROM python:3.6
RUN pip install pymongo requests tqdm flask
COPY . /
CMD [ "python", "app.py" ]
