import graphene
from procesos.models import FechaActual
from nocturno.helpers.resolve import query_objetos, actualiza_fecha


class TablaType(graphene.ObjectType):
    id_job = graphene.String()
    job = graphene.String()
    carpeta = graphene.String()
    proceso = graphene.String()
    tipo = graphene.String()
    com = graphene.String()
    secuencia = graphene.String()
    hora = graphene.String()
    status_bandera = graphene.String()
    state = graphene.String()
    status_ejec = graphene.String()
    store_day = graphene.DateTime()
        

class StatusType(graphene.ObjectType):
    Tabla_23_0 = graphene.List(TablaType)
    Tabla_0_1 = graphene.List(TablaType)
    Tabla_1_2 = graphene.List(TablaType)
    Tabla_2_3 = graphene.List(TablaType)
    Tabla_3_4 = graphene.List(TablaType)
    Tabla_4_5 = graphene.List(TablaType)
    Tabla_5 = graphene.List(TablaType)


class ActualizarFecha(graphene.Mutation):
    class Arguments:
        fecha = graphene.DateTime()
    
    ok = graphene.Boolean()
    today = graphene.Field(lambda: Today)
    
    def mutate(root, info, fecha):
        ok = True
        today = Today(fecha=fecha)
        return actualiza_fecha(fecha)

class Today(graphene.ObjectType):
    fecha = graphene.DateTime()


class MyMutations(graphene.ObjectType):
    actualizar_fecha = ActualizarFecha.Field()


class Query(graphene.ObjectType):
    status = graphene.Field(StatusType)
    today = graphene.Field(Today)
    
    def resolve_today(root, info):
        return FechaActual.objects.all()[0].today
    
    def resolve_status(root, info):
        return query_objetos()
    
schema = graphene.Schema(query=Query, mutation=MyMutations)