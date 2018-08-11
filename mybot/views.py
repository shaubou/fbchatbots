from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from mybot.messenger_api import *
from mybot.fb_setting import *
from mybot.data_search import *
from mybot.feedbackmail import *
from mybot.keyword_process import *
import random,time

search_detail_data = []
search_detail_data_contend = []
title = None
body = 0
waitfeedbackflag = 0

def post_facebook_message(fbid, recevied_message):
    global search_detail_data,search_detail_data_contend
    global datasearchtitle,datasearchlink,body,waitfeedbackflag
    global analyse_word
    print("recevied_message0", recevied_message)
    print("search_detail_data0",search_detail_data)
    print("recevied_message[len(recevied_message)-1]",recevied_message[len(recevied_message)-1])
    fb = FbMessageApi(fbid)
    print("00000000")
    if recevied_message in hello_word:
        print(random.choice(hello_word))
        fb.text_message(random.choice(hello_word))
        time.sleep(5)
        home_page(fb)
        return
    print("00000001")
    if recevied_message in recevied_message_dict:
        fb.text_message(recevied_message_dict[recevied_message])
        return
    print("00000002")
    if recevied_message == "首頁":
        home_page(fb)
        return
    print("00000003")
    if recevied_message == "基本資料":
        for i in recevied_message_dict:
            fb.text_message(i)
            fb.text_message(recevied_message_dict[i])
        home_page(fb)
        return
    print("00000004")
    if recevied_message == "意見回饋":
        content = "請輸入您的寶貴建議，作為我們改進的參考！."
        fb.text_message(content)
        return
    print("00000005")
    if recevied_message == "請輸入您的寶貴建議，作為我們改進的參考！.":
        waitfeedbackflag = 1
        return
    print("00000006")
    if waitfeedbackflag == 1:
        body = recevied_message
        content = "您的意見回饋內容是：" + body + "."
        fb.text_message(content)
        waitfeedbackflag = 0
        selectdata = ["首頁", "重新輸入", "正確並傳送"]
        title = "請選擇選單項目或重新輸入查詢內容."
        quick_answer(fb, title, selectdata)
        return
    print("00000007")
    if recevied_message == "重新輸入":
        content = "請輸入您的寶貴建議，作為我們改進的參考！."
        fb.text_message(content)
        return
    print("00000009")
    if recevied_message == "正確並傳送":
        content = "您的意見回饋已透過郵件傳送給管理者，非常感謝您！."
        fb.text_message(content)
        feedback_mail(body)
        body = ""
        time.sleep(5)
        home_page(fb)
        return
    print("00000010")
    if recevied_message == "下一頁":
        data_list(fb)
        return
    print("00000011")
    if recevied_message in search_detail_data:
        print("ghgghghg",recevied_message)
        data_list(fb)
        return
    print("00000012")
    if recevied_message in datasearchtitle:
        print("recevied_messagekc", recevied_message)
        count = datasearchtitle.index(recevied_message)
        print("count", count)
        search_link_data = datasearchlink[count]
        print("search_link_data",search_link_data)
        search_detail_link = yahoodetaillink(search_link_data)
        print("search_detail_link",search_detail_link)
        search_detail_data=yahoodetailsearch(search_detail_link)
        search_detail_data_contend = search_detail_data
        print("search_detail_data",str(search_detail_data))
        data_list(fb)
        return
    print("00000013")
    #if recevied_message[0] != ".":
    if recevied_message[len(recevied_message)-1] != ".":
        print("recevied_message8", recevied_message)
        print("recevied_message8", str(recevied_message)[0])
        print("str(recevied_message)[0]2=", str(recevied_message)[0])
        recevied_message=jieba_analyse(recevied_message)
        print("jieba_analyse",recevied_message)
        search_detail_data = wikisearch(recevied_message)
        search_detail_data_contend = search_detail_data
        print("recevied_messagejf", recevied_message)
        print("search_detail_data", search_detail_data)
        if search_detail_data == []:
            print("recevied_message11", recevied_message)
            yahoodatasearch(recevied_message)
            print("datasearchtitle", datasearchtitle)
            title = "請左右移動選擇最適合您的問題項目：."
            quick_answer(fb, title, datasearchtitle)
            return
        elif search_detail_data != []:
            data_list(fb)
            print("recevied_messageLIST", recevied_message)
            return
        return

def data_list(fb):
    if search_detail_data_contend == []:
        #print("recevied_message7", recevied_message)
        selectdata = ["首頁", "基本資料"]
        title = "已無資料，請選擇選單項目或重新輸入查詢內容."
        quick_answer(fb, title, selectdata)
        return
    elif search_detail_data_contend != []:
        for i in search_detail_data_contend:
            print("idata i111", i)
            fb.text_message(str(i))
            search_detail_data_contend.remove(i)
            if search_detail_data_contend != []:
                print("idata i222")
                selectdata = ["首頁", "下一頁"]
                title = "請選擇選單項目或重新輸入查詢內容."
                quick_answer(fb, title, selectdata)
                return
            elif search_detail_data_contend == []:
                print("idata i333")
                selectdata = ["首頁", "基本資料"]
                title = "已無資料，請選擇選單項目或重新輸入查詢內容."
                quick_answer(fb, title, selectdata)
                return
    return
def quick_answer(fb,title,quick_answer_list):
    print("quick_answer")
    data = []
    for i in quick_answer_list:
        print("i",i)
        quick_message_dic = {
            "content_type": "text",
            "title": i,
            "payload": i
        }
        data.append(quick_message_dic)
    print("data",data)
    fb.quick_reply_message(
        text=title,
        quick_replies=data)
    return

def home_page(fb):
    data = [
        {
            "type": "postback",
            "title": "基本資料",
            "payload": "基本資料"
        },
        {
            "type": "postback",
            "title": "意見回饋",
            "payload": "意見回饋"
        }
    ]
    fb.template_message(
        title="禾韻藥局(健保特約)自動回覆客服系統，請直接輸入醫療保健相關問題之文字即可！.",
        image_url="https://i.imgur.com/kzi5kKy.jpg",
        subtitle="",
        data=data)
    return

class MyBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    # pprint(message)
                    print('message')
                    try:
                        post_facebook_message(message['sender']['id'], message['message']['text'])
                    except:
                        return HttpResponse()
                if 'postback' in message:
                    # pprint(message)
                    print('postback')
                    try:
                        post_facebook_message(message['sender']['id'], message['postback']['payload'])
                    except:
                        return HttpResponse()
        return HttpResponse()
