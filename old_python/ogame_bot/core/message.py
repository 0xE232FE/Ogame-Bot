from old_python.ogame_bot import get_bot


class Message:
    def __init__(self):
        self.bot = get_bot()

    def send_message(self, player_id, msg):
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        payload = {'playerId': player_id,
                   'text': msg,
                   'mode': 1,
                   'ajax': 1}
        url = self.bot.get_url('ajaxChat')
        self.bot.wrapper.session.post(url, data=payload, headers=headers)

