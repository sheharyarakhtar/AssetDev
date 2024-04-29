def generate_data(num):
    random.seed(10)
    df = pd.DataFrame({'party_id':[i for i in range(num)],
                      'risk_probability': [random.uniform(a = 0, b = 1) for i in range(num)]
                      })
    
    df['high_risk_flag'] = [0 if i<0.50 else 1 for i in df['risk_probability']]
    ##################### BILL  ##############################
    df['BILL_OUTSTANDING_M1_avg'] = 5000*(df['risk_probability'] + prob_return(num) )
    df['BILL_AMT_M1_avg'] = 4000*(df['risk_probability'] + prob_return(num) )
    df['BILL_RENTALS_M1_avg'] = 700*(df['risk_probability'] + prob_return(num) )
    df['BILL_RENTALS_M2_avg'] = 1700*(df['risk_probability'] + prob_return(num) )
    df['BILL_RENTALS_M3_avg'] = 1600*(df['risk_probability'] + prob_return(num) )
    df['BILL_RENTALS_M4_avg'] = 400*(df['risk_probability'] + prob_return(num) )
    df['BILL_RENTALS_M5_avg'] = 350*(df['risk_probability'] + prob_return(num) )
    df['BILL_RENTALS_M6_avg'] = 400*(df['risk_probability'] + prob_return(num) )
    df['BILL_USAGE_CHRGS_M1_avg'] = 0.02*(df['risk_probability'] + prob_return(num) )
    df['BILL_USAGE_CHRGS_M2_avg'] = 0.2*(df['risk_probability'] + prob_return(num) )
    df['BILL_USAGE_CHRGS_M3_avg'] = 0.2*(df['risk_probability'] + prob_return(num) )
    df['BILL_USAGE_CHRGS_M4_avg'] = 0.15*(df['risk_probability'] + prob_return(num) )
    df['BILL_USAGE_CHRGS_M5_avg'] = 1300*(df['risk_probability'] + prob_return(num) )
    df['BILL_USAGE_CHRGS_M6_avg'] = 1400*(df['risk_probability'] + prob_return(num) )
    df['BILL_OUTSTANDING_M1_sum'] = 5000*(df['risk_probability'] + prob_return(num) )
    df['BILL_OUTSTANDING_M3_avg'] = 3500*(df['risk_probability'] + prob_return(num) )
    df['BILL_OUTSTANDING_M3_sum'] = 7000*(df['risk_probability'] + prob_return(num) )
    df['BILL_OUTSTANDING_M6_avg'] = 3000*(df['risk_probability'] + prob_return(num) )
    df['BILL_OUTSTANDING_M6_sum'] = 4000*(df['risk_probability'] + prob_return(num) )
    ########### ACTV ##############
    df['ACTV_30_DYS_avg'] = df['risk_probability'] + prob_return(num)
    df['ACTV_60_DYS_avg'] = df['risk_probability'] + prob_return(num)
    df['ACTV_90_DYS_avg'] = df['risk_probability'] + prob_return(num)
    df['ACTV_30_DYS_norm'] = 50*(df['risk_probability'] + prob_return(num))
    df['ACTV_60_DYS_norm'] = 100*(df['risk_probability'] + prob_return(num))
    df['ACTV_90_DYS_norm'] = 25*(df['risk_probability'] + prob_return(num))
    
    ########### ARPU #################
    df['ARPU_12_avg'] = 350*(df['risk_probability'] + prob_return(num))
    df['ARPU_1_avg'] = 3000*(df['risk_probability'] + prob_return(num))
    df['ARPU_3_avg'] = 150*(df['risk_probability'] + prob_return(num))
    df['ARPU_6_avg'] = 2000*(df['risk_probability'] + prob_return(num))
    df['ARPU_12_sum'] = 200*(df['risk_probability'] + prob_return(num))
    df['ARPU_1_sum'] = 325*(df['risk_probability'] + prob_return(num))
    df['ARPU_3_sum'] = 150*(df['risk_probability'] + prob_return(num))
    df['ARPU_6_sum'] = 3500*(df['risk_probability'] + prob_return(num))
    df
    ############# FLG ##############
    df['BAR_FLG_M6_N_norm'] = 97*(df['risk_probability'] + prob_return(num))
    df['BAR_FLG_M6_Y_norm'] = 52*(df['risk_probability'] + prob_return(num))
    df['BAR_FLG_N_norm'] = 1*(df['risk_probability'] + prob_return(num))
    df['BAR_FLG_Y_norm'] = 1*(df['risk_probability'] + prob_return(num))
    df['CC_CARD_FLG_count']  = 1*(df['risk_probability'] + prob_return(num))
    df['CST_CAT_FLG_EP_norm'] = 73*(df['risk_probability'] + prob_return(num))
    df['CST_CAT_FLG_NP_norm'] = 87*(df['risk_probability'] + prob_return(num))
    df['PORTIN_N_FLG_count'] = 0.5*(df['risk_probability'] + prob_return(num))
    df['PORTIN_N_FLG_norm'] = 86*(df['risk_probability'] + prob_return(num))
    df['PORTIN_Other_FLG_count'] = 1*(df['risk_probability'] + prob_return(num))
    df['PORTIN_Other_FLG_norm'] = 1*(df['risk_probability'] + prob_return(num))
    df['PORTIN_Y_FLG_count'] = 1*(df['risk_probability'] + prob_return(num))
    df['PORTIN_Y_FLG_norm'] = 1*(df['risk_probability'] + prob_return(num))
    df['PORTOUT_N_FLG_count'] = 0.5*(df['risk_probability'] + prob_return(num))
    df['PORTOUT_N_FLG_norm'] = 86*(df['risk_probability'] + prob_return(num))
    df['PORTOUT_Other_FLG_count'] = 1*(df['risk_probability'] + prob_return(num))
    df['PORTOUT_Other_FLG_norm'] = 1*(df['risk_probability'] + prob_return(num))
    df['PORTOUT_Y_FLG_count'] = 1*(df['risk_probability'] + prob_return(num))
    df['PORTOUT_Y_FLG_norm'] = 1*(df['risk_probability'] + prob_return(num))
    
    
    ############## VO #############
    df['VO_MOB_MOU_FREE_M1'] = 13500*(df['risk_probability'] + prob_return(num))
    df['VO_MOB_MOU_OFFNT_M1'] = 3156*(df['risk_probability'] + prob_return(num))
    df['VO_MOB_MOU_ONNT_M1'] = 15500*(df['risk_probability'] + prob_return(num))
    
    ############ PORT #############
    df['MNP_PORT_IN_0_count'] = prob_return(num)
    df['MNP_PORT_OUT_0_count'] = prob_return(num)
    df['MNP_PORT_IN_1_count'] = prob_return(num)
    df['MNP_PORT_OUT_1_count'] =prob_return(num)
    df['MNP_PORT_IN_0_norm'] = prob_return(num)
    df['MNP_PORT_OUT_0_norm'] =prob_return(num)
    df['MNP_PORT_IN_1_norm'] = prob_return(num)
    df['MNP_PORT_OUT_1_norm'] =prob_return(num)
    
    df['PORTIN_N_FLG_count']=0.5*(df['risk_probability'] + prob_return(num))
    df['PORTIN_N_FLG_norm']=86*(df['risk_probability'] + prob_return(num))
    df['PORTIN_Y_FLG_count'] =prob_return(num)
    df['PORTIN_Y_FLG_norm']=prob_return(num)
    df['PORTIN_Other_FLG_count']=prob_return(num)
    df['PORTIN_Other_FLG_norm']=prob_return(num)
    
    
    df['PORTOUT_N_FLG_count']=0.5*(df['risk_probability'] + prob_return(num))
    df['PORTOUT_N_FLG_norm']=86*(df['risk_probability'] + prob_return(num))
    df['PORTOUT_Y_FLG_count'] =prob_return(num)
    df['PORTOUT_Y_FLG_norm']=prob_return(num)
    df['PORTOUT_Other_FLG_count']=prob_return(num)
    df['PORTOUT_Other_FLG_norm']=prob_return(num)
    
    ####### CST ################
    df['CST_BAD_DEBT_AMT'] = 6200*(df['risk_probability'] + prob_return(num))
    df['CST_BAD_DEBT_RATIO'] = 700*(df['risk_probability'] + prob_return(num))
    df['CST_BILL_AMT_M1']  = 6500*(df['risk_probability'] + prob_return(num))
    
    
    df['OS_TO_PMNT_RATIO_avg']  = 3000*(df['risk_probability'] + prob_return(num))
    df['OS_TO_PMNT_RATIO_norm']  = 317000*(df['risk_probability'] + prob_return(num))
    df['PMNT_AMT_M1_avg']  = 1500*(df['risk_probability'] + prob_return(num))
    df['PMNT_AMT_M1_sum']  = 3500*(df['risk_probability'] + prob_return(num))
    df['PMNT_CHNL_CNT_M1_max']  = 1.5*(df['risk_probability'] + prob_return(num))
    df['PMNT_CNT_M1_avg']  = 1.03*(df['risk_probability'] + prob_return(num))
    df['PMNT_CNT_M1_max']  = 1.5*(df['risk_probability'] + prob_return(num))
    df['TOP_CHNL_TOT_PMNT_RAT_M1_avg']  = 1.53*(df['risk_probability'] + prob_return(num))
    
    df['FNP_portin_count'] = abs(10*np.random.normal(size = num)).astype(int)
    df['FNP_portin_norm'] = abs(10*np.random.normal(size = num)).astype(int)
    df['FNP_portout_count'] = abs(10*np.random.normal(size = num)).astype(int)
    df['FNP_portout_norm'] = abs(10*np.random.normal(size = num)).astype(int)
    df = create_categorical(df, ['GOV-SALES-VIP-AUH','Growth','Unknown','Missing'], 'CST_CORP_SEG_mode')
    df = create_categorical(df, ['1*STAR','4*STAR','2*STAR','PRSTG_MGMT','PRESTIGE','3*STAR','NEW CUST','5*STAR','Unknown','DORMANT','Missing'], 'CST_PFT_ARPU_BAND_mode')
    df = create_categorical(df, ['None', 'EMIRATI BRONZE','UNIDENTIFIED', 'PRESTIGE BY MGMT', 'BRONZE','VVVIP', 'GOLD_SPECIAL_NEEDS', 'EMIRATI GOLD', 'PRESTIGE PLATINUM', 'PRESTIGE Ana Emirati', 'EMIRATI SILVER','EMIRATI WELCOME', 'PRESTIGE SOLITAIRE', 'SILVER', 'GOLD', 'WELCOME','YOUTH', 'Missing'] , 'CST_PFT_ARPU_SEG_mode')
    df = create_categorical(df, ['CONSUMER'], 'CST_SEG_TP_mode')
    df = create_categorical(df, ['Diamond','Unknown','Platinum','Gold'], 'CST_VAL_SEG_mode')
    df = create_categorical(df, ['Unknown', 'BankAdvice', 'Cheque', 'Card', 'Mix', 'Wallet', 'Cash', 'Loyalty', 'None'],'PMNT_TOP_CHNL_M1_mode') 

    return df



