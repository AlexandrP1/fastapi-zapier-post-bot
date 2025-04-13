# FastAPI Telegram Post Generator

Генератор постов для Telegram с использованием GPT-4o, совместим с Zapier.

## Эндпоинт

`POST /generate-post`

### Пример тела запроса

```json
{
  "topic": "путешествия"
}
```

### Ответ

```json
{
  "post": "🌍 Путешествия — это..."
}
```
