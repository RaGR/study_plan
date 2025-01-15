from persiantools.jdatetime import JalaliDate
from datetime import datetime
import pytz
import json
from random import randint

path_data = "/home/mahbod/Desktop/study_plan/database.json" #should be systematic file path -> use os module
path_student_id = "/home/mahbod/Desktop/study_plan/uniq_id/student_id.txt" #should be systematic file path -> use os module

user_data_dict = {
    "uniq_id": None,
    "account_name": None,
    "account_lastname": None,
    "account_username": None,
    "account_phone_number": None,
    "available_phone_number": None,
    "name": None,
    "last_name": None,
    "nationality_number": None,
    "email": None,
    "age": None,
    "gender": None,
    "password": None,
    "repeat_password": None,
    "relationship": None,
    "persian_date": None,
    "tehran_time": None
}

data_dict = {

}


def generating_student_uniq_id(chat_id: str, path=path_student_id):
    try:
        with open(path, "r") as file:
            ides = file.readlines()

        student_id = randint(100000000, 200000000)
        while student_id in ides:
            student_id = randint(100000000, 200000000)

        with open(path, "w") as file:
            file.write(str(student_id))

        data = read_data_uniq(chat_id)
        if data is False:
            return str(student_id)

        else:
            return False

    except Exception as error:
        print(f"this Error for generating_student_uniq_id func:\n{error}")


def telegram_data_creator(message):
    chat_id_account = str(message.chat.id)
    user_id_account = message.from_user.username
    first_name_account = message.from_user.first_name
    last_name_account = message.from_user.last_name
    phone_number_account = message.contact.phone_number

    student_uniq_id = generating_student_uniq_id(chat_id_account)

    data_dict[chat_id_account] = user_data_dict.copy()
    data_dict[chat_id_account]["account_name"] = first_name_account
    data_dict[chat_id_account]["account_lastname"] = last_name_account
    data_dict[chat_id_account]["account_username"] = f"@{user_id_account}"
    data_dict[chat_id_account]["account_phone_number"] = phone_number_account
    data_dict[chat_id_account]["uniq_id"] = student_uniq_id
    data_dict[chat_id_account]["persian_date"] = persian_date()
    data_dict[chat_id_account]["tehran_time"] = tehran_time()

    write_data(data_dict)


def is_in_channel(bot, id_channel: str, chat_id: int):
    try:
        member_status = bot.get_chat_member(id_channel, chat_id).status
        if member_status in ["member", "creator", "administrator"]:
            return True

        else:
            return False

    except Exception as e:
        print(f"this error for is_in_channel func : \n{e}")


def contact_check(message):

    if message.contact is not None:
        telegram_data_creator(message)
        return True

    else:
        return False


def write_data(user_data, path=path_data):

    existing_data = read_data()
    existing_data.update(user_data)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)


def read_data(path=path_data):

    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        user_data = json.loads(content)

    return user_data


def read_data_uniq(chat_id: str, path=path_data):
    all_data = read_data(path)

    if chat_id in all_data:
        return all_data[chat_id]

    else:
        return False


def persian_date():
    current_date = JalaliDate.today()

    return str(current_date)


def tehran_time():
    iran_tz = pytz.timezone('Asia/Tehran')
    iran_now = datetime.now(iran_tz)

    return iran_now.strftime('%H:%M:%S')
