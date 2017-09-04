#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import config

link_register = "https://www.reddit.com/message/compose?to=" + config.bot_name + "&subject=\%2Bregister&message=\%2Bregister"
link_help = "https://www.reddit.com/message/compose?to=" + config.bot_name + "&subject=%2Bhelp&message=%2Bhelp"
link_withdraw = "https://www.reddit.com/message/compose?to=" + config.bot_name + "&subject=%2Bwithdraw&message=%2Bwithdraw%20AMOUNT%20maga%20to%20ADDRESS"
link_history = "https://www.reddit.com/message/compose?to=" + config.bot_name + "&subject=%2Bhistory&message=%2Bhistory"
link_info = "https://www.reddit.com/message/compose?to=" + config.bot_name + "&subject=%2Binfo&message=%2Binfo"
link_balance = "https://www.reddit.com/message/compose?to=" + config.bot_name + "&subject=%2Bbalance&message=%2Bbalance"

link_gold = "https://www.reddit.com/gold/about"
link_gold_buy = "https://www.reddit.com/message/compose?to=" + config.bot_name + "&subject=%2Bgold&message=buy"

message_register_success = ("Hello /u/{{ username }}! Your account is now registered and ready to tip Magacoins :)" \
                            "\n\nYour wallet address is: {{ address }}" \
                            "\n\nThis bot is \"on chain\" so when you tip some __mining fee are added__ ! " \
                            "\n\nWondering how to get tipped Magacoins? Participate in /r/magacoin!" \
                            "\n\nIf you need help using me (such as tipping people), you can send me a +help message [here](" + link_help + ") to receive a getting started guide.")

message_need_register = ("Hello /u/{{ username }}! You need to register an account before you can use me." \
                         "\n\nTo register an account:" \
                         "\n\n1. [Click here](" + link_register + ") to send a pre-filled +register message" \
                                                                  "\n\n2. Click the \"Send\" button" \
                                                                  "\n\n3. Receive the successful register message" \
                                                                  "\n\nThe successful register message will contain your Magacoin address to your tipping account.")

message_invalid_amount = "__^[error]__: ^The ^tip ^amount ^must ^be ^at ^least ^1 ^maga. ^[[help]](" + link_help + ")"
message_invalid_currency = "__^[error]__: ^The ^tip ^currency ^must ^be ^maga. ^[[help]](" + link_help + ")"
message_balance_low_tip = (
    "__^[error]__: ^/u/{{ username }}\'s ^balance ^is ^too ^low ^for ^this ^tip ^[[help]](" + link_help + ")")
message_balance_pending_tip = (
    "__^[error]__: ^/u/{{ username }}\'s ^balance ^must ^wait ^for ^pending ^tips ^to ^be ^confirmed ^before ^sending ^this ^tip ^amount ^[[help]](" + link_help + ")")
message_already_registered = "You are already registered!\n\n__MAGA__"
message_balance_low_withdraw = (
    "Hello /u/{{ username }}! It seems your balance of __M{{ user_balance }}__ is too low for this withdraw amount of __M{{ amount }}__." \
    "\n\n[Want to try again?](" + link_withdraw + ")\n\n__MAGA__")

message_account_details = "\n\nHere are your account details /u/{{ username }}!" \
                          "\n\n^info | &nbsp;" \
                          "\n---|---" \
                          "\n^Your ^balance | ^{{ spendable_balance }} ^maga ^(${{ spendable_value_usd }})" \
                          "\n^Your ^pending ^balance | ^{{ unconfirmed_balance }} ^maga ^(${{ unconfirmed_value_usd }})" \
                          "\n^Tips ^to ^unregistered ^users | ^{{ pending_tips }} ^maga ^(${{ pending_tips_value_usd}})" \
                          "\n^Deposit ^address | ^{{ address }}" \
                          "\n^Withdraw | ^[+withdraw](" + link_withdraw + ")" \
                                                                          "\n\nATTENTION: This bot is \"on chain\" so for every tip you make, you'll pay a small fee!"

message_not_supported = "__^[error]__: ^That ^is ^currently ^not ^supported! ^[[help]](" + link_help + ")"

message_history = ("Hello /u/{{ username }}! Here is your transaction history: \n\n")
message_tip = (
    "__^[verified]__: ^/u/{{ sender }} ^-> ^/u/{{ receiver }} ^__M{{ amount }}__ ^__maga__ ^__(${{ value_usd }})__ ^[[help]](" + link_help + ")  ^[[transaction]](https://brickwall.info/tx/{{ txid }})")
message_withdraw = (
    "__^[verified]__: ^/u/{{ username }} ^-> ^{{ receiver_address }} ^__M{{ amount }}__ ^__maga__ ^__(${{ value_usd }})__ ^[[help]](" + link_help + ")")
message_withdraw_to_self = ("__^[error]__: ^You ^cannot ^withdraw ^to ^your ^own ^bot ^address")
message_footer = ("\n\n*****" \
                  "\n\nNew user? Ask the community any questions on /r/magacoin!" \
                  "\n\n^quick ^commands |&nbsp;" \
                  "\n---|---" \
                  "\n^Past ^tips|^[+history](" + link_history + ")" \
                  "\n^Get ^account ^details|^[+info](" + link_info + ")" \
                  "\n^Balance|^[+balance](" + link_balance + ")" \
                  "\n^Help ^me!|^[+help](" + link_help + ")" \
                  "\n\nPROTIP: An example tip would be: +/u/" + config.bot_name + " 100 maga"
                  "\n\n__MAGA__")

message_help = (
    "Welcome to Magacoin and " + config.bot_name + "!\n\nThe community is extremely important to us, and we\'re always happy to see new faces and continue building the brickwall :)\n\nTo learn more about Magacoin and experience our friendly community, check out the /r/magacoin subreddit. .\n\nUnlike other tipping services, " + config.bot_name + " is built on an \"on chain\" platform. This means every tip is verified by the secure Magacoin network and publically viewable on its database of transactions (called a brickwall) for a small fee.\n\nThis is your wallet address: {{ address }}\n\nHow to use " + config.bot_name + ":\n\nSend someone a Magacoin tip by commenting or replying: +/u/" + config.bot_name + " AMOUNT maga. Replace AMOUNT with an amount of Magacoins (ex. 100 to tip 100 MAGA).\n\n[+history](" + link_history + ") - view your transaction history (includes tips and withdraws)\n\n[+info](" + link_info + ") or [+balance](" + link_balance + ") - view your Magacoin balance on /u/" + config.bot_name + "\n\n[+withdraw](" + link_withdraw + ") - withdraw Magacoins from your /u/" + config.bot_name + " balance into a separate Magacoin address")

message_recipient_register = (
    "__^[error]__: ^/u/{{ username }} ^needs ^to ^[register](" + link_register + ") ^before ^receiving ^any ^tips. __^\(this ^tip ^has ^been ^saved ^for ^3 ^days)__ ^[[help]](" + link_help + ")\n\n__MAGA__")
message_recipient_need_register_title = (
    "Someone sent you a Magacoin tip of M{{ amount }}, and you need to register to receive it!\n\n__MAGA__")
message_recipient_need_register_message = (
    "Hello /u/{{ username }}! You need to register an account before you can receive __{{ sender }}\'s__ Magacoin tip of __M{{ amount }} maga (${{ value_usd }})__." \
    "\n\nTo register an account:" \
    "\n\n1. [Click here](" + link_register + ") to send a pre-filled +register message" \
                                             "\n\n2. Click the \"Send\" button" \
                                             "\n\n3. Receive the successful register message" \
                                             "\n\nThe successful register message will contain your Magacoin address to your tipping account.\n\n__MAGA__")
message_recipient_self = ("__^[error]__: ^You ^cannot ^send ^yourself ^a ^tip")

# Gold Message

message_buy_gold = "You can buy an reddit [gold](" + link_gold + "), price is {{ price }} for one month.\n\n " \
                                                                 "To buy send a [message](" + link_gold_buy + ") to bot with subject +gold an content 'buy' \n\n" \
                                                                                                              "The amount will be deducted on your wallet.\n\n" \
                                                                                                              "There are {{ gold_credit }} credits remaining for sale\n\n" \
                                                                                                              "The price is bit over than reddit price because it add fee to bitcoin exchange, support hosting cost, etc .."

message_gold_no_more = "Sorry no more gold tickets to sell"
message_buy_gold_error = "Error during buy of gold credits"
message_buy_gold_success = "Thanks to buy reddit gold via bot and support hosting cost, all coffee for developpers, etc ..."

message_gold_no_enough_maga = "Sorry it seems your confirmed balance is too low"