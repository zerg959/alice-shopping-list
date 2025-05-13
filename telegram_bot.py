from telegram.ext import Updater, CommandHandler
import database

TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("Привет! Используйте /list чтобы посмотреть списки.")

def list_lists(update, context):
    user = update.message.from_user.id
    lists = database.get_all_lists(user)
    if not lists:
        update.message.reply_text("Список покупок пуст.")
        return
    for lid, _, content in lists:
        update.message.reply_text(f"?? Список #{lid}:\n{content}")

def edit_list(update, context):
    try:
        list_id = int(context.args[0])
        new_content = ' '.join(context.args[1:])
        success = database.update_list(list_id, new_content)
        if success:
            update.message.reply_text(f"Список #{list_id} обновлён")
        else:
            update.message.reply_text("Ошибка при редактировании")
    except:
        update.message.reply_text("Используйте: /edit <номер> <новое содержимое>")

updater = Updater(TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("list", list_lists))
dp.add_handler(CommandHandler("edit", edit_list))

updater.start_polling()