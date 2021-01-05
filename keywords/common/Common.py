import string
import datetime
from unidecode import unidecode


def convert_amount(amount_num):
    amount_num = int(amount_num)
    amount = ('{:0,.0f}'.format(amount_num).replace(',', '.')+' VND')
    print('{:0,.0f}'.format(amount_num).replace(',', '.')+' VND')
    return amount


def validate_balance(pre_balance, after_balance, trans_amount, fee):
    pre_balance = int(pre_balance)
    after_balance = int(after_balance)
    trans_amount = int(trans_amount)
    fee = int(fee)
    if pre_balance - after_balance == trans_amount + fee:
        print('balance match')
        return True
    else:
        print('balance not match')
        return False


def validate_balance_with_discount(pre_balance, after_balance, trans_amount, fee, discount):
    pre_balance = int(pre_balance)
    after_balance = int(after_balance)
    trans_amount = int(trans_amount)
    fee = int(fee)
    discount = float(int(discount[:-1]) * 0.01)
    print(discount)
    if pre_balance - after_balance == trans_amount + fee - discount*trans_amount:
        print('balance match')
        return True
    else:
        print('balance not match')
        return False


def validate_balance_after_recharge(pre_balance, after_balance, trans_amount):
    pre_balance = int(pre_balance)
    after_balance = int(after_balance)
    trans_amount = int(trans_amount)
    if after_balance - pre_balance == trans_amount:
        print('balance match')
        return True
    else:
        print('balance not match')
        return False


def get_customer_name_from_transfer_phone(text):
    customer_name = text[int(text.find(': ')+1):int(len(text))]
    return customer_name.strip()


def validate_trans_time(trans_time):
    current_time = datetime.datetime.now()
    compare_time = current_time.strftime('%d/%m/%Y - %H')
    trans_time = trans_time.strip()[:-6]
    if compare_time == trans_time:
        return True
    else:
        return False


