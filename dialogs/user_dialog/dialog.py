from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import SwitchTo, Column, Row, Button, Group, Select, Start, Url
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.media import DynamicMedia

from dialogs.user_dialog import getters

from states.state_groups import startSG, adminSG

user_dialog = Dialog(
    Window(
        DynamicMedia('media'),
        Const('Выберите интересующий вас пункт'),
        Row(
            SwitchTo(Const('❓Кто я'), id='about_switcher', state=startSG.about),
            SwitchTo(Const('🗓Услуги'), id='help_switcher', state=startSG.help),
        ),
        Column(
            Url(Const('🔗Отзывы'), id='reviews_url', url=Const('https://t.me/leggit_reviews')),
            Url(Const('🔗Блог'), id='blog_url', url=Const('https://t.me/leggit_life')),
            Url(Const('🔗Leggit Tech'), id='tech_url', url=Const('https://t.me/LeggitTech')),
            Start(Const('Админ панель'), id='admin', state=adminSG.start, when='admin')
        ),
        getter=getters.start_getter,
        state=startSG.start
    ),
    Window(
        DynamicMedia('media'),
        Format('{text}'),
        Url(Const('💬Написать мне'), id='contact_url', url=Const('https://t.me/Leggit_Russia')),
        SwitchTo(Const('🔙Назад'), id='back', state=startSG.start),
        getter=getters.about_getter,
        state=startSG.about
    ),
    Window(
        DynamicMedia('media'),
        Format('{text}'),
        Url(Const('💬Написать мне'), id='contact_url', url=Const('https://t.me/Leggit_Russia')),
        SwitchTo(Const('🔙Назад'), id='back', state=startSG.start),
        getter=getters.help_getter,
        state=startSG.help
    ),
)