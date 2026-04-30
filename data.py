import pandas as pd
import numpy as np

######## Importing data ##########
def spot_import(): #Importing spots
    spot1 = pd.read_excel("/Users/hirecheariles/Documents/Cours/Master Finance/Master Thesis/Data/spot_rates_98-24.xls", sheet_name="daily_spot_1", skiprows=1, index_col="Code")
    spot2 = pd.read_excel("/Users/hirecheariles/Documents/Cours/Master Finance/Master Thesis/Data/spot_rates_98-24.xls", skiprows=1, sheet_name="daily_spot_2", index_col="Code")
    return spot1.join(spot2).filter(regex="ER") #Only import columns where finding redular expression "ER"

def spt_dol_import():
    """Convert in USD direct quote all the currencies and cleans NaN"""
    
    spt=spot_import() #importing spots

    #Converting into USD
    spt_dol = 1 / (spt.drop(columns=["USDOLLR(ER)", "PHILPES(ER)", "THABAHT(ER)", "CROATKN(ER)", "BULGLEV(ER)"]).mul(1/spt["USDOLLR(ER)"], axis=0))
                            #We do not convert GBP already evaluated in $ ; no PPP data for PHILPES and THAIBAHT
    spt_dol["GBP(ER)"] = spt["USDOLLR(ER)"] #Including GBP/USD back in the dataframe
    spt_dol["USEURSP(ER)"]=spt["USEURSP(ER)"] #We've tranformed € too which was already quoted in $, so we must revert it back to its initial value

    return spt_dol

def frwd_import(rebal_dates):
    """Import the forward rates midquote from Datastream 1998-2024
    
    Check the mapping
    rebal_dates : define it as you want, to be checked! (2026/03/2024)
    """
    frwd2=pd.read_excel("/Users/hirecheariles/Documents/Cours/Master Finance/International Finance/Project/assignment_fwd_rates_MAJ (2).xlsx", sheet_name="fwd_2", skiprows=1, index_col="Code").filter(regex="ER")
    frwd3=pd.read_excel("/Users/hirecheariles/Documents/Cours/Master Finance/International Finance/Project/assignment_fwd_rates_MAJ (2).xlsx", sheet_name="fwd3", skiprows=1, index_col="Code").filter(regex="ER")
    frwd = frwd2.join(frwd3)
   #frwd = pd.concat([frwd2, frwd3], axis=1)
    frwd = frwd.iloc[1:, ~frwd.columns.str.contains("W")] #Removing weekly forwards

    #Moving data
    cols = frwd.columns.tolist()
    cols.insert(23, cols.pop(6))  # changing index 5 to index 22 (6th column to 23rd position)
    frwd = frwd[cols]

    #Inverting non-EUR, GBP, AUD and NZD currencies
    others = ["TDAUD1M(ER)", "BLEUR1F(ER)", "CLEUR1F(ER)", "TDEUR1M(ER)", "TDNZD1M(ER)", "TDGBP1M(ER)"]
    mask = ~frwd.columns.isin(others) 
    frwd.loc[:, mask] = 1 / frwd.loc[:, mask] #Inverting all the columns except "others"
    
    spt_dol = spt_dol_import()

    #Converting BGN and CLP quotes into USD ones
    eurusd = pd.Series(spt_dol.loc[rebal_dates, "USEURSP(ER)"].values, index=frwd.index) #By default, pandas divides by labels, not by position, so we follow the next steps
    #storing in a series the spot EUR/USD on each rebalancing dates, with the fd indices to match in the division below.
    frwd["BLEUR1F(ER)"] = 1 / (frwd["BLEUR1F(ER)"] / eurusd)
    frwd["CLEUR1F(ER)"] = 1 / (frwd["CLEUR1F(ER)"] / eurusd)  #Dividing by spot EUR/USD rebalancing dates (we don't have spots on the exact 1st day of each month)

    return frwd


def PPP_import():
    df_PPP = pd.read_csv("/Users/hirecheariles/Documents/Cours/Master Finance/Master Thesis/Data/OECD1960PPP.csv", sep=",")
    #print(df_PPP[["CURRENCY", "Currency"]].head(50)) -> if you need to see which tickers correspond to what
    df_PPP = df_PPP[["TIME_PERIOD", "CURRENCY", "OBS_VALUE"]]  #Keeping required data
    df_PPP = df_PPP.pivot_table(index="TIME_PERIOD", columns="CURRENCY")
    df_PPP.columns = df_PPP.columns.droplevel(0)
    df_PPP.index = pd.to_datetime(df_PPP.index, format='%Y') #Getting to datetime type
    return df_PPP 

# def spot_BA():
#     """
#     Importing from reuters full dataset of spot rates, with bid ask spreads, starting earlier.
#     """

#     return df_spot_BA = 

# def frwd_BA():

######### Strategy building ############

def weightsPPPstrat(RERdf, n_long=3, rebal_dates = None, print_short = False):
    """Compute the weights of a PPP strategy from the real exchange rates.
    Make sure that the indices (dates) of your dataframe matches the rebalancing dates.
    
    RERdf : pandas.core.frame.DataFrame
        Dataframe storing the Real Exchange Rates for each country/region
    n_long : int
        number of long (and reciprocally short) assets per date
    """
    if rebal_dates is None:
        rebal_dates = RERdf.index
    
    long = RERdf.apply(lambda r: r.nsmallest(n_long).index, axis=1)
    short = RERdf.apply(lambda r: r.nlargest(n_long).index, axis=1)
    short_data = RERdf.apply(lambda r: r.nlargest(n_long), axis=1) #To check there are no errors
    
    if print_short:
        print(short_data.head(), "")

    weights = pd.DataFrame(0.0, index = rebal_dates, columns = RERdf.columns)
   
    for d in rebal_dates:
        weights.loc[d, long.loc[d]] = 1/n_long
        weights.loc[d, short.loc[d]] = -1/n_long
    
    return weights.shift(1)