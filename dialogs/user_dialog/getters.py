from aiogram.types import CallbackQuery, User, Message, ContentType
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Button, Select
from aiogram_dialog.widgets.input import ManagedTextInput

from database.action_data_class import DataInteraction
from config_data.config import load_config, Config
from states.state_groups import startSG


config: Config = load_config()


async def start_getter(event_from_user: User, **kwargs):
    admin = False
    if event_from_user.id in config.bot.admin_ids:
        admin = True
    media = MediaAttachment(type=ContentType.PHOTO, path='photos/Menu.png')
    return {
        'media': media,
        'admin': admin
    }


async def help_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    text = ('<b><u>Что я предлагаю?</u></b>\n\n<b>• 📊Боты для инфобизнеса</b>: создание воронок продаж, '
            'CRM-систем и автоматизированных решений для прогрева аудитории, увеличения конверсий и '
            'управления клиентами.\n• <b>⚙️Автоматизация бизнес-процессов</b>: оптимизация рутинных задач, управление '
            'базами данных и построение систем, которые работают за вас 24/7.\n<b>• 🤖Интеграция ИИ</b>: '
            'внедрение умных алгоритмов для анализа данных, прогнозирования поведения клиентов и '
            'персонализации взаимодействия.\n<b>• 💸Монетизация продуктов</b>: '
            'разработка решений для продажи товаров, услуг или контента через Telegram, включая '
            'полноценные магазины и системы подписок.')
    media = MediaAttachment(type=ContentType.PHOTO, path='photos/Service.png')
    return {
        'media': media,
        'text': text
    }


async def about_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    text = ('👋Привет, меня зовут <b>Кирилл</b>, мне 18 лет, и я — Python-developer '
            '(Технический специалист) под брендом <b>Leggit</b>.\n\n<em>Я помогаю предпринимателям и '
            'бизнесменам создавать эффективные решения для автоматизации процессов, увеличения продаж и '
            'улучшения взаимодействия с аудиторией через Telegram-боты и веб-приложения .</em>\n\n'
            '<b>❓Почему выбирают меня?</b>\n\n<b>• Глубокая экспертиза в Telegram-технологиях :</b>\n'
            'Я специализируюсь на разработке ботов и веб-приложений, которые работают на результат. '
            'Будь то воронка продаж, CRM-система или полноценный магазин в Telegram — я создаю продукты, '
            'которые приносят реальную прибыль.\n<b>• Молодой, но опытный: </b>\nНесмотря на возраст, '
            'я уже реализовал десятки успешных проектов для бизнеса. Мой подход сочетает современные '
            'технологии и креативное мышление.\n<b>• Индивидуальный подход:</b>\n Я не просто пишу код — '
            'я изучаю ваш бизнес, чтобы предложить решение, которое решает именно ваши задачи.')
    media = MediaAttachment(type=ContentType.PHOTO, path='photos/Me.png')
    return {
        'media': media,
        'text': text
    }
