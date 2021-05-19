# Tryout_Project-Flask-App-for-answering-questions

This is a flask app that performs question-answering on various pdf files. You can use bunch of pdf files and then you can get answers, either exact or most simillar, to given question. Using pdf files is really easy and can be useful in many cases. For example, you have a set of pdf files of annual reports of a company or have any other large number of pdf files from which you want to extract data then building a question-answering system can be very beneficial.

![](https://github.com/vanshu25/Tryout_Project-Flask-App-for-answering-questions/blob/main/images/Screenshot%20(205).png)

![](https://github.com/vanshu25/Tryout_Project-Flask-App-for-answering-questions/blob/main/images/Screenshot%20(204).png)

## Project Structure

### Folder for Pdf documents - docs

* Create a folder named "docs" and add your pdf files in this folder. These files will work as data for question-answering system. I have added 3 files here you can choose whatever files you want to choose.

### Models

* Create a folder named "models" and in this folder we are going to download pre-trained model called 'bert-squad_1.1'. This model is pre-trained model on Stanford Question Answering Dataset (SQuAD). 
* To download this pre-trained model, run the following in python : 
  from cdqa.utils.download import download_model
  download_model(model='bert-squad_1.1', dir='./models')

### Templates

* Create a folder named "templates" and here we are gonna add our html files for the app. I have added two files here - home.html and after.html

### app.py

* This is the python file for the flask app

### qa.py

* This is the python file for the fitting of model.

Your Project directory should look like this:

![](https://github.com/vanshu25/Tryout_Project-Flask-App-for-answering-questions/blob/main/images/Screenshot%20(203).png)

## Running the Flask App

* Activate your virtual environment and then run 'flask run'
* You can then go to the localhost on which the app is running.

# explain the three top answers and libraries by each folder above
