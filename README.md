#Run the project:
nohup python3 manage.py runserver

#Stop existing Port:
kill -9 $(lsof -t -i:8001)
That's it!
