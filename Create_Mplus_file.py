import pandas as pd

fh = 'C:\Users\maeganlrobinson09\Desktop\final.csv'
data = pd.read_csv(fh, sep= ',')

selected_columns = data [["subjectkey", "interview_age", "sex", "site_id_l",
                          'ksads_ptsd_raw_754_p', 'ksads_ptsd_raw_755_p', 'ksads_ptsd_raw_756_p',
                          'ksads_ptsd_raw_757_p', 'ksads_ptsd_raw_758_p',
                          'ksads_ptsd_raw_759_p', 'ksads_ptsd_raw_760_p', 'ksads_ptsd_raw_761_p',
                          'ksads_ptsd_raw_762_p', 'ksads_ptsd_raw_763_p',
                          'ksads_ptsd_raw_764_p', 'ksads_ptsd_raw_765_p', 'ksads_ptsd_raw_766_p',
                          'ksads_ptsd_raw_767_p', 'ksads_ptsd_raw_768_p',
                          'ksads_ptsd_raw_769_p', 'ksads_ptsd_raw_770_p'
                          'famhx_ss_fath_prob_alc_p', 'famhx_ss_moth_prob_alc_p',
                          'famhx_ss_fath_prob_dg_p', 'famhx_ss_moth_prob_dg_p', 'famhx_ss_fath_prob_dprs_p',
                          'famhx_ss_moth_prob_dprs_p', 'famhx_ss_fath_prob_ma_p	', 'famhx_ss_moth_prob_ma_p',
                          'famhx_ss_fath_prob_vs_p', 'famhx_ss_moth_prob_vs_p',
                          'famhx_ss_fath_prob_trb_p', 'famhx_ss_moth_prob_trb_p', 'famhx_ss_fath_prob_nrv_p',
                          'famhx_ss_moth_prob_nrv_p', 'famhx_ss_fath_prob_scd_p',
                          'famhx_ss_moth_prob_scd_p',
                          'asr_scr_anxdisord_r', 'asr_scr_somaticpr_r',
                          'asr_scr_depress_r', 'asr_scr_avoidant_r', 'asr_scr_adhd_r', 'asr_scr_antisocial_r',
                          'asr_scr_inattention_r', 'asr_scr_hyperactive_r',
                          'fes_youth_q1', 'fes_youth_q2', 'fes_youth_q3', 'fes_youth_q4', 'fes_youth_q5',
                          'fes_youth_q6', 'fes_youth_q7', 'fes_youth_q8', 'fes_youth_q9',  # these are yes/no
                          'fam_enviro1_p', 'fam_enviro2r_p', 'fam_enviro3_p', 'fam_enviro4r_p', 'fam_enviro5_p',
                          'fam_enviro6_p', 'fam_enviro7r_p', 'fam_enviro8_p', 'fam_enviro9r_p',
                          'crpbi_parent1_y', 'crpbi_parent2_y', 'crpbi_parent3_y', 'crpbi_parent4_y', 'crpbi_parent5_y',
                          'crpbi_caregiver1_y', 'crpbi_caregiver2_y', 'crpbi_caregiver12_y', 'crpbi_caregiver13_y', 'crpbi_caregiver14_y', 'crpbi_caregiver15_y',
                          'crpbi_caregiver16_y',
                          "rsfmri_cor_ngd_fopa_scs_aglh", "rsfmri_cor_ngd_fopa_scs_agrh"]]

df1 = selected_columns.copy()


df1.to_csv('C:\Users\maeganlrobinson09\Desktop\SEM_df.csv')