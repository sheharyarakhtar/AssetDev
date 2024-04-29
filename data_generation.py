import os
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from lightgbm import LGBMRegressor, LGBMClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import mlflow 
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from xgboost import XGBClassifier, XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
from optbinning import OptimalBinning
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from scipy.stats import f_oneway
import sweetviz as sv
warnings.filterwarnings('ignore')
def prob_return(num):
    mu = 0
    sigma = 0.8
    return np.random.normal(mu, sigma, num)
def create_categorical(df, pop_vals, col_name):
    le = LabelEncoder()
    le.fit(pop_vals)
    le.transform(pop_vals)
    noisy_probs = (df['risk_probability'] + np.random.beta(10,15,size = len(df)) )
    noisy_probs = [0.99 if i>1 else i for i in noisy_probs]
    values = [int(i*len(pop_vals)) for i in noisy_probs]
    transformed = le.inverse_transform(values)
    df[col_name]  = transformed
    return df
    
def generate_data(num):
    import random
    import pandas as pd
    random.seed(10)
    df = pd.DataFrame({'party_id':[i for i in range(num)],
                      'risk_probability': [random.uniform(a = 0, b = 1) for i in range(num)]
                      })
    
    df['high_risk_flag'] = [0 if i<0.90 else 1 for i in df['risk_probability']]
    ##################### BILL  ##############################
    df['AVG BILL L1M'] = 4000*(df['risk_probability'] + prob_return(num) )
    
    df['AVG BILL RENTAL L1M'] = 700*(df['risk_probability'] + prob_return(num) )
    df['AVG BILL RENTAL L2M'] = 1700*(df['risk_probability'] + prob_return(num) )
    df['AVG BILL RENTAL L3M'] = 1600*(df['risk_probability'] + prob_return(num) )
    df['AVG BILL RENTAL L4M'] = 400*(df['risk_probability'] + prob_return(num) )
    df['AVG BILL RENTAL L5M'] = 350*(df['risk_probability'] + prob_return(num) )
    df['AVG BILL RENTAL L6M'] = 400*(df['risk_probability'] + prob_return(num) )
    
    df['AVG USAGE L1M'] = 0.02*(df['risk_probability'] + prob_return(num) )
    df['AVG USAGE L2M'] = 0.2*(df['risk_probability'] + prob_return(num) )
    df['AVG USAGE L3M'] = 0.2*(df['risk_probability'] + prob_return(num) )
    df['AVG USAGE L4M'] = 0.15*(df['risk_probability'] + prob_return(num) )
    df['AVG USAGE L5M'] = 1300*(df['risk_probability'] + prob_return(num) )
    df['AVG USAGE L6M'] = 1400*(df['risk_probability'] + prob_return(num) )
    
    df['AVG OUTSTANDING BILL L1M'] = 5000*(df['risk_probability'] + prob_return(num) )
    df['TOTAL OUTSTANDING BILL L1M'] = 5000*(df['risk_probability'] + prob_return(num) )
    df['AVG OUTSTANDING BILL L2M'] = 3500*(df['risk_probability'] + prob_return(num) )
    df['TOTAL OUTSTANDING BILL L2M'] = 7000*(df['risk_probability'] + prob_return(num) )
    df['AVG OUTSTANDING BILL L3M'] = 3000*(df['risk_probability'] + prob_return(num) )
    df['TOTAL OUTSTANDING BILL L3M'] = 4000*(df['risk_probability'] + prob_return(num) )
    
    ########### ACTV ##############
    df['PERCENT ACTIVE ACCOUNTS L30D'] = df['risk_probability'] + prob_return(num)
    df['PERCENT ACTIVE ACCOUNTS L60D'] = df['risk_probability'] + prob_return(num)
    df['PERCENT ACTIVE ACCOUNTS L90D'] = df['risk_probability'] + prob_return(num)
    df['TOTAL ACTIVE ACCOUNTS L30D'] = 50*(df['risk_probability'] + prob_return(num))
    df['TOTAL ACTIVE ACCOUNTS L60D'] = 100*(df['risk_probability'] + prob_return(num))
    df['TOTAL ACTIVE ACCOUNTS L90D'] = 25*(df['risk_probability'] + prob_return(num))
    
    ########### ARPU #################
    df['AVG REVENUE PER USER L12M'] = 350*(df['risk_probability'] + prob_return(num))
    df['AVG REVENUE PER USER L1M'] = 3000*(df['risk_probability'] + prob_return(num))
    df['AVG REVENUE PER USER L3M'] = 150*(df['risk_probability'] + prob_return(num))
    df['AVG REVENUE PER USER L6M'] = 2000*(df['risk_probability'] + prob_return(num))
    df['TOTAL REVENUE PER USER L12M'] = 200*(df['risk_probability'] + prob_return(num))
    df['TOTAL REVENUE PER USER L1M'] = 325*(df['risk_probability'] + prob_return(num))
    df['TOTAL REVENUE PER USER L3M'] = 150*(df['risk_probability'] + prob_return(num))
    df['TOTAL REVENUE PER USER L6M'] = 3500*(df['risk_probability'] + prob_return(num))

    ############# FLG ##############
    df['TOTAL NON-BARRED CUSTOMERS L6M'] = 97*(df['risk_probability'] + prob_return(num))
    df['TOTAL BARRED CUSTOMERS'] = 52*(df['risk_probability'] + prob_return(num))
    df['TOTAL NON-BARRED CUSTOMERS L1M'] = 1*(df['risk_probability'] + prob_return(num))
    df['TOTAL BARRED CUSTOMERS L1M'] = 1*(df['risk_probability'] + prob_return(num))
    
    df['PERCENT OF FLAGGED CREDIT CARDS']  = 1*(df['risk_probability'] + prob_return(num))
    
    # df['CST_CAT_FLG_EP_norm'] = 73*(df['risk_probability'] + prob_return(num))
    # df['CST_CAT_FLG_NP_norm'] = 87*(df['risk_probability'] + prob_return(num))
    
    df['TOTAL NON-PORTIN CUSTOMERS'] = 0.5*(df['risk_probability'] + prob_return(num))
    df['PERCENT NON-PORTIN CUSTOMERS'] = 86*(df['risk_probability'] + prob_return(num))
    df['TOTAL PORTIN CUSTOMERS'] = 1*(df['risk_probability'] + prob_return(num))
    df['PERCENT PORTIN CUSTOMERS'] = 1*(df['risk_probability'] + prob_return(num))
    df['TOTAL PORTIN OTHER CUSTOMERS'] = 1*(df['risk_probability'] + prob_return(num))
    df['PERCENT PORTIN OTHER CUSTOMERS'] = 1*(df['risk_probability'] + prob_return(num))

    df['TOTAL NON-PORTOUT CUSTOMERS'] = 86*(df['risk_probability'] + prob_return(num))
    df['PERCENT NON-PORTOUT CUSTOMERS'] = 0.5*(df['risk_probability'] + prob_return(num))
    df['TOTAL PORTOUT CUSTOMERS'] = 1*(df['risk_probability'] + prob_return(num))
    df['PERCENT PORTOUT CUSTOMERS'] = 1*(df['risk_probability'] + prob_return(num))
    df['TOTAL PORTOUT OTHER CUSTOMERS'] = 1*(df['risk_probability'] + prob_return(num))
    df['PERCENT PORTOUT OTHER CUSTOMERS'] = 1*(df['risk_probability'] + prob_return(num))
    
    
    ############## VO #############
    df['FREE MOBILE USAGE AMOUNT L1M'] = 13500*(df['risk_probability'] + prob_return(num))
    df['OFF-NET MOBILE USAGE AMOUNT L1M'] = 3156*(df['risk_probability'] + prob_return(num))
    df['ON-NET MOBILE USAGE AMOUNT L1M'] = 15500*(df['risk_probability'] + prob_return(num))
    
    ############ PORT #############
    df['NO-PORTIN COUNT'] = prob_return(num)
    df['NO-PORTOUT COUNT'] = prob_return(num)
    df['SINGLE PORTIN COUNT'] = prob_return(num)
    df['SINGLE PORTOUT COUNT'] =prob_return(num)
    
    df['PERCENT NO-PORTIN'] = prob_return(num)
    df['PERCENT NO-PORTOUT'] =prob_return(num)
    df['PERCENT SINGLE PORTIN'] = prob_return(num)
    df['PERCENT SINGLE PORTOUT'] =prob_return(num)
    
    ####### CST ################
    df['CREDIT CARD BAD-DEBT AMOUNT'] = 6200*(df['risk_probability'] + prob_return(num))
    df['CREDIT CARD BAD-DEBT RATIO'] = 700*(df['risk_probability'] + prob_return(num))
    df['CREDIT CARD BILL AMOUNT L1M']  = 6500*(df['risk_probability'] + prob_return(num))
    
    
    df['AVG DEBT TO PAYMENT RATIO']  = 3000*(df['risk_probability'] + prob_return(num))
    df['TOTAL DEBT BY TOTAL PAID']  = 317000*(df['risk_probability'] + prob_return(num))
    
    df['AVG PAID AMOUNT L1M']  = 1500*(df['risk_probability'] + prob_return(num))
    df['TOTAL PAID AMOUNT L1M']  = 3500*(df['risk_probability'] + prob_return(num))
    df['PERCENT DEBT-FREE ACCOUNTS']  = 1.5*(df['risk_probability'] + prob_return(num))
    df['AVG DEBT-FREE ACCOUNTS L1M']  = 1.03*(df['risk_probability'] + prob_return(num))
    df['PERCENT DEBT-FREE ACCOUNTS L1M']  = 1.5*(df['risk_probability'] + prob_return(num))
    
    df['PRIMARY-CHANNEL PAYMENT SHARE L1M']  = 1.53*(df['risk_probability'] + prob_return(num))
    df = create_categorical(df, ['GOV-SALES-VIP-AUH','Growth','Unknown','Missing'], 'CORPORATION SEGMENT')
    df = create_categorical(df, ['1*STAR','4*STAR','2*STAR','PRSTG_MGMT','PRESTIGE','3*STAR','NEW CUST','5*STAR','Unknown','DORMANT','Missing'], 'CUSTOMER REVENUE BAND SEGMENT')
    df = create_categorical(df, ['None', 'EMIRATI BRONZE','UNIDENTIFIED', 'PRESTIGE BY MGMT', 'BRONZE','VVVIP', 'GOLD_SPECIAL_NEEDS', 'EMIRATI GOLD', 'PRESTIGE PLATINUM', 'PRESTIGE Ana Emirati', 'EMIRATI SILVER','EMIRATI WELCOME', 'PRESTIGE SOLITAIRE', 'SILVER', 'GOLD', 'WELCOME','YOUTH', 'Missing'] , 'CUSTOMER PROFIT SEGMENT')
    df = create_categorical(df, ['CONSUMER'], 'CUSTOMER TYPE')
    df = create_categorical(df, ['Diamond','Unknown','Platinum','Gold'], 'CUSTOMER VALUE SEGMENT')
    df = create_categorical(df, ['Unknown', 'BankAdvice', 'Cheque', 'Card', 'Mix', 'Wallet', 'Cash', 'Loyalty', 'None'],'PRIMARY-CHANNEL FOR PAYMENT') 

    return df



