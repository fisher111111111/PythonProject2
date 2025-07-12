from flask import Flask
from flask_graphql import GraphQLView
import graphene

users = []

class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(root, info):
        return users

# Создание пользователя
class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(root, info, name):
        user = {"id": len(users) + 1, "name": name}
        users.append(user)
        return CreateUser(user=user)

# Редактирование пользователя
class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(root, info, id, name):
        for user in users:
            if user["id"] == id:
                user["name"] = name
                return UpdateUser(user=user)
        raise Exception("Пользователь с таким id не найден")

# Удаление пользователя
class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(root, info, id):
        global users
        for user in users:
            if user["id"] == id:
                users = [u for u in users if u["id"] != id]
                return DeleteUser(ok=True)
        raise Exception("Пользователь с таким id не найден")

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    app.run(debug=True)
