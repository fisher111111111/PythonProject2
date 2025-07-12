# app.py
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)

# Добавляем маршрут /graphql, который будет использовать наш Graphene-схему.
# graphiql=True включает интерактивную среду GraphiQL для тестирования в браузере.
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # Включаем GraphiQL для удобного тестирования
    )
)

if __name__ == '__main__':
    print("GraphQL API запущен на http://127.0.0.1:5000/graphql")
    print("Откройте этот адрес в браузере для использования GraphiQL.")
    app.run(debug=True)
