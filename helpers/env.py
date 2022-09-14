ENDPOINT = "eph-datalake-prod-datamodel.cxfsarlkejk3.us-east-1.rds.amazonaws.com"
PORT = "3306"
USER = "analiticosbi"
PASSWD = "z9!umps4D37p"
DBNAME = "eph_datalake_prod_datamodel"

script_prueba = """
select p.process_id, p.module, p.process_desc, p.zone, p.status, p.storeday, t.table_id_fk, t.state, t.status, t.records_read, t.storeday 
from eph_datalake_prod_datamodel.Process p
left join 
(
	select 
	t.table_id_fk, t.state, t.status, max(t.records_read) as records_read, max(t.storeday) as storeday 
	from
	eph_datalake_prod_datamodel.Table_Status t 
	join (
		select 
		t.table_id_fk, max(storeday ) as storeday 
		from
		eph_datalake_prod_datamodel.Table_Status t 
 		WHERE storeday >= '2022-09-04 23:15:00'  /*Dia a concluir*/
		group by 1
	)x
	on t.table_id_fk = x.table_id_fk and  t.storeday = x.storeday
	group by 1,2,3	
)t
on p.process_id = t.table_id_fk 
where p.zone = 'Staging-Zone' and p.process_id >= 1000000 and p.process_id <= 4000000;
"""