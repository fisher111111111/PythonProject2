# schema.py
import graphene

# Имитация базы данных в памяти
USERS_DATA = {}
next_user_id = 1
# Также добавим некоторые посты для демонстрации связи
POSTS_DATA = {}
next_post_id = 1

class User(graphene.ObjectType):
    """Тип пользователя."""
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    posts = graphene.List(lambda: Post) # Использование lambda для избежания циклической зависимости

    def resolve_posts(self, info):
        # В реальном приложении здесь был бы запрос к БД
        return [post for post in POSTS_DATA.values() if post['author_id'] == int(self.id)]

class Post(graphene.ObjectType):
    """Тип поста."""
    id = graphene.ID()
    title = graphene.String()
    published = graphene.Boolean()
    link = graphene.String()
    author = graphene.Field(User)

    def resolve_author(self, info):
        # В реальном приложении здесь был бы запрос к БД
        author_id = self.author_id # author_id будет добавлен в POSTS_DATA
        return USERS_DATA.get(author_id)

# --- QUERY (Запросы на чтение) ---
class Query(graphene.ObjectType):
    """Определяет все доступные запросы (Query)."""
    users = graphene.List(User)
    user = graphene.Field(User, id=graphene.ID(required=True))

    def resolve_users(self, info):
        """Возвращает список всех пользователей."""
        return [User(**user) for user in USERS_DATA.values()]

    def resolve_user(self, info, id):
        """Возвращает пользователя по ID."""
        user_data = USERS_DATA.get(int(id))
        return User(**user_data) if user_data else None

# --- MUTATIONS (Запросы на изменение) ---

class CreateUser(graphene.Mutation):
    """Мутация для создания нового пользователя."""
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String()

    Output = User # Что возвращаем после создания

    def mutate(self, info, name, email=None):
        global next_user_id
        user_id = next_user_id
        next_user_id += 1

        new_user = {
            'id': user_id,
            'name': name,
            'email': email
        }
        USERS_DATA[user_id] = new_user
        return CreateUser(user=User(**new_user))

class UpdateUser(graphene.Mutation):
    """Мутация для обновления существующего пользователя."""
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()

    Output = User # Что возвращаем после обновления

    def mutate(self, info, id, name=None, email=None):
        user_id = int(id)
        user = USERS_DATA.get(user_id)
        if not user:
            raise Exception(f"Пользователь с ID {id} не найден.")

        if name is not None:
            user['name'] = name
        if email is not None:
            user['email'] = email

        USERS_DATA[user_id] = user # Обновляем данные в словаре (по факту уже обновлено, но для ясности)
        return UpdateUser(user=User(**user))

class DeleteUser(graphene.Mutation):
    """Мутация для удаления пользователя."""
    class Arguments:
        id = graphene.ID(required=True)

    Output = graphene.Boolean # Просто булево значение, обозначающее успех операции

    def mutate(self, info, id):
        user_id = int(id)
        if user_id in USERS_DATA:
            del USERS_DATA[user_id]
            # Также удаляем посты этого пользователя для целостности
            posts_to_delete = [pid for pid, post in POSTS_DATA.items() if post['author_id'] == user_id]
            for pid in posts_to_delete:
                del POSTS_DATA[pid]
            return True
        return False

class Mutation(graphene.ObjectType):
    """Объединяет все мутации."""
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

# Создаем финальную схему GraphQL
schema = graphene.Schema(query=Query, mutation=Mutation)

# --- Добавление начальных данных для тестирования ---
def init_data():
    global next_user_id, next_post_id

    # User 1
    user1_id = next_user_id
    next_user_id += 1
    USERS_DATA[user1_id] = {'id': user1_id, 'name': 'Alice', 'email': 'alice@example.com'}

    # User 2
    user2_id = next_user_id
    next_user_id += 1
    USERS_DATA[user2_id] = {'id': user2_id, 'name': 'Bob', 'email': 'bob@example.com'}

    # Post 1 (by Alice)
    post1_id = next_post_id
    next_post_id += 1
    POSTS_DATA[post1_id] = {
        'id': post1_id, 'title': 'My First Post', 'published': True,
        'link': 'http://example.com/post1', 'author_id': user1_id
    }

    # Post 2 (by Bob)
    post2_id = next_post_id
    next_post_id += 1
    POSTS_DATA[post2_id] = {
        'id': post2_id, 'title': 'Bob\'s Amazing Story', 'published': False,
        'link': 'http://example.com/post2', 'author_id': user2_id
    }

init_data()
