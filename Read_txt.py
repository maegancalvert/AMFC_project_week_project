import pandas as pd

fh = '/home/mcalvert/ABCD3/abcd_lpds01.txt'
poverty = pd.read_csv(fh, sep= '\t', skiprows=[1], low_memory=False)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(poverty['demo_fam_exp1_v2_l'])
print(poverty['demo_fam_exp1_v2_l'].count())