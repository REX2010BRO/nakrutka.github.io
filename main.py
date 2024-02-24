import hashlib
import asyncio
import aiohttp
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import config
import database
import keyboard
import telebot
from telebot import types
import config
from background import keep_alive
##цены
amount500viewstg = 3
amount1000viewstg = 6
amount2000viewstg = 9
amount4000viewstg = 12
amount5000viewstg = 15
amount500subscriptionstg = 19
amount1000subscriptionstg = 39
amount2000subscriptionstg = 79
amount4000subscriptionstg = 149
amount5000subscriptionstg = 180

db = database.SQLite()
bot = Bot(token=config.telegram_token)
dp = Dispatcher(bot)


async def check_new_payments():
    while True:
        async with aiohttp.ClientSession() as session:
            request_params = {'API_ID': config.api_id, 'API_KEY': config.api_key, 'shop': config.shop_id}

            async with session.post('https://payok.io/api/transaction', data=request_params) as response:
                transaction_list = await response.json(content_type=None)
        
        if transaction_list['status'] == 'success':
            new_transaction = db.check_transaction(transaction_list['1']['transaction'])
            if transaction_list['1']['transaction_status'] == '1' and new_transaction:
                await bot.send_message(transaction_list['1']['payment_id'], 'Оплачено, напишите свой телеграм канал на который хотите нарутить подписчиков')
                db.add_transaction(transaction_list['1']['transaction'], transaction_list['1']['payment_id'], transaction_list['1']['amount'])
                print('Новый заказ от @',message.from_user.username, message.from_user.first_name,message.from_user.last_name)

        await asyncio.sleep(2)


async def get_payment_url(user_id, amount):
    sign = hashlib.md5(f"{amount}|{user_id}|{config.shop_id}|{config.currency}|{config.desc}|{config.secret}".encode('utf-8')).hexdigest()
    url = f"https://payok.io/pay?amount={amount}&currency={config.currency}&payment={user_id}&desc={config.desc}&shop={config.shop_id}&method=cd&sign={sign}"
    return url


@dp.message_handler(commands=['start'])
async def handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать!\nЧтобы выбрать товар, воспользуйтесь клавиатурой. Все цены здесь - https://t.me/nakrutkatelegram2023', reply_markup=keyboard.get_main_keyboard())


@dp.message_handler(text='Купить 500 просмотров')
async def handler(message: types.Message):
    payment_url = await get_payment_url(message.from_user.id, amount500viewstg)
    await bot.send_message(message.from_user.id, f"💵 Оплатите 💵\n\n💰 Цена: {amount500viewstg}р\n\n🚀 Для оплаты перейдите по ссылке через кнопку ниже", reply_markup=keyboard.get_payment_keyboard(payment_url))
@dp.message_handler(text='Купить 1000 просмотров')
async def handler(message: types.Message):
    payment_url = await get_payment_url(message.from_user.id, amount1000viewstg)
    await bot.send_message(message.from_user.id, f"💵 Оплатите 💵\n\n💰 Цена: {amount1000viewstg}р\n\n🚀 Для оплаты перейдите по ссылке через кнопку ниже", reply_markup=keyboard.get_payment_keyboard(payment_url))
@dp.message_handler(text='Купить 2000 просмотров')
async def handler(message: types.Message):
    payment_url = await get_payment_url(message.from_user.id, amount2000viewstg)
    await bot.send_message(message.from_user.id, f"💵 Оплатите 💵\n\n💰 Цена: {amount2000viewstg}р\n\n🚀 Для оплаты перейдите по ссылке через кнопку ниже", reply_markup=keyboard.get_payment_keyboard(payment_url))
@dp.message_handler(text='Купить 4000 просмотров')
async def handler(message: types.Message):
    payment_url = await get_payment_url(message.from_user.id, amount4000viewstg)
    await bot.send_message(message.from_user.id, f"💵 Оплатите 💵\n\n💰 Цена: {amount4000viewstg}р\n\n🚀 Для оплаты перейдите по ссылке через кнопку ниже", reply_markup=keyboard.get_payment_keyboard(payment_url))
@dp.message_handler(text='Купить 5000 просмотров')
async def handler(message: types.Message):
    payment_url = await get_payment_url(message.from_user.id, amount5000viewstg)
    await bot.send_message(message.from_user.id, f"💵 Оплатите 💵\n\n💰 Цена: {amount5000viewstg}р\n\n🚀 Для оплаты перейдите по ссылке через кнопку ниже", reply_markup=keyboard.get_payment_keyboard(payment_url))
@dp.message_handler(text='Купить 500 подписчиков')
async def handler(message: types.Message):
    payment_url = await get_payment_url(message.from_user.id, amount500subscriptionstg)
    await bot.send_message(message.from_user.id, f"💵 Оплатите 💵\n\n💰 Цена: {amount500subscriptionstg}р\n\n🚀 Для оплаты перейдите по ссылке через кнопку ниже", reply_markup=keyboard.get_payment_keyboard(payment_url))
@dp.message_handler(text='Купить 1000 подписчиков')
async def handler(message: types.Message):
    payment_url = await get_payment_url(message.from_user.id, amount1000subscriptionstg)
    await bot.send_message(message.from_user.id, f"💵 Оплатите 💵\n\n💰 Цена: {amount1000subscriptionstg}р\n\n🚀 Для оплаты перейдите по ссылке через кнопку ниже", reply_markup=keyboard.get_payment_keyboard(payment_url))
@dp.message_handler(text='Купить 2000 подписчиков')
async def handler(message: types.Message):
    payment_url = await get_payment_url(message.from_user.id, amount2000subscriptionstg)
    await bot.send_message(message.from_user.id, f"💵 Оплатите 💵\n\n💰 Цена: {amount2000subscriptionstg}р\n\n🚀 Для оплаты перейдите по ссылке через кнопку ниже", reply_markup=keyboard.get_payment_keyboard(payment_url))
@dp.message_handler(text='Купить 4000 подписчиков')
async def handler(message: types.Message):
    payment_url = await get_payment_url(message.from_user.id, amount4000subscriptionstg)
    await bot.send_message(message.from_user.id, f"💵 Оплатите 💵\n\n💰 Цена: {amount4000subscriptionstg}р\n\n🚀 Для оплаты перейдите по ссылке через кнопку ниже", reply_markup=keyboard.get_payment_keyboard(payment_url))
@dp.message_handler(text='Купить 5000 подписчиков')
async def handler(message: types.Message):
    payment_url = await get_payment_url(message.from_user.id, amount5000subscriptionstg)
    await bot.send_message(message.from_user.id, f"💵 Оплатите 💵\n\n💰 Цена: {amount5000subscriptionstg}р\n\n🚀 Для оплаты перейдите по ссылке через кнопку ниже", reply_markup=keyboard.get_payment_keyboard(payment_url))    
keep_alive()
if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
loop = asyncio.get_event_loop()
loop.create_task(check_new_payments())
executor.start_polling(dp)
