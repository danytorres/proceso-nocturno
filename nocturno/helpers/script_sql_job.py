# ----- VALIDAR Fecha Jobs
t001l_erp = """ 
SELECT storeday , COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.t001l_erp 
GROUP BY 1
ORDER BY 1 desc
"""

mara_erp = """
SELECT mara_ersda , COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.mara_erp 
GROUP BY 1
ORDER BY 1 desc"""

posdw_tlogf_x_cap = """
SELECT posdw_tlogf_x_businessdaydate , COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.posdw_tlogf_x_cap 
GROUP BY 1
ORDER BY 1 desc"""

posdw_tstat_cap = """
SELECT posdw_tstat_businessdaydate , COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.posdw_tstat_cap 
GROUP BY 1
ORDER BY 1 desc"""

mean_erp = """
SELECT  storeday , COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.mean_erp 
GROUP BY 1
ORDER BY 1 desc"""

lfa1_erp = """
SELECT  storeday , COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.lfa1_erp 
GROUP BY 1
ORDER BY 1 desc"""

POSDW_TLOGF_CAP = """
SELECT POSDW_TLOGF_BUSINESSDAYDATE, COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.POSDW_TLOGF_CAP 
GROUP BY 1
ORDER BY 1 desc"""

t161t_erp ="""SELECT storeday , COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.t161t_erp 
GROUP BY 1
ORDER BY 1 desc"""

vbrk_erp = """
select vbrk_erdat , count(*)
from eph_datalake_prod_staging.vbrk_erp 
group by 1
order by 1 desc"""

vbrp_erp = """
select vbrp_erdat ,count(*)
from eph_datalake_prod_staging.vbrp_erp 
group by 1
order by 1 desc"""

# --------Validacion VB's----

# -- ECC
val_vbr = """
select 
vbrp_kursk_dat,
--p.vbrp_werks as str_id,
sum(cast(p.vbrp_netwr as double)) as vta_sn_imp_ecc
from eph_datalake_prod_staging.vbrp_erp p
join eph_datalake_prod_staging.vbrk_erp k ON k.vbrk_vbeln = p.vbrp_vbeln
--where p.vbrp_kursk_dat between '20210501' and '20210530'
group by 1
order by 1 desc"""

# -------------

ekko_erp = """
select ekko_aedat ,count(*)
from eph_datalake_prod_staging.ekko_erp  
group by 1
order by 1 desc"""

ekbe_erp = """
SELECT ekbe_budat ,count(*)
FROM EPH_DATALAKE_PROD_STAGING.ekbe_erp  
GROUP BY 1
ORDER BY 1 desc"""

konp_erp = """
SELECT  storeday storeday , COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.konp_erp 
GROUP BY 1
ORDER BY 1 desc"""

fret_erp = """
SELECT  fret_erfdat , COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.fret_erp 
GROUP BY 1
ORDER BY 1 desc"""

ekpo_erp = """
select ekpo_aedat ,count(*)
from eph_datalake_prod_staging.ekpo_erp  
group by 1
order by 1 desc"""

mseg_erp = """
SELECT mseg_budat_mkpf , COUNT(*)
FROM EPH_DATALAKE_PROD_STAGING.mseg_erp 
GROUP BY 1
ORDER BY 1 desc"""

# ----- VALIDAR transacciones-----

trans_1 = """
select part_date, count(*) from eph_datalake_prod_sales_mdl.audit_sale_trans_line
where 1=1
---and part_date = '2021-08-31'
GROUP BY 1
ORDER BY 1 desc"""

# ------ Transacciones 2----

trans_2 = """
select sale_trans_tot_fact.part_date,
sum(sale_trans_tot_fact.ctdd_trans ) as ctdd_trans 
from  eph_datalake_prod_sales_dim.bild_sale_trans_tot_fact bild_sale_trans_tot_fact
left join eph_datalake_prod_sales_dim.sale_trans_tot_fact sale_trans_tot_fact
on 
			(sale_trans_tot_fact.part_period = bild_sale_trans_tot_fact.part_period) and
            (sale_trans_tot_fact.part_date = bild_sale_trans_tot_fact.part_date) and
            (sale_trans_tot_fact.str_id = bild_sale_trans_tot_fact.str_id) and
            (sale_trans_tot_fact.itm_division_cd = bild_sale_trans_tot_fact.itm_division_cd) and
            (sale_trans_tot_fact.itm_department_cd = bild_sale_trans_tot_fact.itm_department_cd) and
            (sale_trans_tot_fact.firm_flag = bild_sale_trans_tot_fact.firm_flag) and
            (sale_trans_tot_fact.version = bild_sale_trans_tot_fact.version) 
where 1=1
---and sale_trans_tot_fact.part_date = '2021-08-29'
and sale_trans_tot_fact.version = 'ACTUAL'
GROUP BY 1
ORDER BY 1 desc"""

# ------Transacciones 3
trans_3 = """
select * from (
select part_date,
sum(ctdd_trans) as ctdd_trans,
count(*) rowcount
from eph_datalake_prod_sales_semantic.sales_reports_fact
where 1=1
---and part_date = '2021-08-29'
and version = 'ACTUAL'
GROUP BY 1
ORDER BY 1 desc ) where ctdd_trans is not null
"""

# ---Transacciones 4------

# --Viajes_ingresos.csv en capa semantica cambio de base de datos a eph datalake------
trans_4 = """
select * from (
    select  fec_cal, 
            sum(vta_net_rtl) as venta_total, 
            sum(ctdd_trans ) as transacciones 
    from eph_datalake_semantic.vta_dir_fact vdf
    where depto like 'VIAJES %' and version like 'ACTUAL'
    group by fec_cal order by 1 desc
) where venta_total is not null
"""

# ---------Transacciones 5
trans_5 = """
select * from (
select 
part_date, 
sum(vta_net_rtl) as vta_net_rtl,
sum(vta_sn_imp_cpnes) as vta_sn_imp_cpnes,
sum(utl_ant_bonf) as utl_ant_bonf
from eph_datalake_prod_sales_semantic.sales_reports_fact
where 1=1
and version = 'ACTUAL'
and part_date >= '2021-10-01'
group by 1
order by 1 desc ) where vta_net_rtl is not null
"""

jobs = [
    ["t001l_erp", "mara_erp"],
    ["mean_erp", "lfa1_erp"],
    ["t161t_erp", "vbrk_erp", "vbrp_erp", "val_vbr"],
    ["ekko_erp", "ekbe_erp", "konp_erp", "fret_erp", "ekpo_erp"],
    ["mseg_erp"],
    ["posdw_tlogf_x_cap", "posdw_tstat_cap", "POSDW_TLOGF_CAP"]
]

scripts_jobs = [
    [t001l_erp, mara_erp],
    [mean_erp, lfa1_erp],
    [t161t_erp, vbrk_erp, vbrp_erp, val_vbr],
    [ekko_erp, ekbe_erp, konp_erp, fret_erp, ekpo_erp],
    [mseg_erp],
    [posdw_tlogf_x_cap, posdw_tstat_cap, POSDW_TLOGF_CAP]
]

scripts_trans = [trans_1, trans_2, trans_3, trans_5]

script_redshift = trans_4
