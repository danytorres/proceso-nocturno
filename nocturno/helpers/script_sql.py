
def ScriptActualizado(fecha):
	script_procesos = f"""
	select p.process_id, p.status, t.state, t.status, p.storeday
	from eph_datalake_prod_datamodel.Process p
	left join 
	(
		select 
		t.table_id_fk, t.state, t.status, max(t.storeday) as storeday 
		from
		eph_datalake_prod_datamodel.Table_Status t 
		join (
			select 
			t.table_id_fk, max(storeday ) as storeday 
			from
			eph_datalake_prod_datamodel.Table_Status t 
			WHERE storeday >= '{fecha} 23:15:00'  /*Dia a concluir*/
			group by 1
		)x
		on t.table_id_fk = x.table_id_fk and  t.storeday = x.storeday
		group by 1,2,3	
	)t
	on p.process_id = t.table_id_fk 
	where p.zone = 'Staging-Zone' and p.process_id >= 1000000 and p.process_id <= 4000000;
	"""

	return script_procesos

def ScriptOtrosProcesos(fecha):
    script = f"""
    select table_id_fk ,status,state , status ,storeday from eph_datalake_prod_datamodel.Table_Status 
	where table_id_fk IN (95,3010130,3010129,3010128,3010127,3010126,3010125,3010124,3010123,3010122,3010121,3010120,3010119,3010118,3010117,3010116,3010115,81,85,86,87)  
	and storeday like '{fecha}%' and state  = 'COMPACTION' and status = 'SUCCESS'
    """
    
    return script