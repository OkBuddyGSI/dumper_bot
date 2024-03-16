from info import *
import random
import os

dump_methods = ["dump_gh_actions.sh"]
vndr_gen_script = "vendor_tree.sh"
botid = 7004812988
request_id = [-1001263694109, -1002108265780]

def command(m): 
    if m.text == "/start":
        bot.reply_to(m, "Hi, if you want to use me please join here: https://t.me/+_uajqfCeH6Y4ZWJl")
        bot.send_message(m.chat.id, f"This bot is made by {bot_creator}")
    if m.text.split()[0] =="/request" or m.text.split()[0] =="/dump":
        if m.chat.id in request_id:
            dump(m)
        else:
            bot.reply_to(m, "Please join this group and use me there: https://t.me/+_uajqfCeH6Y4ZWJl")
    if m.text.split()[0] == "/vt":
        if m.chat.id in request_id:
            vndr_gen(m)
        else: 
            bot.reply_to(m, "Please join this group and use me there: https://t.me/+_uajqfCeH6Y4ZWJl")
    if m.text.split()[0] == "/workflows":
        try:
            request = m.text.split()[1]
            if request == "vendor":
                return_workflows(m, "vendor")
            else:
                return_workflows(m, "dump")
        except:
            bot.reply_to(m, "Something bad happened bruv")
def dump(m):
    try:
        URL = m.text.split()[1]
        dump_method = random.choice(dump_methods)
        result = os.system(f'bash {dump_method} {URL}')
        if result == 0:
            bot.reply_to(m, "Succesfully requested the dump!")
            bot.reply_to(m, "You can follow the progress here: https://github.com/OkBuddyGSI/AndroidDumpsCI/actions")
        else:
            bot.reply_to(m, "Something went wrong")
    except:
        bot.send_message(m.chat.id, "I need a url to work")

def vndr_gen(m):
    try:
        dump_link = m.text.split()[1]
        dump_branch = m.text.split()[2]
        device_tree_link = m.text.split()[3]
        device_tree_branch = m.text.split()[4]
        codename = m.text.split()[5]
        vendor = m.text.split()[6]
        result = os.system(f'bash {vndr_gen_script} {dump_link} {dump_branch} {device_tree_link} {device_tree_branch} {codename} {vendor}')
        if result == 0:
            bot.reply_to(m, "Succesfully requested the vendor tree generation!")
            bot.reply_to(m, "You can follow the progress here: https://github.com/OkBuddyGSI/AndroidDumpsCI/actions")
        else:
            bot.reply_to(m, "Something went wrong")
    except:
        bot.reply_to(m, "Please give all the arguments in the correct order")
        bot.reply_to(m, "Usage is as follows: /vt {dump_link} {dump_repo_branch} {device_tree_link} {device_tree_branch} {device_codename} {device_vendor_name}")
        bot.reply_to(m, "example: /vt https://gitlab.com/sounddrill311/infinix/Infinix-X6816/-/tree/sys_tssi_64_infinix-user-11-RP1A.200720.011-287229-release-keys/ sys_tssi_64_infinix-user-11-RP1A.200720.011-287229-release-keys https://github.com/IMYdev/android_device_infinix_X6816 lineage-20 X6816 Infinix")

def return_workflows(m, workflow):
    if workflow == "vendor":
        list = "cd extract_proprietary_blobs && gh run list --workflow=extract-blobs.yml"
        result = os.popen(list)
        workflows = 1
        for i in result.readlines():
            while workflows < 6:
                bot.reply_to(m, i)
                workflows += 1
    if workflow == "dump":
        list = "cd AndroidDumpsCI && gh run list --workflow=DumprX.yml"
        result = os.popen(list)
        workflows = 1
        for i in result.readlines():
            while workflows < 6:
                bot.reply_to(m, i)
                workflows += 1
        