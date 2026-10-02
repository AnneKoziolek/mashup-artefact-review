# MASHUP is implemented in Python 3.6 (artefact README). 3.6 is end-of-life;
# the last official images are Debian bullseye based.
FROM python:3.6-bullseye

# The AWS CLI is installed from pip (v1), as the artefact README does; v2 is a
# separate binary and is not what the authors used.
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
 && rm /tmp/requirements.txt
