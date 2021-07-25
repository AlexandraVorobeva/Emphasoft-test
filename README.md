# Emphasoft-test
## FASTAPI CRUD application.
REST API application scans a folder with all subfolders and text files and provides aggregate statistics for certain indicators.<br>

### Basic functionality:<br>
1.Web REST API<br>
2.For a start application scans DIR (base directory) with all subfolders and text files<br>
3.Information for REST API:<br>
  -List of folders and files<br>
	-Count of files<br>
	-Names_of files<br>
	-The most common word<br>
	-The rarest word<br>
	-Average length of words<br>
	-Count of vowels/consonants/syllables<br>
4.For each file or word you can use RESR API request: 	/api/file/readable-file-id 
5.You can use this app English and Russian words


## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/Emphasoft-test<br>
$ cd Emphasoft-test<br>


### Create virtualenv:<br>
$ virtualenv venv<br>
$ source venv/bin/activate<br>

### Dependency
$ pip install -r requirements.tx<br>

### Run the sample server:<br>
$ uvicorn app:app --reload<br>


### Run tests:<br>
$ run pytest<br>

### API from the command line:
$ curl -X GET "http://127.0.0.1:8000/"<br>


### API from the browser:
You can also work on the API directly in your browser
http://127.0.0.1:8000/docs
![Screenshot](https://github.com/SparklingAcidity/Emphasoft-test/blob/in_process/img_for_readme/Снимок%20экрана%202021-07-24%20в%2013.47.32.png)
