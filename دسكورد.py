import os
import time
import random

# تثبيت مكتبة requests إذا غير مثبتة
try:
    import requests
except ImportError:
    print("جارٍ تثبيت مكتبة requests...")
    os.system("pip install requests")
    import requests

def load_messages(filename):
    if not os.path.exists(filename):
        print(f"الملف {filename} غير موجود! أنشئه وضع فيه الرسائل.")
        exit()
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        print("الملف فارغ! أضف بعض الرسائل.")
        exit()
    return lines

def main():
    token = "MTIxMjI2OTcyOTEwMDcyNjI5Mw.GH5z0E.ro6U8pwlt1C8MJPILIPYqxCYbKvoxICBPnt33s"
    channel_id = "1330137673389838416"
    
    # قائمة الـ IDs اللي تبي تمنشنهم كلهم مع كل رسالة
    user_ids = [
        "1003254064223629373",
        "1261293345297141786", 
        "893792041593610251" , "1358635602039541782" ,"1254413632108888064" , "1368901454969966722" , "1014388423009767546"
    ]

    delay = 1.5  # ثواني بين كل رسالة

    messages = load_messages("رسائل.txt")

    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    print("\nبدأ الإرسال العشوائي مع منشن للجميع...\nاضغط Ctrl+C لإيقافه.\n")

    while True:
        message = random.choice(messages)
        
        # إضافة جميع المنشنات في أول الرسالة
        mentions = " ".join([f"<@{uid}>" for uid in user_ids])
        full_message = f"{mentions} {message}"

        payload = {
            "content": full_message
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            print(f"تم الإرسال: {full_message}")
        else:
            print(f"خطأ: {response.status_code} | {response.text}")

        time.sleep(delay)

if __name__ == "__main__":
    main()