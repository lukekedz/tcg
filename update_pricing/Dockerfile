FROM tcg_core

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python launch.py