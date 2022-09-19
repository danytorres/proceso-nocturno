import graphene
from graphene_django import DjangoObjectType
from procesos.models import *
from nocturno.helpers.mysql_helper import mysql_consultor

class Tabla_23_0Type(DjangoObjectType):
    class Meta:
        model = Tabla_23_0
        fields = "__all__"


class Tabla_0_1Type(DjangoObjectType):
    class Meta:
        model = Tabla_0_1
        fields = "__all__"


class Tabla_1_2Type(DjangoObjectType):
    class Meta:
        model = Tabla_1_2
        fields = "__all__"


class Tabla_2_3Type(DjangoObjectType):
    class Meta:
        model = Tabla_2_3
        fields = "__all__"
        

class Tabla_3_4Type(DjangoObjectType):
    class Meta:
        model = Tabla_3_4
        fields = "__all__"
        
        
class Tabla_4_5Type(DjangoObjectType):
    class Meta:
        model = Tabla_4_5
        fields = "__all__"
        

class StatusType(graphene.ObjectType):
    status_bandera = graphene.String()
    state = graphene.String()
    status_ejecucion = graphene.String()
    storeday = graphene.DateTime()


class Query(graphene.ObjectType):
    all_tabla_1 = graphene.List(Tabla_23_0Type)
    all_tabla_2 = graphene.List(Tabla_0_1Type)
    all_tabla_3 = graphene.List(Tabla_1_2Type)
    all_tabla_4 = graphene.List(Tabla_2_3Type)
    all_tabla_5 = graphene.List(Tabla_3_4Type)
    all_tabla_6 = graphene.List(Tabla_4_5Type)
    status_id = graphene.List(StatusType)
    
    def resolve_all_tabla_1(root, info):
        return Tabla_23_0.objects.all()
    
    def resolve_all_tabla_2(root, info):
        return Tabla_0_1.objects.all()
    
    def resolve_all_tabla_3(root, info):
        return Tabla_1_2.objects.all()
    
    def resolve_all_tabla_4(root, info):
        return Tabla_2_3.objects.all()
    
    def resolve_all_tabla_5(root, info):
        return Tabla_3_4.objects.all()
    
    def resolve_all_tabla_6(root, info):
        return Tabla_4_5.objects.all()

    def resolve_status_id(root, info, id_job):
        fecha_1 = "2022-09-15"
        fecha_2 = "2022-09-16"
        datos_actualizados, datos_otros_procesos = mysql_consultor(fecha_1, fecha_2)
        res = datos_actualizados.get(
            int(id_job) if id_job != '#N/D' else '0', 
            datos_otros_procesos.get(
                int(id_job) if id_job != '#N/D' else '0', 
                'sin datos'
            )
        )
        
        return res
    
schema = graphene.Schema(query=Query)