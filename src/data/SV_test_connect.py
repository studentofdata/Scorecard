# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:57:23 2016

@author: Cloud User
"""

import pandas as pd
from sqlalchemy import create_engine
import MySQLdb

host    = 'db-5.sv.local'
db_name = 'crm_monterey_count_30'
user    = 'Monterey_Remote'
pw      = '43yhdn2m'


#engine = create_engine("mysql+mysqldb://job_growthmaster:jobgrowthpass@job-growth.cotzely14ram.us-west-2.rds.amazonaws.com/job_growth2?charset=utf8&use_unicode=0")

engine = create_engine("mysql+mysqldb://Monterey_Remote:43yhdn2m@db-5.sv.local:3306/crm_monterey_count_30?charset=utf8&use_unicode=0")


pd.read_sql('show tables;', con = engine)