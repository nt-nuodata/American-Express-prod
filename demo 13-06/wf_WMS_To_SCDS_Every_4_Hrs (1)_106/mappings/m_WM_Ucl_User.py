# Databricks notebook source
# MAGIC %run "./udf_informatica"

# COMMAND ----------


from pyspark.sql.types import *

spark.sql("use DELTA_TRAINING")
spark.sql("set spark.sql.legacy.timeParserPolicy = LEGACY")


# COMMAND ----------
# DBTITLE 1, Shortcut_to_WM_UCL_USER_PRE_0


df_0 = spark.sql("""SELECT
  DC_NBR AS DC_NBR,
  UCL_USER_ID AS UCL_USER_ID,
  COMPANY_ID AS COMPANY_ID,
  USER_NAME AS USER_NAME,
  USER_PASSWORD AS USER_PASSWORD,
  IS_ACTIVE AS IS_ACTIVE,
  CREATED_SOURCE_TYPE_ID AS CREATED_SOURCE_TYPE_ID,
  CREATED_SOURCE AS CREATED_SOURCE,
  CREATED_DTTM AS CREATED_DTTM,
  LAST_UPDATED_SOURCE_TYPE_ID AS LAST_UPDATED_SOURCE_TYPE_ID,
  LAST_UPDATED_SOURCE AS LAST_UPDATED_SOURCE,
  LAST_UPDATED_DTTM AS LAST_UPDATED_DTTM,
  USER_TYPE_ID AS USER_TYPE_ID,
  LOCALE_ID AS LOCALE_ID,
  LOCATION_ID AS LOCATION_ID,
  USER_FIRST_NAME AS USER_FIRST_NAME,
  USER_MIDDLE_NAME AS USER_MIDDLE_NAME,
  USER_LAST_NAME AS USER_LAST_NAME,
  USER_PREFIX AS USER_PREFIX,
  USER_TITLE AS USER_TITLE,
  TELEPHONE_NUMBER AS TELEPHONE_NUMBER,
  FAX_NUMBER AS FAX_NUMBER,
  ADDRESS_1 AS ADDRESS_1,
  ADDRESS_2 AS ADDRESS_2,
  CITY AS CITY,
  STATE_PROV_CODE AS STATE_PROV_CODE,
  POSTAL_CODE AS POSTAL_CODE,
  COUNTRY_CODE AS COUNTRY_CODE,
  USER_EMAIL_1 AS USER_EMAIL_1,
  USER_EMAIL_2 AS USER_EMAIL_2,
  COMM_METHOD_ID_DURING_BH_1 AS COMM_METHOD_ID_DURING_BH_1,
  COMM_METHOD_ID_DURING_BH_2 AS COMM_METHOD_ID_DURING_BH_2,
  COMM_METHOD_ID_AFTER_BH_1 AS COMM_METHOD_ID_AFTER_BH_1,
  COMM_METHOD_ID_AFTER_BH_2 AS COMM_METHOD_ID_AFTER_BH_2,
  COMMON_NAME AS COMMON_NAME,
  LAST_PASSWORD_CHANGE_DTTM AS LAST_PASSWORD_CHANGE_DTTM,
  LOGGED_IN AS LOGGED_IN,
  LAST_LOGIN_DTTM AS LAST_LOGIN_DTTM,
  DEFAULT_BUSINESS_UNIT_ID AS DEFAULT_BUSINESS_UNIT_ID,
  DEFAULT_WHSE_REGION_ID AS DEFAULT_WHSE_REGION_ID,
  CHANNEL_ID AS CHANNEL_ID,
  HIBERNATE_VERSION AS HIBERNATE_VERSION,
  NUMBER_OF_INVALID_LOGINS AS NUMBER_OF_INVALID_LOGINS,
  TAX_ID_NBR AS TAX_ID_NBR,
  EMP_START_DATE AS EMP_START_DATE,
  BIRTH_DATE AS BIRTH_DATE,
  GENDER_ID AS GENDER_ID,
  PASSWORD_RESET_DATE_TIME AS PASSWORD_RESET_DATE_TIME,
  PASSWORD_TOKEN AS PASSWORD_TOKEN,
  ISPASSWORDMANAGEDINTERNALLY AS ISPASSWORDMANAGEDINTERNALLY,
  COPY_FROM_USER AS COPY_FROM_USER,
  EXTERNAL_USER_ID AS EXTERNAL_USER_ID,
  SECURITY_POLICY_GROUP_ID AS SECURITY_POLICY_GROUP_ID,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  WM_UCL_USER_PRE""")

df_0.createOrReplaceTempView("Shortcut_to_WM_UCL_USER_PRE_0")

# COMMAND ----------
# DBTITLE 1, SQ_Shortcut_to_WM_UCL_USER_PRE_1


df_1 = spark.sql("""SELECT
  DC_NBR AS DC_NBR,
  UCL_USER_ID AS UCL_USER_ID,
  COMPANY_ID AS COMPANY_ID,
  USER_NAME AS USER_NAME,
  USER_PASSWORD AS USER_PASSWORD,
  IS_ACTIVE AS IS_ACTIVE,
  CREATED_SOURCE_TYPE_ID AS CREATED_SOURCE_TYPE_ID,
  CREATED_SOURCE AS CREATED_SOURCE,
  CREATED_DTTM AS CREATED_DTTM,
  LAST_UPDATED_SOURCE_TYPE_ID AS LAST_UPDATED_SOURCE_TYPE_ID,
  LAST_UPDATED_SOURCE AS LAST_UPDATED_SOURCE,
  LAST_UPDATED_DTTM AS LAST_UPDATED_DTTM,
  USER_TYPE_ID AS USER_TYPE_ID,
  LOCALE_ID AS LOCALE_ID,
  LOCATION_ID AS LOCATION_ID,
  USER_FIRST_NAME AS USER_FIRST_NAME,
  USER_MIDDLE_NAME AS USER_MIDDLE_NAME,
  USER_LAST_NAME AS USER_LAST_NAME,
  USER_PREFIX AS USER_PREFIX,
  USER_TITLE AS USER_TITLE,
  TELEPHONE_NUMBER AS TELEPHONE_NUMBER,
  FAX_NUMBER AS FAX_NUMBER,
  ADDRESS_1 AS ADDRESS_1,
  ADDRESS_2 AS ADDRESS_2,
  CITY AS CITY,
  STATE_PROV_CODE AS STATE_PROV_CODE,
  POSTAL_CODE AS POSTAL_CODE,
  COUNTRY_CODE AS COUNTRY_CODE,
  USER_EMAIL_1 AS USER_EMAIL_1,
  USER_EMAIL_2 AS USER_EMAIL_2,
  COMM_METHOD_ID_DURING_BH_1 AS COMM_METHOD_ID_DURING_BH_1,
  COMM_METHOD_ID_DURING_BH_2 AS COMM_METHOD_ID_DURING_BH_2,
  COMM_METHOD_ID_AFTER_BH_1 AS COMM_METHOD_ID_AFTER_BH_1,
  COMM_METHOD_ID_AFTER_BH_2 AS COMM_METHOD_ID_AFTER_BH_2,
  COMMON_NAME AS COMMON_NAME,
  LAST_PASSWORD_CHANGE_DTTM AS LAST_PASSWORD_CHANGE_DTTM,
  LOGGED_IN AS LOGGED_IN,
  LAST_LOGIN_DTTM AS LAST_LOGIN_DTTM,
  DEFAULT_BUSINESS_UNIT_ID AS DEFAULT_BUSINESS_UNIT_ID,
  DEFAULT_WHSE_REGION_ID AS DEFAULT_WHSE_REGION_ID,
  CHANNEL_ID AS CHANNEL_ID,
  HIBERNATE_VERSION AS HIBERNATE_VERSION,
  NUMBER_OF_INVALID_LOGINS AS NUMBER_OF_INVALID_LOGINS,
  TAX_ID_NBR AS TAX_ID_NBR,
  EMP_START_DATE AS EMP_START_DATE,
  BIRTH_DATE AS BIRTH_DATE,
  GENDER_ID AS GENDER_ID,
  PASSWORD_RESET_DATE_TIME AS PASSWORD_RESET_DATE_TIME,
  PASSWORD_TOKEN AS PASSWORD_TOKEN,
  ISPASSWORDMANAGEDINTERNALLY AS ISPASSWORDMANAGEDINTERNALLY,
  COPY_FROM_USER AS COPY_FROM_USER,
  EXTERNAL_USER_ID AS EXTERNAL_USER_ID,
  SECURITY_POLICY_GROUP_ID AS SECURITY_POLICY_GROUP_ID,
  LOAD_TSTMP AS LOAD_TSTMP,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_WM_UCL_USER_PRE_0""")

df_1.createOrReplaceTempView("SQ_Shortcut_to_WM_UCL_USER_PRE_1")

# COMMAND ----------
# DBTITLE 1, EXP_INT_CONVERSION_2


df_2 = spark.sql("""SELECT
  TO_INTEGER(DC_NBR) AS o_DC_NBR,
  UCL_USER_ID AS UCL_USER_ID,
  COMPANY_ID AS COMPANY_ID,
  USER_NAME AS USER_NAME,
  USER_PASSWORD AS USER_PASSWORD,
  IS_ACTIVE AS IS_ACTIVE,
  CREATED_SOURCE_TYPE_ID AS CREATED_SOURCE_TYPE_ID,
  CREATED_SOURCE AS CREATED_SOURCE,
  CREATED_DTTM AS CREATED_DTTM,
  LAST_UPDATED_SOURCE_TYPE_ID AS LAST_UPDATED_SOURCE_TYPE_ID,
  LAST_UPDATED_SOURCE AS LAST_UPDATED_SOURCE,
  LAST_UPDATED_DTTM AS LAST_UPDATED_DTTM,
  USER_TYPE_ID AS USER_TYPE_ID,
  LOCALE_ID AS LOCALE_ID,
  LOCATION_ID AS LOCATION_ID,
  USER_FIRST_NAME AS USER_FIRST_NAME,
  USER_MIDDLE_NAME AS USER_MIDDLE_NAME,
  USER_LAST_NAME AS USER_LAST_NAME,
  USER_PREFIX AS USER_PREFIX,
  USER_TITLE AS USER_TITLE,
  TELEPHONE_NUMBER AS TELEPHONE_NUMBER,
  FAX_NUMBER AS FAX_NUMBER,
  ADDRESS_1 AS ADDRESS_1,
  ADDRESS_2 AS ADDRESS_2,
  CITY AS CITY,
  STATE_PROV_CODE AS STATE_PROV_CODE,
  POSTAL_CODE AS POSTAL_CODE,
  COUNTRY_CODE AS COUNTRY_CODE,
  USER_EMAIL_1 AS USER_EMAIL_1,
  USER_EMAIL_2 AS USER_EMAIL_2,
  COMM_METHOD_ID_DURING_BH_1 AS COMM_METHOD_ID_DURING_BH_1,
  COMM_METHOD_ID_DURING_BH_2 AS COMM_METHOD_ID_DURING_BH_2,
  COMM_METHOD_ID_AFTER_BH_1 AS COMM_METHOD_ID_AFTER_BH_1,
  COMM_METHOD_ID_AFTER_BH_2 AS COMM_METHOD_ID_AFTER_BH_2,
  COMMON_NAME AS COMMON_NAME,
  LAST_PASSWORD_CHANGE_DTTM AS LAST_PASSWORD_CHANGE_DTTM,
  LOGGED_IN AS LOGGED_IN,
  LAST_LOGIN_DTTM AS LAST_LOGIN_DTTM,
  DEFAULT_BUSINESS_UNIT_ID AS DEFAULT_BUSINESS_UNIT_ID,
  DEFAULT_WHSE_REGION_ID AS DEFAULT_WHSE_REGION_ID,
  CHANNEL_ID AS CHANNEL_ID,
  HIBERNATE_VERSION AS HIBERNATE_VERSION,
  NUMBER_OF_INVALID_LOGINS AS NUMBER_OF_INVALID_LOGINS,
  TAX_ID_NBR AS TAX_ID_NBR,
  EMP_START_DATE AS EMP_START_DATE,
  BIRTH_DATE AS BIRTH_DATE,
  GENDER_ID AS GENDER_ID,
  PASSWORD_RESET_DATE_TIME AS PASSWORD_RESET_DATE_TIME,
  PASSWORD_TOKEN AS PASSWORD_TOKEN,
  ISPASSWORDMANAGEDINTERNALLY AS ISPASSWORDMANAGEDINTERNALLY,
  COPY_FROM_USER AS COPY_FROM_USER,
  EXTERNAL_USER_ID AS EXTERNAL_USER_ID,
  SECURITY_POLICY_GROUP_ID AS SECURITY_POLICY_GROUP_ID,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  SQ_Shortcut_to_WM_UCL_USER_PRE_1""")

df_2.createOrReplaceTempView("EXP_INT_CONVERSION_2")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_WM_UCL_USER1_3


df_3 = spark.sql("""SELECT
  LOCATION_ID AS LOCATION_ID,
  WM_UCL_USER_ID AS WM_UCL_USER_ID,
  WM_COMPANY_ID AS WM_COMPANY_ID,
  WM_LOCATION_ID AS WM_LOCATION_ID,
  WM_LOCALE_ID AS WM_LOCALE_ID,
  WM_USER_TYPE_ID AS WM_USER_TYPE_ID,
  ACTIVE_FLAG AS ACTIVE_FLAG,
  USER_NAME AS USER_NAME,
  TAX_ID_NBR AS TAX_ID_NBR,
  COMMON_NAME AS COMMON_NAME,
  USER_PREFIX AS USER_PREFIX,
  USER_TITLE AS USER_TITLE,
  USER_FIRST_NAME AS USER_FIRST_NAME,
  USER_MIDDLE_NAME AS USER_MIDDLE_NAME,
  USER_LAST_NAME AS USER_LAST_NAME,
  BIRTH_DT AS BIRTH_DT,
  GENDER_ID AS GENDER_ID,
  EMPLOYEE_START_DT AS EMPLOYEE_START_DT,
  ADDR_1 AS ADDR_1,
  ADDR_2 AS ADDR_2,
  CITY AS CITY,
  STATE_PROV_CD AS STATE_PROV_CD,
  POSTAL_CD AS POSTAL_CD,
  COUNTRY_CD AS COUNTRY_CD,
  USER_EMAIL_1 AS USER_EMAIL_1,
  USER_EMAIL_2 AS USER_EMAIL_2,
  PHONE_NBR AS PHONE_NBR,
  FAX_NBR AS FAX_NBR,
  WM_EXTERNAL_USER_ID AS WM_EXTERNAL_USER_ID,
  COPY_FROM_USER AS COPY_FROM_USER,
  WM_SECURITY_POLICY_GROUP_ID AS WM_SECURITY_POLICY_GROUP_ID,
  DEFAULT_WM_BUSINESS_UNIT_ID AS DEFAULT_WM_BUSINESS_UNIT_ID,
  DEFAULT_WM_WHSE_REGION_ID AS DEFAULT_WM_WHSE_REGION_ID,
  WM_CHANNEL_ID AS WM_CHANNEL_ID,
  WM_COMM_METHOD_ID_DURING_BH_1 AS WM_COMM_METHOD_ID_DURING_BH_1,
  WM_COMM_METHOD_ID_DURING_BH_2 AS WM_COMM_METHOD_ID_DURING_BH_2,
  WM_COMM_METHOD_ID_AFTER_BH_1 AS WM_COMM_METHOD_ID_AFTER_BH_1,
  WM_COMM_METHOD_ID_AFTER_BH_2 AS WM_COMM_METHOD_ID_AFTER_BH_2,
  PASSWORD_MANAGED_INTERNALLY_FLAG AS PASSWORD_MANAGED_INTERNALLY_FLAG,
  LOGGED_IN_FLAG AS LOGGED_IN_FLAG,
  LAST_LOGIN_TSTMP AS LAST_LOGIN_TSTMP,
  NUMBER_OF_INVALID_LOGINS AS NUMBER_OF_INVALID_LOGINS,
  PASSWORD_RESET_TSTMP AS PASSWORD_RESET_TSTMP,
  LAST_PASSWORD_CHANGE_TSTMP AS LAST_PASSWORD_CHANGE_TSTMP,
  WM_HIBERNATE_VERSION AS WM_HIBERNATE_VERSION,
  WM_CREATED_SOURCE_TYPE_ID AS WM_CREATED_SOURCE_TYPE_ID,
  WM_CREATED_SOURCE AS WM_CREATED_SOURCE,
  WM_CREATED_TSTMP AS WM_CREATED_TSTMP,
  WM_LAST_UPDATED_SOURCE_TYPE_ID AS WM_LAST_UPDATED_SOURCE_TYPE_ID,
  WM_LAST_UPDATED_SOURCE AS WM_LAST_UPDATED_SOURCE,
  WM_LAST_UPDATED_TSTMP AS WM_LAST_UPDATED_TSTMP,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  WM_UCL_USER""")

df_3.createOrReplaceTempView("Shortcut_to_WM_UCL_USER1_3")

# COMMAND ----------
# DBTITLE 1, SQ_Shortcut_to_WM_UCL_USER_4


df_4 = spark.sql("""SELECT
  LOCATION_ID AS LOCATION_ID,
  WM_UCL_USER_ID AS WM_UCL_USER_ID,
  WM_CREATED_TSTMP AS WM_CREATED_TSTMP,
  WM_LAST_UPDATED_TSTMP AS WM_LAST_UPDATED_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP,
  USER_NAME AS USER_NAME,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_WM_UCL_USER1_3
WHERE
  USER_NAME IN (
    SELECT
      USER_NAME
    FROM
      WM_UCL_USER_PRE
  )""")

df_4.createOrReplaceTempView("SQ_Shortcut_to_WM_UCL_USER_4")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_SITE_PROFILE_5


df_5 = spark.sql("""SELECT
  LOCATION_ID AS LOCATION_ID,
  LOCATION_TYPE_ID AS LOCATION_TYPE_ID,
  STORE_NBR AS STORE_NBR,
  STORE_NAME AS STORE_NAME,
  STORE_TYPE_ID AS STORE_TYPE_ID,
  STORE_OPEN_CLOSE_FLAG AS STORE_OPEN_CLOSE_FLAG,
  COMPANY_ID AS COMPANY_ID,
  REGION_ID AS REGION_ID,
  DISTRICT_ID AS DISTRICT_ID,
  PRICE_ZONE_ID AS PRICE_ZONE_ID,
  PRICE_AD_ZONE_ID AS PRICE_AD_ZONE_ID,
  REPL_DC_NBR AS REPL_DC_NBR,
  REPL_FISH_DC_NBR AS REPL_FISH_DC_NBR,
  REPL_FWD_DC_NBR AS REPL_FWD_DC_NBR,
  SQ_FEET_RETAIL AS SQ_FEET_RETAIL,
  SQ_FEET_TOTAL AS SQ_FEET_TOTAL,
  SITE_ADDRESS AS SITE_ADDRESS,
  SITE_CITY AS SITE_CITY,
  STATE_CD AS STATE_CD,
  COUNTRY_CD AS COUNTRY_CD,
  POSTAL_CD AS POSTAL_CD,
  SITE_MAIN_TELE_NO AS SITE_MAIN_TELE_NO,
  SITE_GROOM_TELE_NO AS SITE_GROOM_TELE_NO,
  SITE_EMAIL_ADDRESS AS SITE_EMAIL_ADDRESS,
  SITE_SALES_FLAG AS SITE_SALES_FLAG,
  EQUINE_MERCH_ID AS EQUINE_MERCH_ID,
  EQUINE_SITE_ID AS EQUINE_SITE_ID,
  EQUINE_SITE_OPEN_DT AS EQUINE_SITE_OPEN_DT,
  GEO_LATITUDE_NBR AS GEO_LATITUDE_NBR,
  GEO_LONGITUDE_NBR AS GEO_LONGITUDE_NBR,
  PETSMART_DMA_CD AS PETSMART_DMA_CD,
  LOYALTY_PGM_TYPE_ID AS LOYALTY_PGM_TYPE_ID,
  LOYALTY_PGM_STATUS_ID AS LOYALTY_PGM_STATUS_ID,
  LOYALTY_PGM_START_DT AS LOYALTY_PGM_START_DT,
  LOYALTY_PGM_CHANGE_DT AS LOYALTY_PGM_CHANGE_DT,
  BP_COMPANY_NBR AS BP_COMPANY_NBR,
  BP_GL_ACCT AS BP_GL_ACCT,
  TP_LOC_FLAG AS TP_LOC_FLAG,
  TP_ACTIVE_CNT AS TP_ACTIVE_CNT,
  PROMO_LABEL_CD AS PROMO_LABEL_CD,
  PARENT_LOCATION_ID AS PARENT_LOCATION_ID,
  LOCATION_NBR AS LOCATION_NBR,
  TIME_ZONE_ID AS TIME_ZONE_ID,
  DELV_SERVICE_CLASS_ID AS DELV_SERVICE_CLASS_ID,
  PICK_SERVICE_CLASS_ID AS PICK_SERVICE_CLASS_ID,
  SITE_LOGIN_ID AS SITE_LOGIN_ID,
  SITE_MANAGER_ID AS SITE_MANAGER_ID,
  SITE_OPEN_YRS_AMT AS SITE_OPEN_YRS_AMT,
  HOTEL_FLAG AS HOTEL_FLAG,
  DAYCAMP_FLAG AS DAYCAMP_FLAG,
  VET_FLAG AS VET_FLAG,
  DIST_MGR_NAME AS DIST_MGR_NAME,
  DIST_SVC_MGR_NAME AS DIST_SVC_MGR_NAME,
  REGION_VP_NAME AS REGION_VP_NAME,
  REGION_TRAINER_NAME AS REGION_TRAINER_NAME,
  ASSET_PROTECT_NAME AS ASSET_PROTECT_NAME,
  SITE_COUNTY AS SITE_COUNTY,
  SITE_FAX_NO AS SITE_FAX_NO,
  SFT_OPEN_DT AS SFT_OPEN_DT,
  DM_EMAIL_ADDRESS AS DM_EMAIL_ADDRESS,
  DSM_EMAIL_ADDRESS AS DSM_EMAIL_ADDRESS,
  RVP_EMAIL_ADDRESS AS RVP_EMAIL_ADDRESS,
  TRADE_AREA AS TRADE_AREA,
  FDLPS_NAME AS FDLPS_NAME,
  FDLPS_EMAIL AS FDLPS_EMAIL,
  OVERSITE_MGR_NAME AS OVERSITE_MGR_NAME,
  OVERSITE_MGR_EMAIL AS OVERSITE_MGR_EMAIL,
  SAFETY_DIRECTOR_NAME AS SAFETY_DIRECTOR_NAME,
  SAFETY_DIRECTOR_EMAIL AS SAFETY_DIRECTOR_EMAIL,
  RETAIL_MANAGER_SAFETY_NAME AS RETAIL_MANAGER_SAFETY_NAME,
  RETAIL_MANAGER_SAFETY_EMAIL AS RETAIL_MANAGER_SAFETY_EMAIL,
  AREA_DIRECTOR_NAME AS AREA_DIRECTOR_NAME,
  AREA_DIRECTOR_EMAIL AS AREA_DIRECTOR_EMAIL,
  DC_GENERAL_MANAGER_NAME AS DC_GENERAL_MANAGER_NAME,
  DC_GENERAL_MANAGER_EMAIL AS DC_GENERAL_MANAGER_EMAIL,
  ASST_DC_GENERAL_MANAGER_NAME1 AS ASST_DC_GENERAL_MANAGER_NAME1,
  ASST_DC_GENERAL_MANAGER_EMAIL1 AS ASST_DC_GENERAL_MANAGER_EMAIL1,
  ASST_DC_GENERAL_MANAGER_NAME2 AS ASST_DC_GENERAL_MANAGER_NAME2,
  ASST_DC_GENERAL_MANAGER_EMAIL2 AS ASST_DC_GENERAL_MANAGER_EMAIL2,
  REGIONAL_DC_SAFETY_MGR_NAME AS REGIONAL_DC_SAFETY_MGR_NAME,
  REGIONAL_DC_SAFETY_MGR_EMAIL AS REGIONAL_DC_SAFETY_MGR_EMAIL,
  DC_PEOPLE_SUPERVISOR_NAME AS DC_PEOPLE_SUPERVISOR_NAME,
  DC_PEOPLE_SUPERVISOR_EMAIL AS DC_PEOPLE_SUPERVISOR_EMAIL,
  PEOPLE_MANAGER_NAME AS PEOPLE_MANAGER_NAME,
  PEOPLE_MANAGER_EMAIL AS PEOPLE_MANAGER_EMAIL,
  ASSET_PROT_DIR_NAME AS ASSET_PROT_DIR_NAME,
  ASSET_PROT_DIR_EMAIL AS ASSET_PROT_DIR_EMAIL,
  SR_REG_ASSET_PROT_MGR_NAME AS SR_REG_ASSET_PROT_MGR_NAME,
  SR_REG_ASSET_PROT_MGR_EMAIL AS SR_REG_ASSET_PROT_MGR_EMAIL,
  REG_ASSET_PROT_MGR_NAME AS REG_ASSET_PROT_MGR_NAME,
  REG_ASSET_PROT_MGR_EMAIL AS REG_ASSET_PROT_MGR_EMAIL,
  ASSET_PROTECT_EMAIL AS ASSET_PROTECT_EMAIL,
  TP_START_DT AS TP_START_DT,
  OPEN_DT AS OPEN_DT,
  GR_OPEN_DT AS GR_OPEN_DT,
  CLOSE_DT AS CLOSE_DT,
  HOTEL_OPEN_DT AS HOTEL_OPEN_DT,
  ADD_DT AS ADD_DT,
  DELETE_DT AS DELETE_DT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT
FROM
  SITE_PROFILE""")

df_5.createOrReplaceTempView("Shortcut_to_SITE_PROFILE_5")

# COMMAND ----------
# DBTITLE 1, SQ_Shortcut_to_SITE_PROFILE_6


df_6 = spark.sql("""SELECT
  LOCATION_ID AS LOCATION_ID,
  STORE_NBR AS STORE_NBR,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_SITE_PROFILE_5""")

df_6.createOrReplaceTempView("SQ_Shortcut_to_SITE_PROFILE_6")

# COMMAND ----------
# DBTITLE 1, JNR_SITE_PROFILE_7


df_7 = spark.sql("""SELECT
  DETAIL.o_DC_NBR AS o_DC_NBR,
  DETAIL.UCL_USER_ID AS UCL_USER_ID,
  DETAIL.COMPANY_ID AS COMPANY_ID,
  DETAIL.USER_NAME AS USER_NAME,
  DETAIL.USER_PASSWORD AS USER_PASSWORD,
  DETAIL.IS_ACTIVE AS IS_ACTIVE,
  DETAIL.CREATED_SOURCE_TYPE_ID AS CREATED_SOURCE_TYPE_ID,
  DETAIL.CREATED_SOURCE AS CREATED_SOURCE,
  DETAIL.CREATED_DTTM AS CREATED_DTTM,
  DETAIL.LAST_UPDATED_SOURCE_TYPE_ID AS LAST_UPDATED_SOURCE_TYPE_ID,
  DETAIL.LAST_UPDATED_SOURCE AS LAST_UPDATED_SOURCE,
  DETAIL.LAST_UPDATED_DTTM AS LAST_UPDATED_DTTM,
  DETAIL.USER_TYPE_ID AS USER_TYPE_ID,
  DETAIL.LOCALE_ID AS LOCALE_ID,
  DETAIL.LOCATION_ID AS LOCATION_ID,
  DETAIL.USER_FIRST_NAME AS USER_FIRST_NAME,
  DETAIL.USER_MIDDLE_NAME AS USER_MIDDLE_NAME,
  DETAIL.USER_LAST_NAME AS USER_LAST_NAME,
  DETAIL.USER_PREFIX AS USER_PREFIX,
  DETAIL.USER_TITLE AS USER_TITLE,
  DETAIL.TELEPHONE_NUMBER AS TELEPHONE_NUMBER,
  DETAIL.FAX_NUMBER AS FAX_NUMBER,
  DETAIL.ADDRESS_1 AS ADDRESS_1,
  DETAIL.ADDRESS_2 AS ADDRESS_2,
  DETAIL.CITY AS CITY,
  DETAIL.STATE_PROV_CODE AS STATE_PROV_CODE,
  DETAIL.POSTAL_CODE AS POSTAL_CODE,
  DETAIL.COUNTRY_CODE AS COUNTRY_CODE,
  DETAIL.USER_EMAIL_1 AS USER_EMAIL_1,
  DETAIL.USER_EMAIL_2 AS USER_EMAIL_2,
  DETAIL.COMM_METHOD_ID_DURING_BH_1 AS COMM_METHOD_ID_DURING_BH_1,
  DETAIL.COMM_METHOD_ID_DURING_BH_2 AS COMM_METHOD_ID_DURING_BH_2,
  DETAIL.COMM_METHOD_ID_AFTER_BH_1 AS COMM_METHOD_ID_AFTER_BH_1,
  DETAIL.COMM_METHOD_ID_AFTER_BH_2 AS COMM_METHOD_ID_AFTER_BH_2,
  DETAIL.COMMON_NAME AS COMMON_NAME,
  DETAIL.LAST_PASSWORD_CHANGE_DTTM AS LAST_PASSWORD_CHANGE_DTTM,
  DETAIL.LOGGED_IN AS LOGGED_IN,
  DETAIL.LAST_LOGIN_DTTM AS LAST_LOGIN_DTTM,
  DETAIL.DEFAULT_BUSINESS_UNIT_ID AS DEFAULT_BUSINESS_UNIT_ID,
  DETAIL.DEFAULT_WHSE_REGION_ID AS DEFAULT_WHSE_REGION_ID,
  DETAIL.CHANNEL_ID AS CHANNEL_ID,
  DETAIL.HIBERNATE_VERSION AS HIBERNATE_VERSION,
  DETAIL.NUMBER_OF_INVALID_LOGINS AS NUMBER_OF_INVALID_LOGINS,
  DETAIL.TAX_ID_NBR AS TAX_ID_NBR,
  DETAIL.EMP_START_DATE AS EMP_START_DATE,
  DETAIL.BIRTH_DATE AS BIRTH_DATE,
  DETAIL.GENDER_ID AS GENDER_ID,
  DETAIL.PASSWORD_RESET_DATE_TIME AS PASSWORD_RESET_DATE_TIME,
  DETAIL.PASSWORD_TOKEN AS PASSWORD_TOKEN,
  DETAIL.ISPASSWORDMANAGEDINTERNALLY AS ISPASSWORDMANAGEDINTERNALLY,
  DETAIL.COPY_FROM_USER AS COPY_FROM_USER,
  DETAIL.EXTERNAL_USER_ID AS EXTERNAL_USER_ID,
  DETAIL.SECURITY_POLICY_GROUP_ID AS SECURITY_POLICY_GROUP_ID,
  MASTER.LOCATION_ID AS LOCATION_ID1,
  MASTER.STORE_NBR AS STORE_NBR,
  MASTER.Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  SQ_Shortcut_to_SITE_PROFILE_6 MASTER
  INNER JOIN EXP_INT_CONVERSION_2 DETAIL ON MASTER.STORE_NBR = DETAIL.o_DC_NBR""")

df_7.createOrReplaceTempView("JNR_SITE_PROFILE_7")

# COMMAND ----------
# DBTITLE 1, JNR_WM_UCL_USER_8


df_8 = spark.sql("""SELECT
  DETAIL.LOCATION_ID1 AS LOCATION_ID1,
  DETAIL.UCL_USER_ID AS UCL_USER_ID,
  DETAIL.COMPANY_ID AS COMPANY_ID,
  DETAIL.USER_NAME AS USER_NAME,
  DETAIL.USER_PASSWORD AS USER_PASSWORD,
  DETAIL.IS_ACTIVE AS IS_ACTIVE,
  DETAIL.CREATED_SOURCE_TYPE_ID AS CREATED_SOURCE_TYPE_ID,
  DETAIL.CREATED_SOURCE AS CREATED_SOURCE,
  DETAIL.CREATED_DTTM AS CREATED_DTTM,
  DETAIL.LAST_UPDATED_SOURCE_TYPE_ID AS LAST_UPDATED_SOURCE_TYPE_ID,
  DETAIL.LAST_UPDATED_SOURCE AS LAST_UPDATED_SOURCE,
  DETAIL.LAST_UPDATED_DTTM AS LAST_UPDATED_DTTM,
  DETAIL.USER_TYPE_ID AS USER_TYPE_ID,
  DETAIL.LOCALE_ID AS LOCALE_ID,
  DETAIL.LOCATION_ID AS LOCATION_ID,
  DETAIL.USER_FIRST_NAME AS USER_FIRST_NAME,
  DETAIL.USER_MIDDLE_NAME AS USER_MIDDLE_NAME,
  DETAIL.USER_LAST_NAME AS USER_LAST_NAME,
  DETAIL.USER_PREFIX AS USER_PREFIX,
  DETAIL.USER_TITLE AS USER_TITLE,
  DETAIL.TELEPHONE_NUMBER AS TELEPHONE_NUMBER,
  DETAIL.FAX_NUMBER AS FAX_NUMBER,
  DETAIL.ADDRESS_1 AS ADDRESS_1,
  DETAIL.ADDRESS_2 AS ADDRESS_2,
  DETAIL.CITY AS CITY,
  DETAIL.STATE_PROV_CODE AS STATE_PROV_CODE,
  DETAIL.POSTAL_CODE AS POSTAL_CODE,
  DETAIL.COUNTRY_CODE AS COUNTRY_CODE,
  DETAIL.USER_EMAIL_1 AS USER_EMAIL_1,
  DETAIL.USER_EMAIL_2 AS USER_EMAIL_2,
  DETAIL.COMM_METHOD_ID_DURING_BH_1 AS COMM_METHOD_ID_DURING_BH_1,
  DETAIL.COMM_METHOD_ID_DURING_BH_2 AS COMM_METHOD_ID_DURING_BH_2,
  DETAIL.COMM_METHOD_ID_AFTER_BH_1 AS COMM_METHOD_ID_AFTER_BH_1,
  DETAIL.COMM_METHOD_ID_AFTER_BH_2 AS COMM_METHOD_ID_AFTER_BH_2,
  DETAIL.COMMON_NAME AS COMMON_NAME,
  DETAIL.LAST_PASSWORD_CHANGE_DTTM AS LAST_PASSWORD_CHANGE_DTTM,
  DETAIL.LOGGED_IN AS LOGGED_IN,
  DETAIL.LAST_LOGIN_DTTM AS LAST_LOGIN_DTTM,
  DETAIL.DEFAULT_BUSINESS_UNIT_ID AS DEFAULT_BUSINESS_UNIT_ID,
  DETAIL.DEFAULT_WHSE_REGION_ID AS DEFAULT_WHSE_REGION_ID,
  DETAIL.CHANNEL_ID AS CHANNEL_ID,
  DETAIL.HIBERNATE_VERSION AS HIBERNATE_VERSION,
  DETAIL.NUMBER_OF_INVALID_LOGINS AS NUMBER_OF_INVALID_LOGINS,
  DETAIL.TAX_ID_NBR AS TAX_ID_NBR,
  DETAIL.EMP_START_DATE AS EMP_START_DATE,
  DETAIL.BIRTH_DATE AS BIRTH_DATE,
  DETAIL.GENDER_ID AS GENDER_ID,
  DETAIL.PASSWORD_RESET_DATE_TIME AS PASSWORD_RESET_DATE_TIME,
  DETAIL.PASSWORD_TOKEN AS PASSWORD_TOKEN,
  DETAIL.ISPASSWORDMANAGEDINTERNALLY AS ISPASSWORDMANAGEDINTERNALLY,
  DETAIL.COPY_FROM_USER AS COPY_FROM_USER,
  DETAIL.EXTERNAL_USER_ID AS EXTERNAL_USER_ID,
  DETAIL.SECURITY_POLICY_GROUP_ID AS SECURITY_POLICY_GROUP_ID,
  MASTER.LOCATION_ID AS i_LOCATION_ID,
  MASTER.WM_UCL_USER_ID AS i_WM_UCL_USER_ID,
  MASTER.WM_CREATED_TSTMP AS i_WM_CREATED_TSTMP,
  MASTER.WM_LAST_UPDATED_TSTMP AS i_WM_LAST_UPDATED_TSTMP,
  MASTER.LOAD_TSTMP AS i_LOAD_TSTMP,
  MASTER.USER_NAME AS i_USER_NAME,
  DETAIL.Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  SQ_Shortcut_to_WM_UCL_USER_4 MASTER
  RIGHT JOIN JNR_SITE_PROFILE_7 DETAIL ON MASTER.LOCATION_ID = DETAIL.LOCATION_ID1
  AND MASTER.USER_NAME = DETAIL.USER_NAME""")

df_8.createOrReplaceTempView("JNR_WM_UCL_USER_8")

# COMMAND ----------
# DBTITLE 1, FIL_UNCHANGED_RECORDS_9


df_9 = spark.sql("""SELECT
  LOCATION_ID1 AS LOCATION_ID1,
  UCL_USER_ID AS UCL_USER_ID,
  COMPANY_ID AS COMPANY_ID,
  USER_NAME AS USER_NAME1,
  USER_PASSWORD AS USER_PASSWORD,
  IS_ACTIVE AS IS_ACTIVE,
  CREATED_SOURCE_TYPE_ID AS CREATED_SOURCE_TYPE_ID,
  CREATED_SOURCE AS CREATED_SOURCE,
  CREATED_DTTM AS CREATED_DTTM,
  LAST_UPDATED_SOURCE_TYPE_ID AS LAST_UPDATED_SOURCE_TYPE_ID,
  LAST_UPDATED_SOURCE AS LAST_UPDATED_SOURCE,
  LAST_UPDATED_DTTM AS LAST_UPDATED_DTTM,
  USER_TYPE_ID AS USER_TYPE_ID,
  LOCALE_ID AS LOCALE_ID,
  LOCATION_ID AS LOCATION_ID2,
  USER_FIRST_NAME AS USER_FIRST_NAME1,
  USER_MIDDLE_NAME AS USER_MIDDLE_NAME1,
  USER_LAST_NAME AS USER_LAST_NAME1,
  USER_PREFIX AS USER_PREFIX1,
  USER_TITLE AS USER_TITLE1,
  TELEPHONE_NUMBER AS TELEPHONE_NUMBER,
  FAX_NUMBER AS FAX_NUMBER,
  ADDRESS_1 AS ADDRESS_11,
  ADDRESS_2 AS ADDRESS_21,
  CITY AS CITY1,
  STATE_PROV_CODE AS STATE_PROV_CODE,
  POSTAL_CODE AS POSTAL_CODE,
  COUNTRY_CODE AS COUNTRY_CODE,
  USER_EMAIL_1 AS USER_EMAIL_11,
  USER_EMAIL_2 AS USER_EMAIL_21,
  COMM_METHOD_ID_DURING_BH_1 AS COMM_METHOD_ID_DURING_BH_1,
  COMM_METHOD_ID_DURING_BH_2 AS COMM_METHOD_ID_DURING_BH_2,
  COMM_METHOD_ID_AFTER_BH_1 AS COMM_METHOD_ID_AFTER_BH_1,
  COMM_METHOD_ID_AFTER_BH_2 AS COMM_METHOD_ID_AFTER_BH_2,
  COMMON_NAME AS COMMON_NAME1,
  LAST_PASSWORD_CHANGE_DTTM AS LAST_PASSWORD_CHANGE_DTTM,
  LOGGED_IN AS LOGGED_IN1,
  LAST_LOGIN_DTTM AS LAST_LOGIN_DTTM,
  DEFAULT_BUSINESS_UNIT_ID AS DEFAULT_BUSINESS_UNIT_ID,
  DEFAULT_WHSE_REGION_ID AS DEFAULT_WHSE_REGION_ID,
  CHANNEL_ID AS CHANNEL_ID,
  HIBERNATE_VERSION AS HIBERNATE_VERSION1,
  NUMBER_OF_INVALID_LOGINS AS NUMBER_OF_INVALID_LOGINS1,
  TAX_ID_NBR AS TAX_ID_NBR,
  EMP_START_DATE AS EMP_START_DATE,
  BIRTH_DATE AS BIRTH_DATE,
  GENDER_ID AS GENDER_ID1,
  PASSWORD_RESET_DATE_TIME AS PASSWORD_RESET_DATE_TIME,
  PASSWORD_TOKEN AS PASSWORD_TOKEN,
  ISPASSWORDMANAGEDINTERNALLY AS ISPASSWORDMANAGEDINTERNALLY,
  COPY_FROM_USER AS COPY_FROM_USER1,
  EXTERNAL_USER_ID AS EXTERNAL_USER_ID,
  SECURITY_POLICY_GROUP_ID AS SECURITY_POLICY_GROUP_ID,
  i_WM_UCL_USER_ID AS i_WM_UCL_USER_ID,
  i_WM_CREATED_TSTMP AS i_WM_CREATED_TSTMP,
  i_WM_LAST_UPDATED_TSTMP AS i_WM_LAST_UPDATED_TSTMP,
  i_LOAD_TSTMP AS i_LOAD_TSTMP,
  i_USER_NAME AS i_USER_NAME1,
  i_LOCATION_ID AS i_LOCATION_ID,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  JNR_WM_UCL_USER_8
WHERE
  ISNULL(i_USER_NAME)
  OR (
    NOT ISNULL(i_USER_NAME)
    AND (
      IFF (
        ISNULL(CREATED_DTTM),
        TO_DATE('01/01/1900', 'MM/DD/YYYY'),
        CREATED_DTTM
      ) != IFF (
        ISNULL(i_WM_CREATED_TSTMP),
        TO_DATE('01/01/1900', 'MM/DD/YYYY'),
        i_WM_CREATED_TSTMP
      )
      OR IFF (
        ISNULL(LAST_UPDATED_DTTM),
        TO_DATE('01/01/1900', 'MM/DD/YYYY'),
        LAST_UPDATED_DTTM
      ) != IFF (
        ISNULL(i_WM_LAST_UPDATED_TSTMP),
        TO_DATE('01/01/1900', 'MM/DD/YYYY'),
        i_WM_LAST_UPDATED_TSTMP
      )
    )
  )""")

df_9.createOrReplaceTempView("FIL_UNCHANGED_RECORDS_9")

# COMMAND ----------
# DBTITLE 1, EXP_UPD_VALIDATOR_10


df_10 = spark.sql("""SELECT
  LOCATION_ID1 AS LOCATION_ID1,
  UCL_USER_ID AS UCL_USER_ID,
  COMPANY_ID AS COMPANY_ID,
  USER_NAME1 AS USER_NAME1,
  USER_PASSWORD AS USER_PASSWORD,
  IS_ACTIVE AS IS_ACTIVE,
  CREATED_SOURCE_TYPE_ID AS CREATED_SOURCE_TYPE_ID,
  CREATED_SOURCE AS CREATED_SOURCE,
  CREATED_DTTM AS CREATED_DTTM,
  LAST_UPDATED_SOURCE_TYPE_ID AS LAST_UPDATED_SOURCE_TYPE_ID,
  LAST_UPDATED_SOURCE AS LAST_UPDATED_SOURCE,
  LAST_UPDATED_DTTM AS LAST_UPDATED_DTTM,
  USER_TYPE_ID AS USER_TYPE_ID,
  LOCALE_ID AS LOCALE_ID,
  LOCATION_ID2 AS LOCATION_ID2,
  USER_FIRST_NAME1 AS USER_FIRST_NAME1,
  USER_MIDDLE_NAME1 AS USER_MIDDLE_NAME1,
  USER_LAST_NAME1 AS USER_LAST_NAME1,
  USER_PREFIX1 AS USER_PREFIX1,
  USER_TITLE1 AS USER_TITLE1,
  TELEPHONE_NUMBER AS TELEPHONE_NUMBER,
  FAX_NUMBER AS FAX_NUMBER,
  ADDRESS_11 AS ADDRESS_11,
  ADDRESS_21 AS ADDRESS_21,
  CITY1 AS CITY1,
  STATE_PROV_CODE AS STATE_PROV_CODE,
  POSTAL_CODE AS POSTAL_CODE,
  COUNTRY_CODE AS COUNTRY_CODE,
  USER_EMAIL_11 AS USER_EMAIL_11,
  USER_EMAIL_21 AS USER_EMAIL_21,
  COMM_METHOD_ID_DURING_BH_1 AS COMM_METHOD_ID_DURING_BH_1,
  COMM_METHOD_ID_DURING_BH_2 AS COMM_METHOD_ID_DURING_BH_2,
  COMM_METHOD_ID_AFTER_BH_1 AS COMM_METHOD_ID_AFTER_BH_1,
  COMM_METHOD_ID_AFTER_BH_2 AS COMM_METHOD_ID_AFTER_BH_2,
  COMMON_NAME1 AS COMMON_NAME1,
  LAST_PASSWORD_CHANGE_DTTM AS LAST_PASSWORD_CHANGE_DTTM,
  LOGGED_IN1 AS LOGGED_IN1,
  LAST_LOGIN_DTTM AS LAST_LOGIN_DTTM,
  DEFAULT_BUSINESS_UNIT_ID AS DEFAULT_BUSINESS_UNIT_ID,
  DEFAULT_WHSE_REGION_ID AS DEFAULT_WHSE_REGION_ID,
  CHANNEL_ID AS CHANNEL_ID,
  HIBERNATE_VERSION1 AS HIBERNATE_VERSION1,
  NUMBER_OF_INVALID_LOGINS1 AS NUMBER_OF_INVALID_LOGINS1,
  TAX_ID_NBR AS TAX_ID_NBR,
  EMP_START_DATE AS EMP_START_DATE,
  BIRTH_DATE AS BIRTH_DATE,
  GENDER_ID1 AS GENDER_ID1,
  PASSWORD_RESET_DATE_TIME AS PASSWORD_RESET_DATE_TIME,
  PASSWORD_TOKEN AS PASSWORD_TOKEN,
  ISPASSWORDMANAGEDINTERNALLY AS ISPASSWORDMANAGEDINTERNALLY,
  COPY_FROM_USER1 AS COPY_FROM_USER1,
  EXTERNAL_USER_ID AS EXTERNAL_USER_ID,
  SECURITY_POLICY_GROUP_ID AS SECURITY_POLICY_GROUP_ID,
  i_USER_NAME1 AS i_USER_NAME1,
  i_LOCATION_ID AS i_LOCATION_ID1,
  now() AS UPDATE_TSTMP,
  IFF(ISNULL(i_LOAD_TSTMP), now(), i_LOAD_TSTMP) AS LOAD_TSTMP,
  IFF(
    (
      ISNULL(i_USER_NAME1)
      AND ISNULL(i_LOCATION_ID)
    ),
    1,
    2
  ) AS o_UPDATE_VALIDATOR,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  FIL_UNCHANGED_RECORDS_9""")

df_10.createOrReplaceTempView("EXP_UPD_VALIDATOR_10")

# COMMAND ----------
# DBTITLE 1, UPD_INS_UPD_11


df_11 = spark.sql("""SELECT
  LOCATION_ID1 AS LOCATION_ID1,
  UCL_USER_ID AS UCL_USER_ID,
  COMPANY_ID AS COMPANY_ID,
  USER_NAME1 AS USER_NAME1,
  USER_PASSWORD AS USER_PASSWORD,
  IS_ACTIVE AS IS_ACTIVE,
  CREATED_SOURCE_TYPE_ID AS CREATED_SOURCE_TYPE_ID,
  CREATED_SOURCE AS CREATED_SOURCE,
  CREATED_DTTM AS CREATED_DTTM,
  LAST_UPDATED_SOURCE_TYPE_ID AS LAST_UPDATED_SOURCE_TYPE_ID,
  LAST_UPDATED_SOURCE AS LAST_UPDATED_SOURCE,
  LAST_UPDATED_DTTM AS LAST_UPDATED_DTTM,
  USER_TYPE_ID AS USER_TYPE_ID,
  LOCALE_ID AS LOCALE_ID,
  LOCATION_ID2 AS LOCATION_ID2,
  USER_FIRST_NAME1 AS USER_FIRST_NAME1,
  USER_MIDDLE_NAME1 AS USER_MIDDLE_NAME1,
  USER_LAST_NAME1 AS USER_LAST_NAME1,
  USER_PREFIX1 AS USER_PREFIX1,
  USER_TITLE1 AS USER_TITLE1,
  TELEPHONE_NUMBER AS TELEPHONE_NUMBER,
  FAX_NUMBER AS FAX_NUMBER,
  ADDRESS_11 AS ADDRESS_11,
  ADDRESS_21 AS ADDRESS_21,
  CITY1 AS CITY1,
  STATE_PROV_CODE AS STATE_PROV_CODE,
  POSTAL_CODE AS POSTAL_CODE,
  COUNTRY_CODE AS COUNTRY_CODE,
  USER_EMAIL_11 AS USER_EMAIL_11,
  USER_EMAIL_21 AS USER_EMAIL_21,
  COMM_METHOD_ID_DURING_BH_1 AS COMM_METHOD_ID_DURING_BH_1,
  COMM_METHOD_ID_DURING_BH_2 AS COMM_METHOD_ID_DURING_BH_2,
  COMM_METHOD_ID_AFTER_BH_1 AS COMM_METHOD_ID_AFTER_BH_1,
  COMM_METHOD_ID_AFTER_BH_2 AS COMM_METHOD_ID_AFTER_BH_2,
  COMMON_NAME1 AS COMMON_NAME1,
  LAST_PASSWORD_CHANGE_DTTM AS LAST_PASSWORD_CHANGE_DTTM,
  LOGGED_IN1 AS LOGGED_IN1,
  LAST_LOGIN_DTTM AS LAST_LOGIN_DTTM,
  DEFAULT_BUSINESS_UNIT_ID AS DEFAULT_BUSINESS_UNIT_ID,
  DEFAULT_WHSE_REGION_ID AS DEFAULT_WHSE_REGION_ID,
  CHANNEL_ID AS CHANNEL_ID,
  HIBERNATE_VERSION1 AS HIBERNATE_VERSION1,
  NUMBER_OF_INVALID_LOGINS1 AS NUMBER_OF_INVALID_LOGINS1,
  TAX_ID_NBR AS TAX_ID_NBR,
  EMP_START_DATE AS EMP_START_DATE,
  BIRTH_DATE AS BIRTH_DATE,
  GENDER_ID1 AS GENDER_ID1,
  PASSWORD_RESET_DATE_TIME AS PASSWORD_RESET_DATE_TIME,
  PASSWORD_TOKEN AS PASSWORD_TOKEN,
  ISPASSWORDMANAGEDINTERNALLY AS ISPASSWORDMANAGEDINTERNALLY,
  COPY_FROM_USER1 AS COPY_FROM_USER1,
  EXTERNAL_USER_ID AS EXTERNAL_USER_ID,
  SECURITY_POLICY_GROUP_ID AS SECURITY_POLICY_GROUP_ID,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP,
  o_UPDATE_VALIDATOR AS o_UPDATE_VALIDATOR,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id,
  DECODE(o_UPDATE_VALIDATOR, 1, 'DD_INSERT', 2, 'DD_UPDATE') AS UPDATE_STRATEGY_FLAG
FROM
  EXP_UPD_VALIDATOR_10""")

df_11.createOrReplaceTempView("UPD_INS_UPD_11")

# COMMAND ----------
# DBTITLE 1, WM_UCL_USER


spark.sql("""MERGE INTO WM_UCL_USER AS TARGET
USING
  UPD_INS_UPD_11 AS SOURCE ON TARGET.USER_NAME = SOURCE.USER_NAME1
  AND TARGET.LOCATION_ID = SOURCE.LOCATION_ID1
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_UPDATE" THEN
UPDATE
SET
  TARGET.LOCATION_ID = SOURCE.LOCATION_ID1,
  TARGET.WM_UCL_USER_ID = SOURCE.UCL_USER_ID,
  TARGET.WM_COMPANY_ID = SOURCE.COMPANY_ID,
  TARGET.WM_LOCATION_ID = SOURCE.LOCATION_ID2,
  TARGET.WM_LOCALE_ID = SOURCE.LOCALE_ID,
  TARGET.WM_USER_TYPE_ID = SOURCE.USER_TYPE_ID,
  TARGET.ACTIVE_FLAG = SOURCE.IS_ACTIVE,
  TARGET.USER_NAME = SOURCE.USER_NAME1,
  TARGET.TAX_ID_NBR = SOURCE.TAX_ID_NBR,
  TARGET.COMMON_NAME = SOURCE.COMMON_NAME1,
  TARGET.USER_PREFIX = SOURCE.USER_PREFIX1,
  TARGET.USER_TITLE = SOURCE.USER_TITLE1,
  TARGET.USER_FIRST_NAME = SOURCE.USER_FIRST_NAME1,
  TARGET.USER_MIDDLE_NAME = SOURCE.USER_MIDDLE_NAME1,
  TARGET.USER_LAST_NAME = SOURCE.USER_LAST_NAME1,
  TARGET.BIRTH_DT = SOURCE.BIRTH_DATE,
  TARGET.GENDER_ID = SOURCE.GENDER_ID1,
  TARGET.EMPLOYEE_START_DT = SOURCE.EMP_START_DATE,
  TARGET.ADDR_1 = SOURCE.ADDRESS_11,
  TARGET.ADDR_2 = SOURCE.ADDRESS_21,
  TARGET.CITY = SOURCE.CITY1,
  TARGET.STATE_PROV_CD = SOURCE.STATE_PROV_CODE,
  TARGET.POSTAL_CD = SOURCE.POSTAL_CODE,
  TARGET.COUNTRY_CD = SOURCE.COUNTRY_CODE,
  TARGET.USER_EMAIL_1 = SOURCE.USER_EMAIL_11,
  TARGET.USER_EMAIL_2 = SOURCE.USER_EMAIL_21,
  TARGET.PHONE_NBR = SOURCE.TELEPHONE_NUMBER,
  TARGET.FAX_NBR = SOURCE.FAX_NUMBER,
  TARGET.WM_EXTERNAL_USER_ID = SOURCE.EXTERNAL_USER_ID,
  TARGET.COPY_FROM_USER = SOURCE.COPY_FROM_USER1,
  TARGET.WM_SECURITY_POLICY_GROUP_ID = SOURCE.SECURITY_POLICY_GROUP_ID,
  TARGET.DEFAULT_WM_BUSINESS_UNIT_ID = SOURCE.DEFAULT_BUSINESS_UNIT_ID,
  TARGET.DEFAULT_WM_WHSE_REGION_ID = SOURCE.DEFAULT_WHSE_REGION_ID,
  TARGET.WM_CHANNEL_ID = SOURCE.CHANNEL_ID,
  TARGET.WM_COMM_METHOD_ID_DURING_BH_1 = SOURCE.COMM_METHOD_ID_DURING_BH_1,
  TARGET.WM_COMM_METHOD_ID_DURING_BH_2 = SOURCE.COMM_METHOD_ID_DURING_BH_2,
  TARGET.WM_COMM_METHOD_ID_AFTER_BH_1 = SOURCE.COMM_METHOD_ID_AFTER_BH_1,
  TARGET.WM_COMM_METHOD_ID_AFTER_BH_2 = SOURCE.COMM_METHOD_ID_AFTER_BH_2,
  TARGET.PASSWORD_MANAGED_INTERNALLY_FLAG = SOURCE.ISPASSWORDMANAGEDINTERNALLY,
  TARGET.LOGGED_IN_FLAG = SOURCE.LOGGED_IN1,
  TARGET.LAST_LOGIN_TSTMP = SOURCE.LAST_LOGIN_DTTM,
  TARGET.NUMBER_OF_INVALID_LOGINS = SOURCE.NUMBER_OF_INVALID_LOGINS1,
  TARGET.PASSWORD_RESET_TSTMP = SOURCE.PASSWORD_RESET_DATE_TIME,
  TARGET.LAST_PASSWORD_CHANGE_TSTMP = SOURCE.LAST_PASSWORD_CHANGE_DTTM,
  TARGET.WM_HIBERNATE_VERSION = SOURCE.HIBERNATE_VERSION1,
  TARGET.WM_CREATED_SOURCE_TYPE_ID = SOURCE.CREATED_SOURCE_TYPE_ID,
  TARGET.WM_CREATED_SOURCE = SOURCE.CREATED_SOURCE,
  TARGET.WM_CREATED_TSTMP = SOURCE.CREATED_DTTM,
  TARGET.WM_LAST_UPDATED_SOURCE_TYPE_ID = SOURCE.LAST_UPDATED_SOURCE_TYPE_ID,
  TARGET.WM_LAST_UPDATED_SOURCE = SOURCE.LAST_UPDATED_SOURCE,
  TARGET.WM_LAST_UPDATED_TSTMP = SOURCE.LAST_UPDATED_DTTM,
  TARGET.UPDATE_TSTMP = SOURCE.UPDATE_TSTMP,
  TARGET.LOAD_TSTMP = SOURCE.LOAD_TSTMP
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_DELETE"
  AND TARGET.WM_UCL_USER_ID = SOURCE.UCL_USER_ID
  AND TARGET.WM_COMPANY_ID = SOURCE.COMPANY_ID
  AND TARGET.WM_LOCATION_ID = SOURCE.LOCATION_ID2
  AND TARGET.WM_LOCALE_ID = SOURCE.LOCALE_ID
  AND TARGET.WM_USER_TYPE_ID = SOURCE.USER_TYPE_ID
  AND TARGET.ACTIVE_FLAG = SOURCE.IS_ACTIVE
  AND TARGET.TAX_ID_NBR = SOURCE.TAX_ID_NBR
  AND TARGET.COMMON_NAME = SOURCE.COMMON_NAME1
  AND TARGET.USER_PREFIX = SOURCE.USER_PREFIX1
  AND TARGET.USER_TITLE = SOURCE.USER_TITLE1
  AND TARGET.USER_FIRST_NAME = SOURCE.USER_FIRST_NAME1
  AND TARGET.USER_MIDDLE_NAME = SOURCE.USER_MIDDLE_NAME1
  AND TARGET.USER_LAST_NAME = SOURCE.USER_LAST_NAME1
  AND TARGET.BIRTH_DT = SOURCE.BIRTH_DATE
  AND TARGET.GENDER_ID = SOURCE.GENDER_ID1
  AND TARGET.EMPLOYEE_START_DT = SOURCE.EMP_START_DATE
  AND TARGET.ADDR_1 = SOURCE.ADDRESS_11
  AND TARGET.ADDR_2 = SOURCE.ADDRESS_21
  AND TARGET.CITY = SOURCE.CITY1
  AND TARGET.STATE_PROV_CD = SOURCE.STATE_PROV_CODE
  AND TARGET.POSTAL_CD = SOURCE.POSTAL_CODE
  AND TARGET.COUNTRY_CD = SOURCE.COUNTRY_CODE
  AND TARGET.USER_EMAIL_1 = SOURCE.USER_EMAIL_11
  AND TARGET.USER_EMAIL_2 = SOURCE.USER_EMAIL_21
  AND TARGET.PHONE_NBR = SOURCE.TELEPHONE_NUMBER
  AND TARGET.FAX_NBR = SOURCE.FAX_NUMBER
  AND TARGET.WM_EXTERNAL_USER_ID = SOURCE.EXTERNAL_USER_ID
  AND TARGET.COPY_FROM_USER = SOURCE.COPY_FROM_USER1
  AND TARGET.WM_SECURITY_POLICY_GROUP_ID = SOURCE.SECURITY_POLICY_GROUP_ID
  AND TARGET.DEFAULT_WM_BUSINESS_UNIT_ID = SOURCE.DEFAULT_BUSINESS_UNIT_ID
  AND TARGET.DEFAULT_WM_WHSE_REGION_ID = SOURCE.DEFAULT_WHSE_REGION_ID
  AND TARGET.WM_CHANNEL_ID = SOURCE.CHANNEL_ID
  AND TARGET.WM_COMM_METHOD_ID_DURING_BH_1 = SOURCE.COMM_METHOD_ID_DURING_BH_1
  AND TARGET.WM_COMM_METHOD_ID_DURING_BH_2 = SOURCE.COMM_METHOD_ID_DURING_BH_2
  AND TARGET.WM_COMM_METHOD_ID_AFTER_BH_1 = SOURCE.COMM_METHOD_ID_AFTER_BH_1
  AND TARGET.WM_COMM_METHOD_ID_AFTER_BH_2 = SOURCE.COMM_METHOD_ID_AFTER_BH_2
  AND TARGET.PASSWORD_MANAGED_INTERNALLY_FLAG = SOURCE.ISPASSWORDMANAGEDINTERNALLY
  AND TARGET.LOGGED_IN_FLAG = SOURCE.LOGGED_IN1
  AND TARGET.LAST_LOGIN_TSTMP = SOURCE.LAST_LOGIN_DTTM
  AND TARGET.NUMBER_OF_INVALID_LOGINS = SOURCE.NUMBER_OF_INVALID_LOGINS1
  AND TARGET.PASSWORD_RESET_TSTMP = SOURCE.PASSWORD_RESET_DATE_TIME
  AND TARGET.LAST_PASSWORD_CHANGE_TSTMP = SOURCE.LAST_PASSWORD_CHANGE_DTTM
  AND TARGET.WM_HIBERNATE_VERSION = SOURCE.HIBERNATE_VERSION1
  AND TARGET.WM_CREATED_SOURCE_TYPE_ID = SOURCE.CREATED_SOURCE_TYPE_ID
  AND TARGET.WM_CREATED_SOURCE = SOURCE.CREATED_SOURCE
  AND TARGET.WM_CREATED_TSTMP = SOURCE.CREATED_DTTM
  AND TARGET.WM_LAST_UPDATED_SOURCE_TYPE_ID = SOURCE.LAST_UPDATED_SOURCE_TYPE_ID
  AND TARGET.WM_LAST_UPDATED_SOURCE = SOURCE.LAST_UPDATED_SOURCE
  AND TARGET.WM_LAST_UPDATED_TSTMP = SOURCE.LAST_UPDATED_DTTM
  AND TARGET.UPDATE_TSTMP = SOURCE.UPDATE_TSTMP
  AND TARGET.LOAD_TSTMP = SOURCE.LOAD_TSTMP THEN DELETE
  WHEN NOT MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_INSERT" THEN
INSERT
  (
    TARGET.LOCATION_ID,
    TARGET.WM_UCL_USER_ID,
    TARGET.WM_COMPANY_ID,
    TARGET.WM_LOCATION_ID,
    TARGET.WM_LOCALE_ID,
    TARGET.WM_USER_TYPE_ID,
    TARGET.ACTIVE_FLAG,
    TARGET.USER_NAME,
    TARGET.TAX_ID_NBR,
    TARGET.COMMON_NAME,
    TARGET.USER_PREFIX,
    TARGET.USER_TITLE,
    TARGET.USER_FIRST_NAME,
    TARGET.USER_MIDDLE_NAME,
    TARGET.USER_LAST_NAME,
    TARGET.BIRTH_DT,
    TARGET.GENDER_ID,
    TARGET.EMPLOYEE_START_DT,
    TARGET.ADDR_1,
    TARGET.ADDR_2,
    TARGET.CITY,
    TARGET.STATE_PROV_CD,
    TARGET.POSTAL_CD,
    TARGET.COUNTRY_CD,
    TARGET.USER_EMAIL_1,
    TARGET.USER_EMAIL_2,
    TARGET.PHONE_NBR,
    TARGET.FAX_NBR,
    TARGET.WM_EXTERNAL_USER_ID,
    TARGET.COPY_FROM_USER,
    TARGET.WM_SECURITY_POLICY_GROUP_ID,
    TARGET.DEFAULT_WM_BUSINESS_UNIT_ID,
    TARGET.DEFAULT_WM_WHSE_REGION_ID,
    TARGET.WM_CHANNEL_ID,
    TARGET.WM_COMM_METHOD_ID_DURING_BH_1,
    TARGET.WM_COMM_METHOD_ID_DURING_BH_2,
    TARGET.WM_COMM_METHOD_ID_AFTER_BH_1,
    TARGET.WM_COMM_METHOD_ID_AFTER_BH_2,
    TARGET.PASSWORD_MANAGED_INTERNALLY_FLAG,
    TARGET.LOGGED_IN_FLAG,
    TARGET.LAST_LOGIN_TSTMP,
    TARGET.NUMBER_OF_INVALID_LOGINS,
    TARGET.PASSWORD_RESET_TSTMP,
    TARGET.LAST_PASSWORD_CHANGE_TSTMP,
    TARGET.WM_HIBERNATE_VERSION,
    TARGET.WM_CREATED_SOURCE_TYPE_ID,
    TARGET.WM_CREATED_SOURCE,
    TARGET.WM_CREATED_TSTMP,
    TARGET.WM_LAST_UPDATED_SOURCE_TYPE_ID,
    TARGET.WM_LAST_UPDATED_SOURCE,
    TARGET.WM_LAST_UPDATED_TSTMP,
    TARGET.UPDATE_TSTMP,
    TARGET.LOAD_TSTMP
  )
VALUES
  (
    SOURCE.LOCATION_ID1,
    SOURCE.UCL_USER_ID,
    SOURCE.COMPANY_ID,
    SOURCE.LOCATION_ID2,
    SOURCE.LOCALE_ID,
    SOURCE.USER_TYPE_ID,
    SOURCE.IS_ACTIVE,
    SOURCE.USER_NAME1,
    SOURCE.TAX_ID_NBR,
    SOURCE.COMMON_NAME1,
    SOURCE.USER_PREFIX1,
    SOURCE.USER_TITLE1,
    SOURCE.USER_FIRST_NAME1,
    SOURCE.USER_MIDDLE_NAME1,
    SOURCE.USER_LAST_NAME1,
    SOURCE.BIRTH_DATE,
    SOURCE.GENDER_ID1,
    SOURCE.EMP_START_DATE,
    SOURCE.ADDRESS_11,
    SOURCE.ADDRESS_21,
    SOURCE.CITY1,
    SOURCE.STATE_PROV_CODE,
    SOURCE.POSTAL_CODE,
    SOURCE.COUNTRY_CODE,
    SOURCE.USER_EMAIL_11,
    SOURCE.USER_EMAIL_21,
    SOURCE.TELEPHONE_NUMBER,
    SOURCE.FAX_NUMBER,
    SOURCE.EXTERNAL_USER_ID,
    SOURCE.COPY_FROM_USER1,
    SOURCE.SECURITY_POLICY_GROUP_ID,
    SOURCE.DEFAULT_BUSINESS_UNIT_ID,
    SOURCE.DEFAULT_WHSE_REGION_ID,
    SOURCE.CHANNEL_ID,
    SOURCE.COMM_METHOD_ID_DURING_BH_1,
    SOURCE.COMM_METHOD_ID_DURING_BH_2,
    SOURCE.COMM_METHOD_ID_AFTER_BH_1,
    SOURCE.COMM_METHOD_ID_AFTER_BH_2,
    SOURCE.ISPASSWORDMANAGEDINTERNALLY,
    SOURCE.LOGGED_IN1,
    SOURCE.LAST_LOGIN_DTTM,
    SOURCE.NUMBER_OF_INVALID_LOGINS1,
    SOURCE.PASSWORD_RESET_DATE_TIME,
    SOURCE.LAST_PASSWORD_CHANGE_DTTM,
    SOURCE.HIBERNATE_VERSION1,
    SOURCE.CREATED_SOURCE_TYPE_ID,
    SOURCE.CREATED_SOURCE,
    SOURCE.CREATED_DTTM,
    SOURCE.LAST_UPDATED_SOURCE_TYPE_ID,
    SOURCE.LAST_UPDATED_SOURCE,
    SOURCE.LAST_UPDATED_DTTM,
    SOURCE.UPDATE_TSTMP,
    SOURCE.LOAD_TSTMP
  )""")