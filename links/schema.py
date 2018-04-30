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
    last_edited = graphene.DateTime()
    created_at = graphene.DateTime()
    posted_by = graphene.Field(LinkType)

    class Arguments:
        url = graphene.String()
        title = graphene.String()

    def mutate(self, info, url, title):
        user = info.contextl.user or None

        link = Link(url=url, title=title, posted_by=user)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            title=link.title,
            posted_by=link.posted_by,
            created_at=link.created_at,
            last_edited=link.last_edited,
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
