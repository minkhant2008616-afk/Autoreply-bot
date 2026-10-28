from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# ကိုယ့်ရဲ့ Bot Token
TOKEN = "9267946446:AAHb9D62E6Ezsff2d7DfFvuqG7egsx3JpRs"

# စာပို့ရင် စာပြန်ပို့မယ့် function
async def echo_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# ပုံပို့ရင် ပုံပြန်ပို့မယ့် function
async def echo_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = update.message.photo[-1].file_id
    await update.message.reply_photo(photo=photo_file)

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    # စာအတွက် handler
    text_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo_text)
    application.add_handler(text_handler)
    
    # ပုံအတွက် handler
    photo_handler = MessageHandler(filters.PHOTO, echo_photo)
    application.add_handler(photo_handler)
    
    # Bot ကို စတင်လည်ပတ်စေရန်
    application.run_polling()

if __name__ == '__main__':
    main()
