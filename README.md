#### Setup for your environment

- Connect to your project directory 

- Create your virtual environment inside your project directory:

```
python3 -m venv env (for MAC)
py -m venv env (for WINDOWS)
```

- Put the venv in your .gitignore (This keeps your virtual environment out of source control):

```
echo 'venv' > .gitignore
```

- Activate your virtual environment with the following commands:

``` 
source env/bin/activate (for MAC)
.\env\Scripts\activate (for WINDOWS)

```
- Select your Python interpreter in text

- Install the packages from the requirements.txt:

```
pip install -r requirements.txt
```

How to run the project

```
python app.py
```