import graphene
from graphene_django import DjangoObjectType
from procesos.models import FechaActual
from nocturno.helpers.resolve import query_objetos


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


class TodayType(DjangoObjectType):
    class Meta:
        model = FechaActual


class ActualizarFecha(graphene.Mutation):
    class Arguments:
        today = graphene.DateTime(required=True)
    
    today = graphene.Field(TodayType)
    
    
    @classmethod
    def mutate(cls, root, info, today):
        today_objeto = FechaActual.objects.get(id=1)
        today_objeto.today = today
        today_objeto.save()
        return ActualizarFecha(today=today_objeto)



class MyMutations(graphene.ObjectType):
    actualizar_fecha = ActualizarFecha.Field()


class Query(graphene.ObjectType):
    status = graphene.Field(StatusType)
    
    
    def resolve_status(root, info):
        return query_objetos()
    
schema = graphene.Schema(query=Query, mutation=MyMutations)