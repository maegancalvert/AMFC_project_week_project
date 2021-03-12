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
#glob (match) all text files in the `data_path` directory
files = sorted(data_path.glob("*.txt"))

data_elements = []
data_structures = {}
event_names = set()
StructureInfo = namedtuple("StructureInfo", field_names=["description", "eventnames"])

for text_file in files:
    #print(text_file)

    #Extract data structure from filename
    data_structure = Path(text_file).name.split('.txt')[0]
    #print(data_structure)
    #Read the data structure and capture all the elements from the file
    #Note this could have been done using the data returned from the NDA API
    #We are using pandas to read both the first and second rows of the file as the header
    #Note: by convention dataframe variables contain `df` in the name.

    data_structure_df = pd.read_csv(text_file, sep='\t', header=[0, 1], nrows=0)
    for data_element, metadata in data_structure_df.columns.values.tolist():
        data_elements.append([data_element, metadata, data_structure])

#Convert to a Pandas dataframe
data_elements_df = pd.DataFrame(data_elements, columns=["element", "description", "structure"])
#print(data_elements_df.head())

data_elements_df.to_csv("/home/mcalvert/ABCD3/data_elements.tsv", sep="\t", index=None)
data_elements_df.to_csv("/home/mcalvert/ABCD3/data_elements.csv", sep=',', index=None)
#print(data_elements_df.shape)
#print(len(data_structures))
#print(event_names)
#print(data_elements_df.element.unique().shape)
#print(data_elements_df.query("element == 'smri_vol_scs_amygdalalh'"))

data_structures_str = json.dumps(data_structures)
with open('/home/mcalvert/ABCD3/data_structures.json', 'w') as fh:
    fh.write('%s\n' % data_structures_str)

#Load data elements and data structures from disk
fh = '/home/mcalvert/ABCD3/data_elements.tsv'
data_elements_df = pd.read_csv(fh, sep= '\t')

jh = '/home/mcalvert/ABCD3/data_structures.json'
with open(jh) as fh1:
    data = fh1.read()
data_structures = json.loads(data)

common = ["subjectkey", "interview_date", "interview_age", "eventname", "sex"]
demographic = ["site_id_l", 'rel_family_id']
clinical = ['medhx_6i', 'medhx_6p', 'medhx_6j', 'medhx_2m', 'medhx_2h','medhx_2f','medhx_2c','ksads_4_826_p',
            'ksads_4_827_p','ksads_4_828_p','ksads_4_829_p','ksads_4_849_p','ksads_4_850_p','ksads_4_851_p',
            'ksads_4_852_p','ksads_ptsd_raw_754_p', 'ksads_ptsd_raw_755_p',
            'ksads_ptsd_raw_756_p', 'ksads_ptsd_raw_757_p', 'ksads_ptsd_raw_758_p',
            'ksads_ptsd_raw_759_p', 'ksads_ptsd_raw_760_p', 'ksads_ptsd_raw_761_p', 'ksads_ptsd_raw_762_p', 'ksads_ptsd_raw_763_p',
            'ksads_ptsd_raw_764_p', 'ksads_ptsd_raw_765_p', 'ksads_ptsd_raw_766_p', 'ksads_ptsd_raw_767_p', 'ksads_ptsd_raw_768_p',
            'ksads_ptsd_raw_769_p', 'ksads_ptsd_raw_770_p'] #these are yes/no
family = ['famhx_ss_fath_prob_alc_p', 'famhx_ss_moth_prob_alc_p', 'famhx_ss_fath_prob_dg_p', 'famhx_ss_moth_prob_dg_p', 'famhx_ss_fath_prob_dprs_p',
          'famhx_ss_moth_prob_dprs_p', 'famhx_ss_fath_prob_ma_p', 'famhx_ss_moth_prob_ma_p', 'famhx_ss_fath_prob_vs_p', 'famhx_ss_moth_prob_vs_p',
          'famhx_ss_fath_prob_trb_p', 'famhx_ss_moth_prob_trb_p', 'famhx_ss_fath_prob_nrv_p', 'famhx_ss_moth_prob_nrv_p', 'famhx_ss_fath_prob_scd_p',
          'famhx_ss_moth_prob_scd_p', #these are yes/no
          'asr_scr_anxdep_t', 'asr_scr_withdrawn_t', 'asr_scr_somaticpr_t',
          'asr_scr_thought_t',	'asr_scr_attention_t', 'asr_scr_aggressive_t', 'asr_scr_rulebreak_t',
          'asr_scr_intrusive_t', #these are t-scores
          'fes_youth_q1', 'fes_youth_q2', 'fes_youth_q3', 'fes_youth_q4', 'fes_youth_q5', 'fes_youth_q6', 'fes_youth_q7', 'fes_youth_q8', 'fes_youth_q9', #these are yes/no
          'fam_enviro1_p', 'fam_enviro2r_p', 'fam_enviro3_p', 'fam_enviro4r_p', 'fam_enviro5_p', 'fam_enviro6_p', 'fam_enviro7r_p', 'fam_enviro8_p', 'fam_enviro9r_p'] #thes
resilience = ['crpbi_parent1_y', 'crpbi_parent2_y', 'crpbi_parent3_y', 'crpbi_parent4_y', 'crpbi_parent5_y',
          'crpbi_caregiver1_y', 'crpbi_caregiver2_y', 'crpbi_caregiver12_y', 'crpbi_caregiver13_y', 'crpbi_caregiver14_y', 'crpbi_caregiver15_y',
          'crpbi_caregiver16_y'] #rating scale
exclusions = ["imgincl_rsfmri_include",]
imaging = ["rsfmri_cor_ngd_fopa_scs_aglh", "rsfmri_cor_ngd_fopa_scs_agrh"]

data_elements_of_interest = demographic + clinical + family + resilience + imaging + exclusions

structures2read = {}
for element in data_elements_of_interest:
    item = data_elements_df.query(f"element == '{element}'").structure.values[0]
    if item not in structures2read:
        structures2read[item] = []
    structures2read[item].append(element)

all_df = None
for structure, elements in structures2read.items():
    data_structure_filtered_df = pd.read_csv(data_path / f"{structure}.txt", sep='\t', skiprows=[1],
                                             low_memory=False, usecols=common + elements)
    data_structure_filtered_df = data_structure_filtered_df.query("eventname == 'baseline_year_1_arm_1'")
    if all_df is None:
        all_df = data_structure_filtered_df[["subjectkey", "interview_date", "interview_age", "sex"] + elements]
    else:
        all_df = all_df.merge(data_structure_filtered_df[['subjectkey'] + elements], how='outer')

unique_df = all_df.drop_duplicates(subset='subjectkey', keep='first')
#all_df = all_df.dropna()
unique_df.to_csv("/home/mcalvert/ABCD3/all_df.csv", sep=",", index=None)
#print(all_df.shape, all_df.subjectkey.unique().shape)
#print(unique_df.shape)
# keep only if ksads = 0 
ksads_df = unique_df[unique_df["ksads_4_826_p"].isin([0])]  # hallucinations present
ksads_df = ksads_df[ksads_df["ksads_4_827_p"].isin([0])]  # hallucinations past
ksads_df = ksads_df[ksads_df["ksads_4_828_p"].isin([0])]  # delusions present
ksads_df = ksads_df[ksads_df["ksads_4_829_p"].isin([0])]  # delusions past
ksads_df = ksads_df[ksads_df["ksads_4_849_p"].isin([0])]  # assoc. psychotic symptoms present
ksads_df = ksads_df[ksads_df["ksads_4_850_p"].isin([0])]  # assoc. psychotic symptoms past
ksads_df = ksads_df[ksads_df["ksads_4_851_p"].isin([0])]  # diagnosis scizophrenia spectrum present
ksads_df = ksads_df[ksads_df["ksads_4_852_p"].isin([0])]  # diagnosis scizophrenia spectrum past

#ksads_df.shape, ksads_df.subjectkey.unique().shape

# med history, 0=no, 1=yes
med_df = ksads_df[ksads_df["medhx_6i"].isin([0])]  # head injury
med_df = med_df[med_df["medhx_6p"].isin([0])]  # seizure
med_df = med_df[med_df["medhx_6j"].isin([0])]  # knocked unconscius
med_df = med_df[med_df["medhx_2m"].isin([0])]  # MS
med_df = med_df[med_df["medhx_2h"].isin([0])]  # epilepsy or seizures
med_df = med_df[med_df["medhx_2f"].isin([0])]  # cerebral palsy
med_df = med_df[med_df["medhx_2c"].isin([0])]  # brain injury

#med_df.shape, med_df.subjectkey.unique().shape

# rec for inclusion?, 0 =no, 1 = yes
qc_df = med_df[med_df["imgincl_rsfmri_include"].isin([1])]
#qc_df.shape, qc_df.subjectkey.unique().shape

# drop sibs
subj_df = qc_df.drop_duplicates(subset='rel_family_id', keep='first')
print(subj_df.shape)

#subj_df.shape, subj_df.subjectkey.unique().shape

subj_df.to_csv("/home/mcalvert/ABCD3/final_df.csv", sep=",", index=None)
