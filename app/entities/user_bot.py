from threading import Thread, Timer

import discum as discum
import random
import time


class UserBot(Thread):
    global proxy, new_to_respond_list, message_data, random_auto_message

    def __init__(self, _token, _time, _auto_channel_id, _channel_id,
                 _message, _user_id):
        self.bot = discum.Client(token=_token,
                                 log={"console": True, "file": False})
        if proxy is not None:
            self.bot.switchProxy(proxy)
        self._time = _time
        self._auto_channel_id = _auto_channel_id
        self._channel_id = _channel_id
        self._message = _message
        self._user_id = _user_id

    def automate_message(self):
        Timer(self._time*60, self.automate_message).start()
        for item in self._auto_channel_id:
            self.bot.sendMessage(item, random.choice(random_auto_message))

    def get_last_message_id(self, sleep_time=2):
        #  threading.Timer(sleep_time, self.get_last_message_id).start()
        for item in self._channel_id:
            last_message_ressponse = self.bot.getMessages(item, num=7).json()
            if "message" in last_message_ressponse:
                sleep_time = data['retry_after']
                time.sleep(sleep_time+2)
            for last_message in last_message_ressponse:
                author = last_message['author']['id']
                if author == self._user_id:
                    #  print("cannot reply to yourself")
                    continue
                else:
                    message_id = last_message['id']
                    content = str(last_message['content']).lower()
                    for solo_word in content.split():
                        if solo_word in _to_respond_list or solo_word in new_to_respond_list:
                            check_data = message_in_message_data(message_id)
                            #  print(check_data)
                            if check_data is False:
                                #  print("adding to queue" + message_id)
                                message_data.append(
                                    {'id': message_id, 'data': solo_word,
                                     'channel_id': item, 'response': False})
        time.sleep(3)

    def respond_to_text(self):
        #  threading.Timer(3, self.respond_to_text).start()
        #  print("Running respond")
        if len(message_data) == 0:
            pass
        else:
            #  to_respond = message_data.pop(0)
            for items in message_data:
                if items['response'] is False:
                    message_id = items['id']
                    message = items['data']
                    channel_id = items['channel_id']
                    response_text = get_respondable_text(message)
                    self.bot.reply(
                        channel_id,
                        message_id,
                        response_text[0],
                        file=response_text[1])
                    items['response'] = True
                    break
            if len(message_data) > 50:
                message_data.pop(0)
                print("Freeing space")
        time.sleep(5)