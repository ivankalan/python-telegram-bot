import os
import logging
from telegram import Update, ReplyParameters
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

bot_token = os.environ.get('bot_token')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# get pods
async def get_pods(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pods=os.popen("kubectl get pod -n unified").read()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_parameters=ReplyParameters(message_id=update.effective_message.message_id),
        text=pods
    )

def main():
    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler('getpods', get_pods))
    
    application.run_polling()

if __name__ == '__main__':
    main()