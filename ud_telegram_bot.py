import telegram.ext

Token = "5872923071:AAHKFHxUmEXVEm-6500bqW-3mYvvjZwZ6iI"

updater = telegram.ext.Updater(Token,use_context = True)
dispatcher = updater.dispatcher

def start(update , context):
    update.message.reply_text("Hello! welcome to UD_bot")
    
def help(update , context):
    update.message.reply_text(
    """
    /start -> Welcome to the channel
    /help -> This is the help message
    /content -> About various playlist of Music
    /indian_classical -> The first playlist of indian classical
    /bollywood_songs -> The first playlist of bollywood songs
    /jazz_music -> The first playlist of jazz music
    /hollywood_songs -> The first playlist of hollywood songs
    /contact -> contact information
    """
    )    
    
def content(update , context):
    update.message.reply_text("We have various type  playlist and albums of music")

def indian_classical(update , context):
    update.message.reply_text("playlist of indian Classical link : https://open.spotify.com/playlist/37i9dQZF1DX3LrQBSMX6aK?si=QbNGpxPdSomxMeGcEGmqcA&utm_source=copy-link")

def bollywood_songs(update , context):
    update.message.reply_text("playlist of bollywood songs link :  https://open.spotify.com/playlist/7sTkp2X5Aq84v9w9UtfkaF?si=f9ZfProOTUuyNjVwEUl4kQ&utm_source=copy-link")

def jazz_music(update , context):
    update.message.reply_text("playlist of  jazz music : https://open.spotify.com/playlist/37i9dQZF1DXbITWG1ZJKYt?si=d0xJSng6R32t4DtijEvsQw&utm_source=copy-link")   
    
def hollywood_songs(update , context):
    update.message.reply_text("playlist of hollywood songs link : https://open.spotify.com/playlist/44j7hYaG0v6DEh9egqVWzw?si=bjpu3n1UQrSmTUAvk1KWoA&utm_source=copy-link")

def contact(update , context):
    update.message.reply_text("you can contact on the registered mail id provided on the website")

dispatcher.add_handler(telegram.ext.CommandHandler('start',start)) 
dispatcher.add_handler(telegram.ext.CommandHandler('help',help)) 
dispatcher.add_handler(telegram.ext.CommandHandler('contact',contact)) 
dispatcher.add_handler(telegram.ext.CommandHandler('indian_classical',indian_classical)) 
dispatcher.add_handler(telegram.ext.CommandHandler('bollywood_songs',bollywood_songs)) 
dispatcher.add_handler(telegram.ext.CommandHandler('jazz_music', jazz_music)) 
dispatcher.add_handler(telegram.ext.CommandHandler('hollywood_songs', hollywood_songs)) 




updater.start_polling()
updater.idle() 