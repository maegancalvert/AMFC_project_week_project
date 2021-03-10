import pandas as pd # to read/manipulate/write data from files
import numpy as np # to manipulate data/generate random numbers
import plotly.express as px # interactive visualizations
import seaborn as sns # static visualizations
import matplotlib.pyplot as plt # fine tune control over visualizations
import json

from pathlib import Path # represent and interact with directories/folders in the operating system
from collections import namedtuple # structure data in an easy to consume way

import requests # retrieve data from an online source



# # save directory we downloaded the ABCD data to `data_path`
data_path = Path("/home/mcalvert/ABCD3")
# #glob (match) all text files in the `data_path` directory
# files = sorted(data_path.glob("*.txt"))
#
# data_elements = []
# data_structures = {}
# event_names = set()
# StructureInfo = namedtuple("StructureInfo", field_names=["description", "eventnames"])
#
# for text_file in files:
#     #print(text_file)
#
#     #Extract data structure from filename
#     data_structure = Path(text_file).name.split('.txt')[0]
#     #print(data_structure)
#     #Read the data structure and capture all the elements from the file
#     #Note this could have been done using the data returned from the NDA API
#     #We are using pandas to read both the first and second rows of the file as the header
#     #Note: by convention dataframe variables contain `df` in the name.
#
#     data_structure_df = pd.read_csv(text_file, sep='\t', header=[0, 1], nrows=0)
#     for data_element, metadata in data_structure_df.columns.values.tolist():
#         data_elements.append([data_element, metadata, data_structure])
#
# #Convert to a Pandas dataframe
# data_elements_df = pd.DataFrame(data_elements, columns=["element", "description", "structure"])
# #print(data_elements_df.head())
#
# data_elements_df.to_csv("/home/mcalvert/ABCD3/data_elements.tsv", sep="\t", index=None)
# #print(data_elements_df.shape)
# #print(len(data_structures))
# #print(event_names)
# #print(data_elements_df.element.unique().shape)
# #print(data_elements_df.query("element == 'smri_vol_scs_amygdalalh'"))
#
# data_structures_str = json.dumps(data_structures)
# with open('/home/mcalvert/ABCD3/data_structures.json', 'w') as fh:
#     fh.write('%s\n' % data_structures_str)

#Load data elements and data structures from disk
fh = '/home/mcalvert/ABCD3/data_elements.tsv'
data_elements_df = pd.read_csv(fh, sep= '\t')

jh = '/home/mcalvert/ABCD3/data_structures.json'
with open(jh) as fh1:
    data = fh1.read()
data_structures = json.loads(data)

# structure = 'abcd_socdev_p_vic01'  # parent report victimization items
# example_structure_df = pd.read_csv(data_path / f"{structure}.txt", sep= '\t', header=[0, 1], nrows=0)
# data_list = example_structure_df.columns.tolist()
# #print(data_list)
#
# structure1 = 'abcd_socdev_child_vic01' #child report victimization items
# example_structure_df1 = pd.read_csv(data_path / f"{structure1}.txt", sep= '\t', header=[0, 1], nrows=0)
# y = example_structure_df1.columns.tolist()
# data_list.append(y)
# #print(data_list)
#
# structure2 = 'abcd_ptsd01' #parent reported adversity
# example_structure_df2 = pd.read_csv(data_path / f"{structure2}.txt", sep= '\t', header=[0, 1], nrows=0)
# y2 = example_structure_df2.columns.tolist()
# data_list.append(y2)
# #print(data_list)
#
# structure3 = 'abcd_lpds01' #economic adversity
# example_structure_df3 = pd.read_csv(data_path / f"{structure3}.txt", sep= '\t', header=[0, 1], nrows=0)
# y3 = example_structure_df3.columns.tolist()
# data_list.append(y3)
# #print(data_list)
#
# structure4 = 'fhxp102' #family mental health history
# example_structure_df4 = pd.read_csv(data_path / f"{structure4}.txt", sep= '\t', header=[0, 1], nrows=0)
# y4 = example_structure_df4.columns.tolist()
# data_list.append(y4)
# #print(data_list)
#
# structure5 = 'fhxp201' #family mental health history
# example_structure_df5 = pd.read_csv(data_path / f"{structure5}.txt", sep= '\t', header=[0, 1], nrows=0)
# y5 = example_structure_df5.columns.tolist()
# data_list.append(y5)
# #print(data_list)
#
# structure6 = 'crpbi01' #acceptance from caregiver
# example_structure_df6 = pd.read_csv(data_path / f"{structure6}.txt", sep= '\t', header=[0, 1], nrows=0)
# y6 = example_structure_df6.columns.tolist()
# data_list.append(y6)
# #print(data_list)
#
# structure7 = 'mriscor02' #resting state correlations
# example_structure_df7= pd.read_csv(data_path / f"{structure7}.txt", sep= '\t', header=[0, 1], nrows=0)
# y7 = example_structure_df7.columns.tolist()
# data_list.append(y7)
# #print(data_list)

common = ["subjectkey", "interview_date", "interview_age", "eventname", "sex"]
demographic = ["site_id_l"]

# Cannot use victimization scales because they are in the year 1 follow-up:
#             'socialdev_pvict_c1', 'socialdev_pvict_c2', 'socialdev_pvict_c3', 'socialdev_pvict_c4', 'socialdev_pvict_c5', 'socialdev_pvict_c6',
#             'socialdev_pvict_c7', 'socialdev_pvict_c8', 'socialdev_pvict_c9', 'socialdev_pvict_p1', 'socialdev_pvict_p2', 'socialdev_pvict_p3',
#             'socialdev_pvict_p4', 'socialdev_pvict_p5', 'socialdev_pvict_p6', 'socialdev_pvict_p7', 'socialdev_pvict_p8', 'socialdev_pvict_w1',
#             'socialdev_pvict_w2', 'socialdev_pvict_w3', 'socialdev_pvict_w4', 'socialdev_pvict_w5', 'socialdev_pvict_w6', 'socialdev_pvict_w8',
#             'socialdev_pvict_g1', 'socialdev_pvict_g2', 'socialdev_pvict_sc1', 'socialdev_pvict_sc2', 'socialdev_pvict_int1', 'socialdev_pvict_int2',
#             'socialdev_cvict_c1', 'socialdev_cvict_c2', 'socialdev_cvict_c3', 'socialdev_pvict_c4',
#             'socialdev_cvict_c5', 'socialdev_cvict_c6',
#             'socialdev_cvict_c7', 'socialdev_cvict_c8', 'socialdev_cvict_c9', 'socialdev_cvict_p1',
#             'socialdev_cvict_p2', 'socialdev_cvict_p3',
#             'socialdev_cvict_p4', 'socialdev_cvict_p5', 'socialdev_cvict_p6', 'socialdev_cvict_p7',
#             'socialdev_cvict_p8', 'socialdev_cvict_w1',
#             'socialdev_cvict_w2', 'socialdev_cvict_w3', 'socialdev_cvict_w4', 'socialdev_cvict_w5',
#             'socialdev_cvict_w6', 'socialdev_cvict_w8',
#             'socialdev_cvict_g1', 'socialdev_cvict_g2', 'socialdev_cvict_sc1', 'socialdev_cvict_sc2',
#             'socialdev_cvict_int1', 'socialdev_cvict_int2',
clinical = ['ksads_ptsd_raw_754_p', 'ksads_ptsd_raw_755_p', 'ksads_ptsd_raw_756_p', 'ksads_ptsd_raw_757_p', 'ksads_ptsd_raw_758_p',
            'ksads_ptsd_raw_759_p', 'ksads_ptsd_raw_760_p', 'ksads_ptsd_raw_761_p', 'ksads_ptsd_raw_762_p', 'ksads_ptsd_raw_763_p',
            'ksads_ptsd_raw_764_p', 'ksads_ptsd_raw_765_p', 'ksads_ptsd_raw_766_p', 'ksads_ptsd_raw_767_p', 'ksads_ptsd_raw_768_p',
            'ksads_ptsd_raw_769_p', 'ksads_ptsd_raw_770_p']

family = ['famhx_ss_fath_prob_alc_p', 'famhx_ss_moth_prob_dg_p', 'asr_scr_anxdisord_r', 'asr_scr_somaticpr_r',
          'asr_scr_depress_r',	'asr_scr_avoidant_r',	'asr_scr_adhd_r',	'asr_scr_antisocial_r',	'asr_scr_inattention_r','asr_scr_hyperactive_r',
### cannot use poverty variables as they were collected after baseline ###
#         'demo_fam_exp1_v2_l', 'demo_fam_exp2_v2_l', 'demo_fam_exp3_v2_l', 'demo_fam_exp4_v2_l', 'demo_fam_exp5_v2_l',
#         'demo_fam_exp6_v2_l', 'demo_fam_exp7_v2_l',
          'fes_youth_q1', 'fes_youth_q2', 'fes_youth_q3', 'fes_youth_q4', 'fes_youth_q5', 'fes_youth_q6', 'fes_youth_q7', 'fes_youth_q8', 'fes_youth_q9',
          'fam_enviro1_p', 'fam_enviro2r_p', 'fam_enviro3_p', 'fam_enviro4r_p', 'fam_enviro5_p', 'fam_enviro6_p', 'fam_enviro7r_p', 'fam_enviro8_p', 'fam_enviro9r_p']

resilience = ['crpbi_parent1_y', 'crpbi_parent2_y', 'crpbi_parent3_y', 'crpbi_parent4_y', 'crpbi_parent5_y',
          'crpbi_caregiver1_y', 'crpbi_caregiver2_y', 'crpbi_caregiver12_y', 'crpbi_caregiver13_y', 'crpbi_caregiver14_y', 'crpbi_caregiver15_y',
          'crpbi_caregiver16_y']
#behavioral = ['prosocial_q2_y', 'prosocial_q3_y'] # 'fit_ss_sleepperiod_minutes', 'fit_ss_avg_hr_deep',
#cognitive = []
imaging = ["rsfmri_cor_ngd_fopa_scs_aglh", "rsfmri_cor_ngd_fopa_scs_agrh"]

data_elements_of_interest = demographic + clinical + family + resilience + imaging #+ behavioral + cognitive
#print(data_elements_of_interest)

structures2read = {}
for element in data_elements_of_interest:
    #print(element)
    item = data_elements_df.query(f"element == '{element}'").structure.values
    #print(item)
    item = item[0]
    #print(' ', item)
    if item not in structures2read.keys():
        structures2read[item] = []
    structures2read[item].append(element)
#print(structures2read)

all_df = None
for structure, elements in structures2read.items():
    data_structure_filtered_df = pd.read_csv(data_path / f"{structure}.txt", sep='\t', skiprows=[1], low_memory=False, usecols=common + elements)
    #print(data_structure_filtered_df)
    data_structure_filtered_df = data_structure_filtered_df.query("eventname == 'baseline_year_1_arm_1'") #("eventname == 'baseline_year_1_arm_1' or eventname == '1_year_follow_up_y_arm_1'")
    if all_df is None:
        all_df = data_structure_filtered_df[["subjectkey", "interview_date", "interview_age", "sex"] + elements]
    else:
        all_df = all_df.merge(data_structure_filtered_df[['subjectkey'] + elements], how='outer')
#print(all_df)

#all_df[all_df.duplicated(subset=['subjectkey'], keep=False)]
nd_all_df = all_df.drop_duplicates(subset=['subjectkey'], keep='first')
#print(nd_all_df)
all_df = all_df.dropna()
#print(nd_all_df.subjectkey.unique().shape)

nd_all_df.to_csv ('/home/mcalvert/ABCD3/all_variables_of_interest.tsv')
pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(nd_all_df.count())
# print(nd_all_df.describe())
# print(nd_all_df.groupby(['sex']).count())


