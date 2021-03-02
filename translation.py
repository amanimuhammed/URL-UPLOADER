class Translation(object):

    START_TEXT = """Hello,

This is a Telegram URL Upload Bot!

<b>Please send me any Direct download URL link, I can upload to telegram as File/Video</b>

/help for more details..

Owner : @Amani_m_h_d
"""

    HELP_USER = """<b>Hai I'am a URL Uploader bot..</b>
    
1. Send url (Link | New Name with Extension).
2. Send Custom Thumbnail (Optional).
3. Select the button.

  <b>SVideo -</b> <code>Give File as video with Screenshots</code>
  <b>DFile -</b> <code>Give File with Screenshots</code>
  <b>Video -</b> <code>Give File as video without Screenshots</code>
  <b>DFile  -</b> <code>Give File without Screenshots</code>

Owner : @Amani_m_h_d
"""

     ABOUT_TEXT = """➠<b>My Name :</b> <code>URL UPLOADER🤓</code>
➠<b>Dev :</b> <a href='https://t.me/Amani_m_h_d'>Amani Muhammed</a>
➠<b>Credits :</b> <code>Everyone in this journey</code>
➠<b>Language :</b> <code>Python3</code>
➠<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 
➠<b>Server :</b> <a href='https://herokuapp.com/'>Heroku</a>
➠<b>Source Code :</b> 👉 <a href='http://t.me/nokkiirunnoippokittum'>Click Here</a>
    <b>📜Quote :</b> <code>ആരും പേടിക്കണ്ട എല്ലാവർക്കും കിട്ടും™️</code>"""


    FORMAT_SELECTION = """Select the desired format: <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /deletethumbnail to delete the auto-generated thumbnail."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    DOWNLOAD_START = "Downloading 📥📥..."
    
    UPLOAD_START = "Uploading now 🚀🚀.."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
