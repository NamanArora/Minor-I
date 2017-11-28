from threading import Thread
import requests
import json
import time
import Queue

q= Queue.Queue()


def ajax_crawl(id):
    u="http://money.rediff.com/money1/currentstatus.php?companycode="+ str(id)
    res = requests.get(u)
    #print res.content
    j= json.loads(res.content)
    return j["LastTradedPrice"]


def worker(share,stop_loss, buy_price):
    risk_factor=1
    for i in range(0,10):
        response = ajax_crawl(14080006)
        current_price = int(float(response))
        profit = current_price-buy_price
        growth_per = (float(profit)/buy_price)*100
        if stop_loss + risk_factor >= current_price:
            print 'Share in *danger* zone. Sell now!'
        time.sleep(5)
        print 'Current rate = ' + str(current_price)
        print 'Stop loss @' + str(stop_loss)
        print 'Current profit/loss = ' + str(profit)
        print 'Growth of each share= ' + str(growth_per)
    q.task_done()

def assistant(share):
    stop_loss = int(raw_input('Enter your stop loss: '))
    buy_price = int(raw_input('Enter your buying price: '))
    q.put(0)
    t=Thread(target=worker, args=(share,stop_loss,buy_price))
    t.setDaemon(True)
    t.start()

    q.join()