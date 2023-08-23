
This project is to access the twitter API and get the relevant data. 
*** twitter_etl.py - extracting data from twitter and storing into csv(get elonmusk tweets and read json and store in csv through panda package) ***

Step 1 - Install pandas using pip install pandas    -- This has pd.dataframe - which creates sheet in csv file. 
You can check using pip freeze. 

Step 2 - Check if tweepy is installed using pip freeze otherwise, use pip install tweepy. 
Step 3 - >pip install s3fs - used to access the data in s3 buckets. 

*** Create AWS EC2 instance, install packages on it and deploy airflow on that. ****
Installing Airflow:
Step 1 - Login to AWS and launch new EC2 t2.micro instance with ubuntu OS. 
Step 2 - Once the instance is launched, connect through SSH and run the sudo commands to install/update -
> sudo apt-get update  ( update the ubuntu )
> sudo apt install python3-pip
> sudo apt install apache-airflow
> sudo pip install pandas
> sudo pip install s3fs
> sudo pip install tweepy 
> clear
> airflow -- this should display soemthing once airflow is installed 
> airflow standalone -- start running airflow server which lists admin and password. COPY HERE
in browser:  machinename:8080 -- search this in the browser as airflow is running on port 8080
And this doesn't work first time. You have to go to security section -- change inbound rules to allow all traffic. (Not on prod). 

*** Once the airflow is running on EC2 instance, we need to create DAG for all this process ***
Step 1 - create DAG and add task where it runs the funct created in the twitter_etl.py 

Step 2 - create s3 bucket and copy the csv to that location. 

Step 3 - 
