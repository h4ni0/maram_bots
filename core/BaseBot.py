from abc import ABC, abstractmethod
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from core.utils.apis import ApiUtils
from core.utils.html import HtmlUtils


class BaseBot(ABC):
    def __init__(self, token):
        self.token = token
        self.app = None
        self.api = ApiUtils()
        self.html = HtmlUtils()

    @abstractmethod
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Bot Started")

    @abstractmethod
    async def text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        This function will obtain a user input and reply with a message
        """
        message = update.message.text
        await update.message.reply_text("message received")

    def __add_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(MessageHandler(filters.TEXT, self.text))

    def __start(self):
        self.app.run_polling()


    def run(self):
        if not self.app:
            self.app = Application.builder().token(self.token).build()
            self.__add_handlers()
            self.__start()

