FROM python:3.10.9
WORKDIR /app
COPY requirements.txt .
COPY main.py .
COPY download_models.py .
RUN python3 -m venv .venv
ENV PATH="/app/.venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt && \
    python3 download_models.py
EXPOSE 6000

ENTRYPOINT [ "python3" ]

# Run main.py when the container launches
CMD [ "main.py" ]