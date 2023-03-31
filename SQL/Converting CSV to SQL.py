#@author: james


#Importing Listings.csv into MySql
import pandas as pd
import glob, os
from sqlalchemy import create_engine

for listings in glob.glob("listings.csv"):
    df = pd.read_csv(listings)
    
    # Create SQLAlchemy engine to connect to MySQL Database
    engine = create_engine("mysql+mysqldb://root:@localhost:3306/airbnb")
    
    # Convert dataframe to sql table                                   
    df.to_sql(listings[:-4], engine, index=False)
    
    print('done')
    
    
#Importing Reviews.csv into MySql
import pandas as pd
import glob, os
from sqlalchemy import create_engine

for reviews in glob.glob("reviews.csv"):
    df = pd.read_csv(reviews)
    
    # Create SQLAlchemy engine to connect to MySQL Database
    engine = create_engine("mysql+mysqldb://root:@localhost:3306/airbnb")
    
    # Convert dataframe to sql table                                   
    df.to_sql(reviews[:-4], engine, index=False)
    
    print('done')