import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '528602725:AAFgbyH7AavynGep_t3D64x8h-tv7mrWeSY'
WEBHOOK_URL = 'https://c6013628.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'Bored',
        'Sweated',
        'Annoyed',
        'Excited',
        'Tired',
        'Sleeping'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'Bored',
            'conditions': 'is_going_to_Bored'
        },
        {
            'trigger': 'advance',
            'source': 'Bored',
            'dest': 'Sweated',
            'conditions': 'is_going_to_Sweated'
        },
        {
            'trigger': 'advance',
            'source': 'Bored',
            'dest': 'Annoyed',
            'conditions': 'is_going_to_Annoyed'
        },
        {
            'trigger': 'advance',
            'source': 'Bored',
            'dest': 'Excited',
            'conditions': 'is_going_to_Excited'
        },
        {
            'trigger': 'advance',
            'source': 'Sweated',
            'dest': 'Tired',
            'conditions': 'is_going_to_Tired'
        },
        {
            'trigger': 'advance',
            'source': 'Tired',
            'dest': 'Sleeping',
            'conditions': 'is_going_to_Sleeping'
        },
        {
            'trigger': 'advance',
            'source': 'Annoyed',
            'dest': 'Tired',
            'conditions': 'is_going_to_Tired'
        },
        {
            'trigger': 'advance',
            'source': 'Annoyed',
            'dest': 'Excited',
            'conditions': 'is_going_to_Excited'
        },
        {
            'trigger': 'advance',
            'source': 'Excited',
            'dest': 'Annoyed',
            'conditions': 'is_going_to_Annoyed'
        },
        {
            'trigger': 'advance',
            'source': 'Excited',
            'dest': 'Excited',
            'conditions': 'is_going_to_Excited'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'Sleeping'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
