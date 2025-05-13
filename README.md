# alice-wuth-shopping-list
Shopping list with voice assistant

# Голосовой помощник: Список покупок через Алису + Telegram

Это пример проекта, где:
- **Алиса** — голосовой ввод
- **Flask + SQLite** — хранение данных
- **Telegram-бот** — просмотр и редактирование

## Установка

```bash
pip install -r requirements.txt
mkdir instance
python -c "from database import init_db; init_db()"
