from telegram.ext import Application, CommandHandler

BOT_TOKEN = "8749944205:AAFV3JEJnF6ZomVOEgb1C1_9Sm9iB18htzE"

async def start(update, context):
    await update.message.reply_text("سلام ربات روشنه ✅")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
