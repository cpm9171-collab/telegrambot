from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

TOKEN = "8874670568:AAGUMyeFAQ6yFcAhadFWg37X2Y79yTuGh-Y"

async def start(update, context):
    keyboard = [[
        InlineKeyboardButton("🔥 Join Channel", url="https://t.me/bdgplaysalarymeeting")
    ]]

    await update.message.reply_text(
        "Welcome! Click below to join our channel.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()