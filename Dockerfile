FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir bandit semgrep

COPY .bandit /app/.bandit
COPY semgrep.yml /app/semgrep.yml
COPY scr/ /app/scr/

CMD sh -c "bandit --ini /app/.bandit -r /app/scr || true; echo '----------------'; semgrep --config /app/semgrep.yml /app/scr || true"