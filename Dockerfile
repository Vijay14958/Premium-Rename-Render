FROM python:3.10

WORKDIR /Premium-Rename-Render

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]
