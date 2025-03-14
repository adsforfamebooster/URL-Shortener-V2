from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
Need to shorten or convert links from all of your channel's posts? I've got you covered! Just make me an admin in your channel and use the following command:

<code>/batch [channel id or username]</code>

For example: <code>/batch -100xxx</code>

I'll handle the rest and get those links shortened or converted in a short time! 💪
"""

START_MESSAGE = """Hi there {} 👋😃

Welcome to [BrieflyUrl Bot](t.me/BrieflyUrl_Help) - Your Personal URL Shortener Bot. 🌐

Just send me a link, and I'll work my magic to shorten it for you. Plus, I'll keep track of your earnings! 💰💼

/shortener_api - Connect API
/me - Your profile setting
/help - Advanced setting

New User ? Then just sign up on BrieflyUrl.com and Get Highest Upto 8$ CPM rate & 10% Refer Earning Lifetime.
"""

HELP_MESSAGE = """Hey there! My name is {firstname} and I'm a link convertor and shortener bot here to make your work easier and help you earn more 💰.

I have a ton of handy features to help you out, such as:

•  Setup Header - /header 
•  Setup Footer - /footer 
•  Setup Username - /username 
•  Setup Banner Img - /banner_image 
•  Setup Include Domains - /include_domain  
•  Setup Exclude Domains - /exclude_domain 

Useful commands:

•  /start Go Back to Home.
•  /shortener_api - Setup or Change API 
•  /me - Your profile Settings 

Contact Help Support - @BrieflyUrl_Help
"""

ABOUT_TEXT = """
**Bot Details:**

`🤖 Name:` ** {} ** 
`📝 Language:` [Python 3](https://www.python.org/)
`👨‍💻 Developer:` [Dev](t.me/BrieflyUrl)
`📢 Support:` [Support Talk](https://t.me/BrieflyUrl_Help)
"""


CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""


CHANNELS_LIST_MESSAGE = """
Here is a list of the channels:

{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Custom Alias", callback_data="alias_conf"),
            InlineKeyboardButton("Home", callback_data="start_command"),
        ],
    ]
)


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Home", callback_data="start_command"),
            InlineKeyboardButton("Help", callback_data="help_command"),
        ],
        [InlineKeyboardButton("Close", callback_data="delete")],
    ]
)

START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Help", callback_data="help_command"),
            InlineKeyboardButton("About", callback_data="about_command"),
        ],
        [
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)

BACK_REPLY_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Back", callback_data="help_command")]]
)

USER_ABOUT_MESSAGE = """
<b>Current Setting Of Your Bot is Here:</b>

•  🌐 Shortener website: BrieflyUrl.com
•  🔌 BrieflyUrl API: {shortener_api}
•  📎 Username: @{username}
•  📝 Header text:
{header_text}
•  📝 Footer text:
{footer_text}
•  🖼️ Banner image: {banner_image}
"""

SHORTENER_API_MESSAGE = """<b>How To Connect API ?</b>

• First Visit BrieflyUrl.com/member/tools/api
• Copy the API Token & Comeback to the Bot.
• Put /shortener_api [api] Replace With Your API
• Done! Now Bot is Succesfully Connected With Your BrieflyUrl Account

To add or update your Shortner Website API, 
`/shortener_api [api]`
            
Ex: `/shortener_api 6LZq851sXofffPHugiKQq`

Current Shortener API: `{shortener_api}`"""

HEADER_MESSAGE = """📝 To set the header text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the header text, use the following command:

`/header remove`

This is a helpful way to add a consistent header to all of your messages. Enjoy! 🎉"""

FOOTER_MESSAGE = """📝 To set the footer text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the footer text, use the following command:

`/footer remove`

This is a helpful way to add a consistent footer to all of your messages. Enjoy! 🎉"""

USERNAME_TEXT = """Current username: {username}

To set the username that will be automatically replaced with other usernames in the post, use the following command:

`/username your_username`

__(Note: Do not include the @ symbol in your username.)__

To remove the current username, use the following command:

`/username remove`

This is a helpful way to make sure that all of your posts have a consistent username. Enjoy! 📎"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
