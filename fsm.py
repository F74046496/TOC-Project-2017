from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'

    def on_enter_state1(self, update):
        update.message.reply_text("I'm entering state1")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("I'm entering state2")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    #def going
    def is_going_to_Bored(self, update):
        text = update.message.text
        return text.lower() == 'feel bored'

    def is_going_to_Sweated(self, update):
        text = update.message.text
        return text.lower() == 'go to sail'

    def is_going_to_Annoyed(self, update):
        text = update.message.text
        return text.lower() == 'go to study'

    def is_going_to_Excited(self, update):
        text = update.message.text
        return text.lower() == 'go to play games'

    def is_going_to_Tired(self, update):
        text = update.message.text
        return (text.lower() == 'go to take a shower' or text.lower() == 'go to study more')

    def is_going_to_Sleeping(self, update):
        text = update.message.text
        return text.lower() == 'go to sleep'

    #def enter and exit
    def on_enter_Bored(self, update):
        update.message.reply_text("If you feel bored, you can try to 'sail', 'study', or 'play games'")
        update.message.reply_photo("https://www.cuded.com/wp-content/uploads/2015/04/bored-cat_work-600x384.jpg")

    def on_exit_Bored(self, update):
        print('Leaving Bored')

    def on_enter_Sweated(self, update):
        update.message.reply_text("You may feel sweated and hot.\nWhy not go to take a shower?")
        update.message.reply_photo("https://events.sailracer.info/userfiles/BRA-ISAFYouths-420Boys.jpg")

    def on_exit_Sweated(self, update):
        print('Leaving Sweated')

    def on_enter_Annoyed(self, update):
        update.message.reply_text("You want to study more?\nOr you feel a little annoyed and want to play games?")
        update.message.reply_photo("https://coachinga01.com/wp-content/uploads/2017/09/20160912101051002.jpg")

    def on_exit_Annoyed(self, update):
        print('Leaving Annoyed')

    def on_enter_Excited(self, update):
        update.message.reply_text("Here is a good song to listen.")
        update.message.reply_audio(open("music/LANY - Hurts.mp3","rb"))
        update.message.reply_text("Do you want to keep playing games?\nOr you want to study?")
        update.message.reply_photo("https://scontent-sea1-1.cdninstagram.com/t51.2885-15/e35/12627830_478163089049299_1325916093_n.jpg?ig_cache_key=MTE4NTUzNzk0MTcxMzU1OtkzNA%3D%3D.2&se=7")

    def on_exit_Excited(self, update):
        print('Leaving Excited')

    def on_enter_Tired(self, update):
        update.message.reply_text("You look like very tired now, I think you should go to sleep.")
        update.message.reply_photo("https://pic.pimg.tw/craburgerm/dbc74a5608da48ef8c3f5f255e4eaa1b.jpg")

    def on_exit_Tired(self, update):
        print('Leaving Tired')

    def on_enter_Sleeping(self, update):
        update.message.reply_text("go to sleep~Zzz")
        update.message.reply_photo("https://3.bp.blogspot.com/-PtOPzvUtUos/VTHYd-Ode1I/AAAAAAAAQPQ/Lvu0JD8PEOM/s1600/0.gif")
        self.go_back(update)

    def on_exit_Sleeping(self, update):
        print('Leaving Sleeping')
