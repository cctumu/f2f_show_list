FROM python:3-slim

# set a directory for the app
WORKDIR /usr/src/kaola.oms

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
#EXPOSE 5000

# run the command
CMD ["python3", "./product_show_list.py"]
