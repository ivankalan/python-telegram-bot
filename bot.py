import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler

bot_token = os.environ.get('bot_token')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#handle /getpods command
async def get_pods(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pods = os.popen("kubectl get pod -n unified").read()
    await update.message.reply_text(pods)

#handle /getpods message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "/getpods":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=get_pods
        )

def main():
    application = ApplicationBuilder().token(bot_token).build()
    
    get_pods_handler = CommandHandler('getpods', get_pods)
    message_handler = MessageHandler(filters.Text, handle_message)

    application.add_handler(get_pods_handler)
    application.add_handler(message_handler)
    
    application.run_polling()

if __name__ == '__main__':
    main()