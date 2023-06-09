# Databricks notebook source
# COMMAND ----------

CREATE DATABASE IF NOT EXISTS DELTA_TRAINING;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.EMPLOYEE_PROFILE_v2(EMPLOYEE_ID_v2 INT,
EMPL_FIRST_NAME STRING,
EMPL_MIDDLE_NAME_v2 STRING,
EMPL_LAST_NAME STRING,
EMPL_BIRTH_DT TIMESTAMP,
GENDER_CD STRING,
PS_MARITAL_STATUS_CD STRING,
ETHNIC_GROUP_ID STRING,
EMPL_ADDR_1 STRING,
EMPL_ADDR_2 STRING,
EMPL_CITY STRING,
EMPL_STATE STRING,
EMPL_PROVINCE STRING,
EMPL_ZIPCODE STRING,
COUNTRY_CD STRING,
EMPL_HOME_PHONE STRING,
EMPL_EMAIL_ADDR STRING,
EMPL_LOGIN_ID STRING,
BADGE_NBR STRING,
EMPL_STATUS_CD STRING,
STATUS_CHG_DT TIMESTAMP,
FULLPT_FLAG STRING,
FULLPT_CHG_DT TIMESTAMP,
EMPL_TYPE_CD STRING,
PS_REG_TEMP_CD STRING,
EMPL_CATEGORY_CD STRING,
EMPL_GROUP_CD STRING,
EMPL_SUBGROUP_CD STRING,
EMPL_HIRE_DT TIMESTAMP,
EMPL_REHIRE_DT TIMESTAMP,
EMPL_TERM_DT TIMESTAMP,
TERM_REASON_CD STRING,
EMPL_SENORITY_DT TIMESTAMP,
PS_ACTION_DT TIMESTAMP,
PS_ACTION_CD STRING,
PS_ACTION_REASON_CD STRING,
LOCATION_ID INT,
LOCATION_CHG_DT TIMESTAMP,
STORE_NBR INT,
STORE_DEPT_NBR STRING,
COMPANY_ID INT,
PS_PERSONNEL_AREA_ID STRING,
PS_PERSONNEL_SUBAREA_ID STRING,
PS_DEPT_CD STRING,
PS_DEPT_CHG_DT TIMESTAMP,
PS_POSITION_ID INT,
POSITION_CHG_DT TIMESTAMP,
PS_SUPERVISOR_ID INT,
JOB_CODE INT,
JOB_CODE_CHG_DT TIMESTAMP,
EMPL_JOB_ENTRY_DT TIMESTAMP,
PS_GRADE_ID INT,
EMPL_STD_BONUS_PCT INT,
EMPL_OVR_BONUS_PCT INT,
EMPL_RATING INT,
PAY_RATE_CHG_DT TIMESTAMP,
PS_PAYROLL_AREA_CD STRING,
PS_TAX_COMPANY_CD STRING,
PS_COMP_FREQ_CD STRING,
COMP_RATE_AMT INT,
ANNUAL_RATE_LOC_AMT INT,
HOURLY_RATE_LOC_AMT INT,
CURRENCY_ID STRING,
EXCH_RATE_PCT INT,
LOAD_TSTMP TIMESTAMP) USING DELTA;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.SITE_PROFILE(LOCATION_ID INT,
LOCATION_TYPE_ID INT,
STORE_NBR INT,
STORE_NAME STRING,
STORE_TYPE_ID STRING,
STORE_OPEN_CLOSE_FLAG STRING,
COMPANY_ID INT,
REGION_ID BIGINT,
DISTRICT_ID BIGINT,
PRICE_ZONE_ID STRING,
PRICE_AD_ZONE_ID STRING,
REPL_DC_NBR INT,
REPL_FISH_DC_NBR INT,
REPL_FWD_DC_NBR INT,
SQ_FEET_RETAIL FLOAT,
SQ_FEET_TOTAL FLOAT,
SITE_ADDRESS STRING,
SITE_CITY STRING,
STATE_CD STRING,
COUNTRY_CD STRING,
POSTAL_CD STRING,
SITE_MAIN_TELE_NO STRING,
SITE_GROOM_TELE_NO STRING,
SITE_EMAIL_ADDRESS STRING,
SITE_SALES_FLAG STRING,
EQUINE_MERCH_ID INT,
EQUINE_SITE_ID INT,
EQUINE_SITE_OPEN_DT TIMESTAMP,
GEO_LATITUDE_NBR INT,
GEO_LONGITUDE_NBR INT,
PETSMART_DMA_CD STRING,
LOYALTY_PGM_TYPE_ID INT,
LOYALTY_PGM_STATUS_ID INT,
LOYALTY_PGM_START_DT TIMESTAMP,
LOYALTY_PGM_CHANGE_DT TIMESTAMP,
BP_COMPANY_NBR INT,
BP_GL_ACCT INT,
TP_LOC_FLAG STRING,
TP_ACTIVE_CNT INT,
PROMO_LABEL_CD STRING,
PARENT_LOCATION_ID INT,
LOCATION_NBR STRING,
TIME_ZONE_ID STRING,
DELV_SERVICE_CLASS_ID STRING,
PICK_SERVICE_CLASS_ID STRING,
SITE_LOGIN_ID STRING,
SITE_MANAGER_ID INT,
SITE_OPEN_YRS_AMT INT,
HOTEL_FLAG INT,
DAYCAMP_FLAG INT,
VET_FLAG INT,
DIST_MGR_NAME STRING,
DIST_SVC_MGR_NAME STRING,
REGION_VP_NAME STRING,
REGION_TRAINER_NAME STRING,
ASSET_PROTECT_NAME STRING,
SITE_COUNTY STRING,
SITE_FAX_NO STRING,
SFT_OPEN_DT TIMESTAMP,
DM_EMAIL_ADDRESS STRING,
DSM_EMAIL_ADDRESS STRING,
RVP_EMAIL_ADDRESS STRING,
TRADE_AREA STRING,
FDLPS_NAME STRING,
FDLPS_EMAIL STRING,
OVERSITE_MGR_NAME STRING,
OVERSITE_MGR_EMAIL STRING,
SAFETY_DIRECTOR_NAME STRING,
SAFETY_DIRECTOR_EMAIL STRING,
RETAIL_MANAGER_SAFETY_NAME STRING,
RETAIL_MANAGER_SAFETY_EMAIL STRING,
AREA_DIRECTOR_NAME STRING,
AREA_DIRECTOR_EMAIL STRING,
DC_GENERAL_MANAGER_NAME STRING,
DC_GENERAL_MANAGER_EMAIL STRING,
ASST_DC_GENERAL_MANAGER_NAME1 STRING,
ASST_DC_GENERAL_MANAGER_EMAIL1 STRING,
ASST_DC_GENERAL_MANAGER_NAME2 STRING,
ASST_DC_GENERAL_MANAGER_EMAIL2 STRING,
REGIONAL_DC_SAFETY_MGR_NAME STRING,
REGIONAL_DC_SAFETY_MGR_EMAIL STRING,
DC_PEOPLE_SUPERVISOR_NAME STRING,
DC_PEOPLE_SUPERVISOR_EMAIL STRING,
PEOPLE_MANAGER_NAME STRING,
PEOPLE_MANAGER_EMAIL STRING,
ASSET_PROT_DIR_NAME STRING,
ASSET_PROT_DIR_EMAIL STRING,
SR_REG_ASSET_PROT_MGR_NAME STRING,
SR_REG_ASSET_PROT_MGR_EMAIL STRING,
REG_ASSET_PROT_MGR_NAME STRING,
REG_ASSET_PROT_MGR_EMAIL STRING,
ASSET_PROTECT_EMAIL STRING,
TP_START_DT TIMESTAMP,
OPEN_DT TIMESTAMP,
GR_OPEN_DT TIMESTAMP,
CLOSE_DT TIMESTAMP,
HOTEL_OPEN_DT TIMESTAMP,
ADD_DT TIMESTAMP,
DELETE_DT TIMESTAMP,
UPDATE_DT TIMESTAMP,
LOAD_DT_v2 TIMESTAMP) USING DELTA;