import players.schema
import products.schema
import book.schema
import graphene


class Query(
    players.schema.Query, 
    book.schema.Query, 
    products.schema.Query,
    graphene.ObjectType
):
    pass 


class Mutation(
    players.schema.Mutation, 
    book.schema.Mutation, 
    products.schema.Mutation,
    graphene.ObjectType
):
    pass 

schema = graphene.Schema(query=Query, mutation=Mutation)
