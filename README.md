IN3007 Individual project 

ONEDRIVE link: https://cityuni-my.sharepoint.com/:f:/g/personal/abbib_akram_city_ac_uk/El5qEy7yUCNMhbNEa6tdTpUBWPguGN57IYBmZN8BpzBStQ?e=dWzinD

This is a web application which helps medical professionals not only manage patient information but also analyse CT scan images of patients lungs in order to deduce whether they are normal or abnormal,saving the doctors the stress,time and hassle of analysing images manually.

The technologies used to implement this softare product are as follows:
1.FastAPI
2.Postgresql
3.Pycharm(IDE)
4.Google Collab
5.Jupyter Notebook
6.Streamlit

Instructions:

In order to run the frontend element of this project implement the following:

1.import streamlit as st
2.import time
3.import pandas as pd
4.import numpy as np

To run this element do the following:

1.streamlit run main.py

(If the URL doesnt open automatically,copy and paste the url produced in the terminal into the search area of a browser.

In order to run the backend element (main program) of this project implment the following:

1.brew install python@3.11
2.python3.11 -m venv venv 
3.venv/bin/activate.fish
4.pip install --upgrade pip
5.pip install -r requirements.txt

To run this element do the following:

1.uvicorn main:app --host 0.0.0.0/docs

In order to run the Machine learning algorithm:

1.In order to set up this element do the following packages:

import io
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras.utils
import seaborn as sns
import ast
import codecs
import csv
import math
from tensorflow import keras
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from PIL import Image
from collections import Counter
from imblearn.over_sampling import SMOTE
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras import regularizers
from keras.callbacks import EarlyStopping
from keras.applications import MobileNetV2
from keras.utils import to_categorical
from tensorflow.keras import models, layers
import shutil
import random

(Install the relevant dependencies locally via the terminal)

Run the model via the following:

1.Choose the T4 GPU runtime

2.Run each cell in Google Collab

3.Wait for the model to train



File structure:
400 v2 /Documents
Model
Schema

References for this project:
1.fastapi.tiangolo.com. (n.d.). SQL (Relational) Databases - FastAPI. [online] Available at: https://fastapi.tiangolo.com/tutorial/sql-databases/[Accessed 1 May 2024].

2.Educative. (2015). How to use PostgreSQL database in FastAPI. [online] Available at: https://www.educative.io/answers/how-to-use-postgresql-database-in-fastapi [Accessed 3 May 2024].

3.Eric Roby and Chad Darby (2024). 'FastApi request method logic', lecture notes distributed in the topic No code Dive in and learn FastAPI from scratch! Learn FastAPI, RESTful APIs using Python, SQLAlchemy, OAuth, JWT and way more!. Udemy, Online On 05/04/2024.
https://www.udemy.com/course/fastapi-the-complete-course/learn/lecture/39925428#overview[Accessed 25 April 2024]

4.www.youtube.com. (n.d.). How to connect PyCharm with a Docker container? [online] Available at: https://www.youtube.com/watch?v=Iam-VLR6tAQ [Accessed 2 May 2024].

5.sqlmodel.tiangolo.com. (n.d.). Multiple Models with FastAPI - SQLModel. [online] Available at: https://sqlmodel.tiangolo.com/tutorial/fastapi/multiple-models/ [Accessed 1 May 2024].

6.codebasics (2021). Deep learning project end to end | Potato Disease Classification - 4 : FastAPI/tf serving Backend. [online] YouTube. Available at: https://www.youtube.com/watch?v=t6NI0u_lgNo&list=PLeo1K3hjS3ut49PskOfLnE6WUoOp_2lsD&index=4 [Accessed 16 Jul. 2024].
‌
7.GitHub. (n.d.). potato-disease-classification/api/main.py at main · codebasics/potato-disease-classification. [online] Available at: https://github.com/codebasics/potato-disease-classification/blob/main/api/main.py [Accessed 16 Jul. 2024].
‌
8.Sinha, A. (2023). Download and configure PostgreSQL16 on MacOS - Abhinav Sinha - Medium. [online] Medium. Available at: https://medium.com/@abhinavsinha_/download-and-configure-postgresql16-on-macos-d41dc49217b6 [Accessed 16 Jul. 2024].
‌
9.Gupta, A. (2017). Creating user, database and adding access on PostgreSQL. [online] Medium. Available at: https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e [Accessed 16 Jul. 2024].
‌
10.Stack Overflow. (n.d.). pip3 install h5py is not working in mac OS. [online] Available at: https://stackoverflow.com/questions/48467924/pip3-install-h5py-is-not-working-in-mac-os [Accessed 16 Jul. 2024].
‌
11.Stack Overflow. (n.d.). Why am I getting a permission denied error for schema public on pgAdmin 4? [online] Available at: https://stackoverflow.com/questions/67276391/why-am-i-getting-a-permission-denied-error-for-schema-public-on-pgadmin-4 [Accessed 16 Jul. 2024].
‌
12.Nileg Production (2022). Streamlit Introduction | Complete Streamlit Python Course | Streamlit Tutorial 1. [online] YouTube. Available at: https://www.youtube.com/watch?v=RjiqbTLW9_E&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW [Accessed 14 Jul. 2024].
#‌

13.Mısra Turp (2022). Streamlit Elements You Should Know About in 2023. [online] YouTube. Available at: https://www.youtube.com/watch?v=_Um12_OlGgw [Accessed 14 Jul. 2024].
#‌

14.Streamlit (n.d.). Streamlit Docs. [online] docs.streamlit.io. Available at: https://docs.streamlit.io/.
#‌
15.#1.codebasics (2021). Deep learning project end to end | Potato Disease Classification - 3 : Model Building. [online] YouTube. Available at: https://www.youtube.com/watch?v=ZN6P_GEJ7lk&list=PLeo1K3hjS3ut49PskOfLnE6WUoOp_2lsD&index=3.
‌
16.kaggle.com. (n.d.). Chest Cancer CT-Scan Detector. [online] Available at: https://www.kaggle.com/code/jameshuangcoding/chest-cancer-ct-scan-detector.
‌
