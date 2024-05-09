from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove


async def default_reply(update: Update, context):
    # user = update.message.from_user
    user_choice = update.message.text
    context.user_data["is_useful"] = user_choice
    context.chat_data
    context.bot_data
    await update.message.reply_text("Default reply", reply_markup=ReplyKeyboardRemove())
