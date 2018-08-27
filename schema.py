
import graphene

from graphene_mongo import MongoengineObjectType

from models import Person as PersonModel


class Persona(graphene.ObjectType):
    nombre = graphene.String()

    def resolve_nombre(self, info):
        print self.id
        print "info:\n\n\n\n\n\n\n\n\n\n\n "
        # print info.field_name
        # print info.field_asts
        # print info.return_type
        # print info.parent_type
        # print info.schema
        # print info.fragments
        # print info.root_value
        # print info.operation
        # print info.variable_values
        # print info.context
        # print info.path
        #return "mi nombre"
        return PersonModel.objects.get(id=self.id).name

# class Persona(MongoengineObjectType):
#     class Meta:
#         model = PersonModel
#
#     nombre = graphene.String()
#
#     def resolve_nombre(self, info):
#         print self.id
#         print "info:\n\n\n\n\n\n\n\n\n\n\n "
#         # print info.field_name
#         # print info.field_asts
#         # print info.return_type
#         # print info.parent_type
#         # print info.schema
#         # print info.fragments
#         # print info.root_value
#         # print info.operation
#         # print info.variable_values
#         # print info.context
#         # print info.path
#         #return "mi nombre"
#         return PersonModel.objects.get(id=self.id).name


# class PersonOT(graphene.ObjectType):
#     nombre = graphene.String()
#
#     def resolve_nombre(self, info):
#         print "info: "
#         print str(info)
#         print info.field_name
#         print info.field_asts
#         print info.return_type
#         print info.parent_type
#         print info.schema
#         print info.fragments
#         print info.root_value
#         print info.operation
#         print info.variable_values
#         print info.context
#         print info.path
#
#         return "mi nombre"


class Query(graphene.ObjectType):
    personas = graphene.List(Persona)
    #personas = graphene.List(PersonOT)

    def resolve_personas(self, info):
        return list(PersonModel.objects.all())

    # def resolve_personas(self, info):
    #     print "resolve_personas> info: "+str(info)
    #     return list([])
    #     #return list(PersonOT.objects.all())

schema = graphene.Schema(query=Query)


def create_person(name):
    p = PersonModel(name=name)
    p.save()

