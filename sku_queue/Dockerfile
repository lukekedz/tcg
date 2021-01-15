FROM tcg_core

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "python", "./main.py", "--host=0.0.0.0" ]