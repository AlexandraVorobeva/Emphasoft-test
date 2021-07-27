# Emphasoft-test
## FASTAPI CRUD application.
REST API application for users with authentication.<br>

### Basic functionality:<br>
1.Web REST API<br>
2.For a start you should sign up or sign in (if you was registered before)<br>
3.Functionality for users:<br>
  -List of all user<br>
  -Current user information<br>
  -Information about any user by id<br>
  -Change or delete any information about users<br>
  -Create new users<br>


## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/Emphasoft-test<br>
$ cd Emphasoft-test<br>


### Create virtualenv:<br>
$ virtualenv venv<br>
$ source venv/bin/activate<br>

### Dependency
$ pip install -r requirements.txt<br>

### Run the sample server:<br>
$ uvicorn app:app --reload<br>


### Run tests:<br>
$ run pytest<br>


### API from the browser:
You can work on the API directly in your browser
http://127.0.0.1:8000/docs <br>
![Screenshot](https://github.com/SparklingAcidity/Emphasoft-test/blob/in_process/img_for_readme/Снимок%20экрана%202021-07-24%20в%2013.47.32.png) <br>
or http://127.0.0.1:8000/redoc
![Screenshot](https://github.com/SparklingAcidity/Emphasoft-test/blob/in_process/img_for_readme/Снимок%20экрана%202021-07-25%20в%2013.09.24.png)
