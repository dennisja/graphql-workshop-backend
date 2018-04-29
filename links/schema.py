import graphene
from graphene_django import DjangoObjectType

from .models import Link


"""
The link type
"""
class LinkType(DjangoObjectType):
    class Meta:
        model = Link

"""
Link mutation fields
"""
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    title = graphene.String()

    class Arguments:
        url = graphene.String()
        title = graphene.String()

    def mutate(self, info, url, title):
        link = Link(url=url, title=title)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            title=link.title
        )

"""
Queries of link type
"""
class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

"""
Mutations of link type
"""
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
