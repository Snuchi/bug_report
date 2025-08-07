from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Текст отчёта
REPORT_TEXT = """
Дата: 
Старший смены: 
Call: 
My call: 

Кол. записей: 
Игорь - 
Кирилл К - 
Andrey - 
Igor - 
Алексей - 
Ростик - 
Hlina - 

Поверка:
Игорь 1 ( ТТ верх 80 водителей )
Проверил: 

Кирилл К 2 (ТТ низ 80 водителей)
Проверил: 

Andrey 3 ( Маджик верх 80 водителей )
Проверил: 

Igor 4 (Маджик низ 80 водителей)
Проверил: 

Алексей 5 ( Пятая проверка 80 водителей )
Проверил: 

Ростик 6 (Шестая проверка 80 водителей)
Проверил: 

Hlina 7 ( Седьмая проверка 80 водителей )
Проверил: 

Редактирование боллов (имя компании )
Dmitriy Silchenkov 2 бола

Коментарий к смене:
* если есть упоменание о сотруднике пожалуйста пишите имя как в edits
* коментарий можно делать в вольной форме БЕЗ МАТОВ большая просьба!
"""

# Обработчик команды /reportexample
async def report_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(REPORT_TEXT)

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(CommandHandler("reportexample", report_handler))

    print("Бот запущен...")
    app.run_polling()
