import graphene

import links.schema
import user.schema


class Query(links.schema.Query, user.schema.Query, graphene.ObjectType):
    pass


class Mutation(links.schema.Mutation, user.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
