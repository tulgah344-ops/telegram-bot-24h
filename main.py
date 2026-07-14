from telegram.ext import Application, CommandHandler
import os
from flask import Flask
import threading

BOT_TOKEN = "8749944205:AAFV3JEJnF6ZomVOEgb1C1_9Sm9iB18htzE"

app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot is alive"

async def start(update, context):
    await update.message.reply_text("سلام ربات روشنه ✅")

application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))

def run_bot():
    application.run_polling()

threading.Thread(target=run_bot).start()

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
