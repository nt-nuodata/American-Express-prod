# Databricks notebook source
# COMMAND ----------

CREATE DATABASE IF NOT EXISTS DELTA_TRAINING;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.E_DEPT(DEPT_ID_v2 BIGINT,
DEPT_CODE STRING,
DESCRIPTION STRING,
CREATE_DATE_TIME TIMESTAMP,
MOD_DATE_TIME DATE,
USER_ID STRING,
WHSE STRING,
MISC_TXT_1 STRING,
MISC_TXT_2 STRING,
MISC_NUM_1 BIGINT,
MISC_NUM_2 BIGINT,
PERF_GOAL BIGINT,
VERSION_ID BIGINT,
CREATED_DTTM TIMESTAMP,
LAST_UPDATED_DTTM_v2 TIMESTAMP) USING DELTA;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.UCL_USER(UCL_USER_ID BIGINT,
COMPANY_ID BIGINT,
USER_NAME STRING,
USER_PASSWORD STRING,
IS_ACTIVE BIGINT,
CREATED_SOURCE_TYPE_ID BIGINT,
CREATED_SOURCE STRING,
CREATED_DTTM TIMESTAMP,
LAST_UPDATED_SOURCE_TYPE_ID BIGINT,
LAST_UPDATED_SOURCE STRING,
LAST_UPDATED_DTTM TIMESTAMP,
USER_TYPE_ID BIGINT,
LOCALE_ID BIGINT,
LOCATION_ID BIGINT,
USER_FIRST_NAME STRING,
USER_MIDDLE_NAME STRING,
USER_LAST_NAME STRING,
USER_PREFIX STRING,
USER_TITLE STRING,
TELEPHONE_NUMBER STRING,
FAX_NUMBER STRING,
ADDRESS_1 STRING,
ADDRESS_2 STRING,
CITY STRING,
STATE_PROV_CODE STRING,
POSTAL_CODE STRING,
COUNTRY_CODE STRING,
USER_EMAIL_1 STRING,
USER_EMAIL_2 STRING,
COMM_METHOD_ID_DURING_BH_1 BIGINT,
COMM_METHOD_ID_DURING_BH_2 BIGINT,
COMM_METHOD_ID_AFTER_BH_1 BIGINT,
COMM_METHOD_ID_AFTER_BH_2 BIGINT,
COMMON_NAME STRING,
LAST_PASSWORD_CHANGE_DTTM DATE,
LOGGED_IN BIGINT,
LAST_LOGIN_DTTM DATE,
DEFAULT_BUSINESS_UNIT_ID BIGINT,
DEFAULT_WHSE_REGION_ID BIGINT,
CHANNEL_ID BIGINT,
HIBERNATE_VERSION BIGINT,
NUMBER_OF_INVALID_LOGINS BIGINT,
TAX_ID_NBR STRING,
EMP_START_DATE DATE,
BIRTH_DATE DATE,
GENDER_ID STRING,
PASSWORD_RESET_DATE_TIME TIMESTAMP,
PASSWORD_TOKEN STRING,
ISPASSWORDMANAGEDINTERNALLY BIGINT,
COPY_FROM_USER STRING,
EXTERNAL_USER_ID STRING,
SECURITY_POLICY_GROUP_ID BIGINT) USING DELTA;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.E_CONSOL_PERF_SMRY(PERF_SMRY_TRAN_ID BIGINT,
WHSE STRING,
LOGIN_USER_ID STRING,
JOB_FUNCTION_NAME STRING,
SPVSR_LOGIN_USER_ID STRING,
DEPT_CODE STRING,
CLOCK_IN_DATE TIMESTAMP,
CLOCK_IN_STATUS BIGINT,
TOTAL_SAM BIGINT,
TOTAL_PAM BIGINT,
TOTAL_TIME BIGINT,
OSDL BIGINT,
OSIL BIGINT,
NSDL BIGINT,
SIL BIGINT,
UDIL BIGINT,
UIL BIGINT,
ADJ_OSDL BIGINT,
ADJ_OSIL BIGINT,
ADJ_UDIL BIGINT,
ADJ_NSDL BIGINT,
PAID_BRK BIGINT,
UNPAID_BRK BIGINT,
REF_OSDL BIGINT,
REF_OSIL BIGINT,
REF_UDIL BIGINT,
REF_NSDL BIGINT,
REF_ADJ_OSDL BIGINT,
REF_ADJ_OSIL BIGINT,
REF_ADJ_UDIL BIGINT,
REF_ADJ_NSDL BIGINT,
MISC_NUMBER_1 BIGINT,
CREATE_DATE_TIME DATE,
MOD_DATE_TIME DATE,
USER_ID STRING,
MISC_1 STRING,
MISC_2 STRING,
CLOCK_OUT_DATE TIMESTAMP,
SHIFT_CODE STRING,
EVENT_COUNT BIGINT,
START_DATE_TIME TIMESTAMP,
END_DATE_TIME TIMESTAMP,
LEVEL_1 STRING,
LEVEL_2 STRING,
LEVEL_3 STRING,
LEVEL_4 STRING,
LEVEL_5 STRING,
WHSE_DATE DATE,
OPS_CODE STRING,
REF_SAM BIGINT,
REF_PAM BIGINT,
REPORT_SHIFT STRING,
MISC_TXT_1 STRING,
MISC_TXT_2 STRING,
MISC_NUM_1 BIGINT,
MISC_NUM_2 BIGINT,
EVNT_CTGRY_1 STRING,
EVNT_CTGRY_2 STRING,
EVNT_CTGRY_3 STRING,
EVNT_CTGRY_4 STRING,
EVNT_CTGRY_5 STRING,
LABOR_COST_RATE BIGINT,
PAID_OVERLAP_OSDL BIGINT,
UNPAID_OVERLAP_OSDL BIGINT,
PAID_OVERLAP_NSDL BIGINT,
UNPAID_OVERLAP_NSDL BIGINT,
PAID_OVERLAP_OSIL BIGINT,
UNPAID_OVERLAP_OSIL BIGINT,
PAID_OVERLAP_UDIL BIGINT,
UNPAID_OVERLAP_UDIL BIGINT,
VERSION_ID BIGINT,
TEAM_CODE STRING,
DEFAULT_JF_FLAG BIGINT,
EMP_PERF_SMRY_ID BIGINT,
TOTAL_QTY BIGINT,
REF_NBR STRING,
TEAM_BEGIN_TIME TIMESTAMP,
THRUPUT_MIN BIGINT,
DISPLAY_UOM_QTY BIGINT,
DISPLAY_UOM STRING,
LOCN_GRP_ATTR STRING,
RESOURCE_GROUP_ID STRING,
COMP_ASSIGNMENT_ID STRING,
REFLECTIVE_CODE STRING) USING DELTA;

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
LOAD_DT TIMESTAMP) USING DELTA;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.WM_E_CONSOL_PERF_SMRY(LOCATION_ID INT,
WM_PERF_SMRY_TRAN_ID INT,
WM_WHSE STRING,
WM_LOGIN_USER_ID STRING,
WM_JOB_FUNCTION_NAME STRING,
CLOCK_IN_TSTMP TIMESTAMP,
CLOCK_OUT_TSTMP TIMESTAMP,
CLOCK_IN_STATUS INT,
START_TSTMP TIMESTAMP,
END_TSTMP TIMESTAMP,
WHSE_TSTMP TIMESTAMP,
TEAM_BEGIN_TSTMP TIMESTAMP,
WM_SHIFT_CD STRING,
WM_REPORT_SHIFT_CD STRING,
WM_USER_ID STRING,
WM_SPVSR_LOGIN_USER_ID STRING,
WM_DEPT_CD STRING,
WM_RESOURCE_GROUP_ID STRING,
WM_COMP_ASSIGNMENT_ID STRING,
WM_REFLECTIVE_CD STRING,
WM_EMP_PERF_SMRY_ID INT,
WM_LOCN_GRP_ATTR STRING,
WM_VERSION_ID INT,
WM_OPS_CD STRING,
WM_TEAM_CD STRING,
WM_REF_NBR STRING,
DEFAULT_JF_FLAG INT,
EVENT_CNT INT,
TOTAL_SAM INT,
TOTAL_PAM INT,
TOTAL_TIME INT,
TOTAL_QTY INT,
OSDL INT,
OSIL INT,
NSDL INT,
SIL INT,
UDIL INT,
UIL INT,
ADJ_OSDL INT,
ADJ_OSIL INT,
ADJ_UDIL INT,
ADJ_NSDL INT,
PAID_BRK INT,
UNPAID_BRK INT,
REF_OSDL INT,
REF_OSIL INT,
REF_UDIL INT,
REF_NSDL INT,
REF_ADJ_OSDL INT,
REF_ADJ_OSIL INT,
REF_ADJ_UDIL INT,
REF_ADJ_NSDL INT,
REF_SAM INT,
REF_PAM INT,
LABOR_COST_RATE INT,
THRUPUT_MIN INT,
PAID_OVERLAP_OSDL INT,
UNPAID_OVERLAP_OSDL INT,
PAID_OVERLAP_NSDL INT,
UNPAID_OVERLAP_NSDL INT,
PAID_OVERLAP_OSIL INT,
UNPAID_OVERLAP_OSIL INT,
PAID_OVERLAP_UDIL INT,
UNPAID_OVERLAP_UDIL INT,
DISPLAY_UOM_QTY INT,
DISPLAY_UOM STRING,
MISC_1 STRING,
MISC_2 STRING,
MISC_TXT_1 STRING,
MISC_TXT_2 STRING,
MISC_NBR_1 INT,
MISC_NUM_1 INT,
MISC_NUM_2 INT,
LEVEL_1 STRING,
LEVEL_2 STRING,
LEVEL_3 STRING,
LEVEL_4 STRING,
LEVEL_5 STRING,
WM_EVNT_CTGRY_1 STRING,
WM_EVNT_CTGRY_2 STRING,
WM_EVNT_CTGRY_3 STRING,
WM_EVNT_CTGRY_4 STRING,
WM_EVNT_CTGRY_5 STRING,
WM_CREATE_TSTMP TIMESTAMP,
WM_MOD_TSTMP TIMESTAMP,
UPDATE_TSTMP TIMESTAMP,
LOAD_TSTMP TIMESTAMP) USING DELTA;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.WM_E_CONSOL_PERF_SMRY_PRE(DC_NBR INT,
PERF_SMRY_TRAN_ID INT,
WHSE STRING,
LOGIN_USER_ID STRING,
JOB_FUNCTION_NAME STRING,
SPVSR_LOGIN_USER_ID STRING,
DEPT_CODE STRING,
CLOCK_IN_DATE TIMESTAMP,
CLOCK_IN_STATUS INT,
TOTAL_SAM INT,
TOTAL_PAM INT,
TOTAL_TIME INT,
OSDL INT,
OSIL INT,
NSDL INT,
SIL INT,
UDIL INT,
UIL INT,
ADJ_OSDL INT,
ADJ_OSIL INT,
ADJ_UDIL INT,
ADJ_NSDL INT,
PAID_BRK INT,
UNPAID_BRK INT,
REF_OSDL INT,
REF_OSIL INT,
REF_UDIL INT,
REF_NSDL INT,
REF_ADJ_OSDL INT,
REF_ADJ_OSIL INT,
REF_ADJ_UDIL INT,
REF_ADJ_NSDL INT,
MISC_NUMBER_1 INT,
CREATE_DATE_TIME TIMESTAMP,
MOD_DATE_TIME TIMESTAMP,
USER_ID STRING,
MISC_1 STRING,
MISC_2 STRING,
CLOCK_OUT_DATE TIMESTAMP,
SHIFT_CODE STRING,
EVENT_COUNT INT,
START_DATE_TIME TIMESTAMP,
END_DATE_TIME TIMESTAMP,
LEVEL_1 STRING,
LEVEL_2 STRING,
LEVEL_3 STRING,
LEVEL_4 STRING,
LEVEL_5 STRING,
WHSE_DATE TIMESTAMP,
OPS_CODE STRING,
REF_SAM INT,
REF_PAM INT,
REPORT_SHIFT STRING,
MISC_TXT_1 STRING,
MISC_TXT_2 STRING,
MISC_NUM_1 INT,
MISC_NUM_2 INT,
EVNT_CTGRY_1 STRING,
EVNT_CTGRY_2 STRING,
EVNT_CTGRY_3 STRING,
EVNT_CTGRY_4 STRING,
EVNT_CTGRY_5 STRING,
LABOR_COST_RATE INT,
PAID_OVERLAP_OSDL INT,
UNPAID_OVERLAP_OSDL INT,
PAID_OVERLAP_NSDL INT,
UNPAID_OVERLAP_NSDL INT,
PAID_OVERLAP_OSIL INT,
UNPAID_OVERLAP_OSIL INT,
PAID_OVERLAP_UDIL INT,
UNPAID_OVERLAP_UDIL INT,
VERSION_ID INT,
TEAM_CODE STRING,
DEFAULT_JF_FLAG INT,
EMP_PERF_SMRY_ID INT,
TOTAL_QTY INT,
REF_NBR STRING,
TEAM_BEGIN_TIME TIMESTAMP,
THRUPUT_MIN INT,
DISPLAY_UOM_QTY INT,
DISPLAY_UOM STRING,
LOCN_GRP_ATTR STRING,
RESOURCE_GROUP_ID STRING,
COMP_ASSIGNMENT_ID STRING,
REFLECTIVE_CODE STRING,
LOAD_TSTMP TIMESTAMP) USING DELTA;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.WM_UCL_USER(LOCATION_ID INT,
WM_UCL_USER_ID INT,
WM_COMPANY_ID INT,
WM_LOCATION_ID INT,
WM_LOCALE_ID INT,
WM_USER_TYPE_ID INT,
ACTIVE_FLAG INT,
USER_NAME STRING,
TAX_ID_NBR STRING,
COMMON_NAME STRING,
USER_PREFIX STRING,
USER_TITLE STRING,
USER_FIRST_NAME STRING,
USER_MIDDLE_NAME STRING,
USER_LAST_NAME STRING,
BIRTH_DT DATE,
GENDER_ID STRING,
EMPLOYEE_START_DT DATE,
ADDR_1 STRING,
ADDR_2 STRING,
CITY STRING,
STATE_PROV_CD STRING,
POSTAL_CD STRING,
COUNTRY_CD STRING,
USER_EMAIL_1 STRING,
USER_EMAIL_2 STRING,
PHONE_NBR STRING,
FAX_NBR STRING,
WM_EXTERNAL_USER_ID STRING,
COPY_FROM_USER STRING,
WM_SECURITY_POLICY_GROUP_ID INT,
DEFAULT_WM_BUSINESS_UNIT_ID INT,
DEFAULT_WM_WHSE_REGION_ID INT,
WM_CHANNEL_ID INT,
WM_COMM_METHOD_ID_DURING_BH_1 INT,
WM_COMM_METHOD_ID_DURING_BH_2 INT,
WM_COMM_METHOD_ID_AFTER_BH_1 INT,
WM_COMM_METHOD_ID_AFTER_BH_2 INT,
PASSWORD_MANAGED_INTERNALLY_FLAG INT,
LOGGED_IN_FLAG INT,
LAST_LOGIN_TSTMP TIMESTAMP,
NUMBER_OF_INVALID_LOGINS INT,
PASSWORD_RESET_TSTMP TIMESTAMP,
LAST_PASSWORD_CHANGE_TSTMP TIMESTAMP,
WM_HIBERNATE_VERSION INT,
WM_CREATED_SOURCE_TYPE_ID INT,
WM_CREATED_SOURCE STRING,
WM_CREATED_TSTMP TIMESTAMP,
WM_LAST_UPDATED_SOURCE_TYPE_ID INT,
WM_LAST_UPDATED_SOURCE STRING,
WM_LAST_UPDATED_TSTMP TIMESTAMP,
UPDATE_TSTMP TIMESTAMP,
LOAD_TSTMP TIMESTAMP) USING DELTA;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.WM_UCL_USER_PRE(DC_NBR INT,
UCL_USER_ID INT,
COMPANY_ID INT,
USER_NAME STRING,
USER_PASSWORD STRING,
IS_ACTIVE INT,
CREATED_SOURCE_TYPE_ID INT,
CREATED_SOURCE STRING,
CREATED_DTTM TIMESTAMP,
LAST_UPDATED_SOURCE_TYPE_ID INT,
LAST_UPDATED_SOURCE STRING,
LAST_UPDATED_DTTM TIMESTAMP,
USER_TYPE_ID INT,
LOCALE_ID INT,
LOCATION_ID INT,
USER_FIRST_NAME STRING,
USER_MIDDLE_NAME STRING,
USER_LAST_NAME STRING,
USER_PREFIX STRING,
USER_TITLE STRING,
TELEPHONE_NUMBER STRING,
FAX_NUMBER STRING,
ADDRESS_1 STRING,
ADDRESS_2 STRING,
CITY STRING,
STATE_PROV_CODE STRING,
POSTAL_CODE STRING,
COUNTRY_CODE STRING,
USER_EMAIL_1 STRING,
USER_EMAIL_2 STRING,
COMM_METHOD_ID_DURING_BH_1 INT,
COMM_METHOD_ID_DURING_BH_2 INT,
COMM_METHOD_ID_AFTER_BH_1 INT,
COMM_METHOD_ID_AFTER_BH_2 INT,
COMMON_NAME STRING,
LAST_PASSWORD_CHANGE_DTTM TIMESTAMP,
LOGGED_IN INT,
LAST_LOGIN_DTTM TIMESTAMP,
DEFAULT_BUSINESS_UNIT_ID INT,
DEFAULT_WHSE_REGION_ID INT,
CHANNEL_ID INT,
HIBERNATE_VERSION INT,
NUMBER_OF_INVALID_LOGINS INT,
TAX_ID_NBR STRING,
EMP_START_DATE TIMESTAMP,
BIRTH_DATE TIMESTAMP,
GENDER_ID STRING,
PASSWORD_RESET_DATE_TIME TIMESTAMP,
PASSWORD_TOKEN STRING,
ISPASSWORDMANAGEDINTERNALLY INT,
COPY_FROM_USER STRING,
EXTERNAL_USER_ID STRING,
SECURITY_POLICY_GROUP_ID INT,
LOAD_TSTMP TIMESTAMP) USING DELTA;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.WM_E_DEPT(LOCATION_ID INT,
WM_DEPT_ID INT,
WM_WHSE STRING,
WM_DEPT_CD STRING,
WM_DEPT_DESC STRING,
PERF_GOAL INT,
MISC_TXT_1 STRING,
MISC_TXT_2 STRING,
MISC_NUM_1 INT,
MISC_NUM_2 INT,
WM_USER_ID STRING,
WM_VERSION_ID INT,
WM_CREATED_TSTMP TIMESTAMP,
WM_LAST_UPDATED_TSTMP TIMESTAMP,
WM_CREATE_TSTMP TIMESTAMP,
WM_MOD_TSTMP TIMESTAMP,
UPDATE_TSTMP TIMESTAMP,
LOAD_TSTMP TIMESTAMP) USING DELTA;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.WM_E_DEPT_PRE(DC_NBR INT,
DEPT_ID INT,
DEPT_CODE STRING,
DESCRIPTION STRING,
CREATE_DATE_TIME TIMESTAMP,
MOD_DATE_TIME TIMESTAMP,
USER_ID STRING,
WHSE STRING,
MISC_TXT_1 STRING,
MISC_TXT_2 STRING,
MISC_NUM_1 INT,
MISC_NUM_2 INT,
PERF_GOAL INT,
VERSION_ID INT,
CREATED_DTTM TIMESTAMP,
LAST_UPDATED_DTTM TIMESTAMP,
LOAD_TSTMP TIMESTAMP) USING DELTA;

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.DAYS(DAY_DT TIMESTAMP,
BUSINESS_DAY_FLAG STRING,
HOLIDAY_FLAG STRING,
DAY_OF_WK_NAME STRING,
DAY_OF_WK_NAME_ABBR STRING,
DAY_OF_WK_NBR INT,
CAL_DAY_OF_MO_NBR INT,
CAL_DAY_OF_YR_NBR INT,
CAL_WK INT,
CAL_WK_NBR INT,
CAL_MO INT,
CAL_MO_NBR INT,
CAL_MO_NAME STRING,
CAL_MO_NAME_ABBR STRING,
CAL_QTR INT,
CAL_QTR_NBR INT,
CAL_HALF INT,
CAL_YR INT,
FISCAL_DAY_OF_MO_NBR INT,
FISCAL_DAY_OF_YR_NBR INT,
FISCAL_WK INT,
FISCAL_WK_NBR INT,
FISCAL_MO INT,
FISCAL_MO_NBR INT,
FISCAL_MO_NAME STRING,
FISCAL_MO_NAME_ABBR STRING,
FISCAL_QTR INT,
FISCAL_QTR_NBR INT,
FISCAL_HALF INT,
FISCAL_YR INT,
LYR_WEEK_DT TIMESTAMP,
LWK_WEEK_DT TIMESTAMP,
WEEK_DT TIMESTAMP,
EST_TIME_CONV_AMT INT,
EST_TIME_CONV_HRS INT,
ES0_TIME_CONV_AMT INT,
ES0_TIME_CONV_HRS INT,
CST_TIME_CONV_AMT INT,
CST_TIME_CONV_HRS INT,
CS0_TIME_CONV_AMT INT,
CS0_TIME_CONV_HRS INT,
MST_TIME_CONV_AMT INT,
MST_TIME_CONV_HRS INT,
MS0_TIME_CONV_AMT INT,
MS0_TIME_CONV_HRS INT,
PST_TIME_CONV_AMT INT,
PST_TIME_CONV_HRS_v2 INT) USING DELTA;