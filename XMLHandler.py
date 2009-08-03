
import xml.sax

class XMLHandler(xml.sax.handler.ContentHandler):

    __elem = None
    __elems = None
    __flags = {}
    __vals  = {}
    ret_list = []
    
    def set_elem(self, elem):
        self.__elem = elem
        self.__flags = {}
        self.__flags[self.__elem] = False
        
    def set_elems(self, elems):
        self.__elems = elems
        for elem in self.__elems:
            self.__flags[elem] = False  
    
    def startElement(self, name, attrs):
        # If it's not a comic element, ignore it
#        print attrs.keys()
        name = str(name)
        if name == self.__elem:
            self.__flags[name] = True
            self.__vals = {}
        else:
            for elem in self.__flags:
                if name == elem and self.__flags[self.__elem]:
                    self.__flags[elem] = True
        for attr in attrs.keys():
            attr = str(attr)
            for elem in self.__elems:
                if attr == elem:
                    self.__vals[attr] = str(attrs[attr])


    def characters(self, ch):
        for elem in self.__flags:
            if elem != self.__elem and self.__flags[elem]:
		if not elem in self.__vals:
	                self.__vals[elem] = ch
		else:
	                self.__vals[elem] += ch

    def endElement(self, name):
        if str(name) == self.__elem:
            self.ret_list.append( self.__vals )
        if name in self.__elems:
            self.__flags[name] = False
                
if __name__ == '__main__':
    
    content = '''<?xml version="1.0" encoding="UTF-8"?>
<ResultSet xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:yahoo:srch" xsi:schemaLocation="urn:yahoo:srch http://api.search.yahoo.com/WebSearchService/V1/WebSearchResponse.xsd" type="web" totalResultsAvailable="306000000" totalResultsReturned="10" firstResultPosition="1" moreSearch="/WebSearchService/V1/webSearch?query=Madonna&amp;appid=YahooDemo&amp;region=us">
<Result><Title>Madonna</Title><Summary>Official site of pop diva Madonna, with news, music, media, and fan club.</Summary><Url>http://www.madonna.com/</Url><ClickUrl>http://www.madonna.com/</ClickUrl><DisplayUrl>www.madonna.com/</DisplayUrl><ModificationDate>1236754800</ModificationDate><MimeType>text/html</MimeType>
<Cache><Url>http://uk.wrs.yahoo.com/_ylt=A0WTeemakbhJrSQBBRfdmMwF;_ylu=X3oDMTBwZTdwbWtkBGNvbG8DZQRwb3MDMQRzZWMDc3IEdnRpZAM-/SIG=155mmu1vd/EXP=1236919066/**http%3A//74.6.239.67/search/cache%3Fei=UTF-8%26appid=YahooDemo%26query=Madonna%26u=www.madonna.com/%26w=madonna%26d=A_opCp2uScRN%26icp=1%26.intl=us</Url><Size>145030</Size></Cache>
</Result>

<Result><Title>Madonna (Entertainer) - Wikipedia</Title><Summary>Exhaustive bio and discography of Madonna\'s early life, career, "Sex" controversy, electronic club mix phase, and more.</Summary><Url>http://en.wikipedia.org/wiki/Madonna_(entertainer)</Url><ClickUrl>http://en.wikipedia.org/wiki/Madonna_(entertainer)</ClickUrl><DisplayUrl>en.wikipedia.org/wiki/Madonna_(entertainer)</DisplayUrl><ModificationDate>1236668400</ModificationDate><MimeType>text/html</MimeType>

<Cache><Url>http://uk.wrs.yahoo.com/_ylt=A0WTeemakbhJrSQBCBfdmMwF;_ylu=X3oDMTBwbGppbHRwBGNvbG8DZQRwb3MDMgRzZWMDc3IEdnRpZAM-/SIG=1687mgu41/EXP=1236919066/**http%3A//74.6.239.67/search/cache%3Fei=UTF-8%26appid=YahooDemo%26query=Madonna%26u=en.wikipedia.org/wiki/Madonna_%2528entertainer%2529%26w=madonna%26d=Hl5LlJ2uSb_n%26icp=1%26.intl=us</Url><Size>448709</Size></Cache>
</Result>

<Result><Title>Madonna - MySpace</Title><Summary>Madonna MySpace page features news, blog, music downloads, desktops, wallpapers, and more.</Summary><Url>http://www.myspace.com/madonna</Url><ClickUrl>http://www.myspace.com/madonna</ClickUrl><DisplayUrl>www.myspace.com/madonna</DisplayUrl><ModificationDate>1236754800</ModificationDate><MimeType>text/html</MimeType>
<Cache><Url>http://uk.wrs.yahoo.com/_ylt=A0WTeemakbhJrSQBCxfdmMwF;_ylu=X3oDMTBwbTJyZTk4BGNvbG8DZQRwb3MDMwRzZWMDc3IEdnRpZAM-/SIG=15c12qop0/EXP=1236919066/**http%3A//74.6.239.67/search/cache%3Fei=UTF-8%26appid=YahooDemo%26query=Madonna%26u=www.myspace.com/madonna%26w=madonna%26d=YjGIGZ2uScVM%26icp=1%26.intl=us</Url><Size>157867</Size></Cache>

</Result>

<Result><Title>YouTube - madonna\'s Channel</Title><Summary>The Official Madonna YouTube Channel. Want to Subscribe? ... http://www.youtube.com/Madonna. Sharing Options (close) There are 3 ways to share this channel.</Summary><Url>http://youtube.com/madonna</Url><ClickUrl>http://youtube.com/madonna</ClickUrl><DisplayUrl>youtube.com/madonna</DisplayUrl><ModificationDate>1236754800</ModificationDate><MimeType>text/html</MimeType>
<Cache><Url>http://uk.wrs.yahoo.com/_ylt=A0WTeemakbhJrSQBDhfdmMwF;_ylu=X3oDMTBwZTk1MWZqBGNvbG8DZQRwb3MDNARzZWMDc3IEdnRpZAM-/SIG=15880on13/EXP=1236919066/**http%3A//74.6.239.67/search/cache%3Fei=UTF-8%26appid=YahooDemo%26query=Madonna%26u=youtube.com/madonna%26w=madonna%26d=aKtFg52uSceF%26icp=1%26.intl=us</Url><Size>51216</Size></Cache>
</Result>

<Result><Title>Madonna Music Profile on IMEEM</Title><Summary>4 Minutes - Behind the Scenes (Music Video) by Madonna. Give It 2 Me (Music ... first disable your pop-up blocker or add imeem.com to your pop-up "safe" list.</Summary><Url>http://www.imeem.com/madonna</Url><ClickUrl>http://www.imeem.com/madonna</ClickUrl><DisplayUrl>www.imeem.com/madonna</DisplayUrl><ModificationDate>1236754800</ModificationDate><MimeType>text/html</MimeType>

<Cache><Url>http://uk.wrs.yahoo.com/_ylt=A0WTeemakbhJrSQBERfdmMwF;_ylu=X3oDMTBwMHMxbzJlBGNvbG8DZQRwb3MDNQRzZWMDc3IEdnRpZAM-/SIG=15a8h4q8d/EXP=1236919066/**http%3A//74.6.239.67/search/cache%3Fei=UTF-8%26appid=YahooDemo%26query=Madonna%26u=www.imeem.com/madonna%26w=madonna%26d=b89YRp2uSceF%26icp=1%26.intl=us</Url><Size>103598</Size></Cache>
</Result>

<Result><Title>Madonna | Music Artist | Videos, News, Photos &amp;amp; Ringtones | MTV</Title><Summary>Madonna profile page, featuring news, video and audio, photo gallery, and biography.</Summary><Url>http://www.mtv.com/music/artist/madonna/artist.jhtml</Url><ClickUrl>http://www.mtv.com/music/artist/madonna/artist.jhtml</ClickUrl><DisplayUrl>www.mtv.com/music/artist/madonna/artist.jhtml</DisplayUrl><ModificationDate>1235203200</ModificationDate><MimeType>text/html</MimeType></Result>

<Result><Title>AbsoluteMadonna.com</Title><Summary>Latest news, forum, FAQ, lyrics, photos, and chart and award statistics.</Summary><Url>http://www.absolutemadonna.com/</Url><ClickUrl>http://www.absolutemadonna.com/</ClickUrl><DisplayUrl>www.absolutemadonna.com/</DisplayUrl><ModificationDate>1236668400</ModificationDate><MimeType>text/html</MimeType>

<Cache><Url>http://uk.wrs.yahoo.com/_ylt=A0WTeemakbhJrSQBFhfdmMwF;_ylu=X3oDMTBwYzVtbTc0BGNvbG8DZQRwb3MDNwRzZWMDc3IEdnRpZAM-/SIG=15d3bc29v/EXP=1236919066/**http%3A//74.6.239.67/search/cache%3Fei=UTF-8%26appid=YahooDemo%26query=Madonna%26u=www.absolutemadonna.com/%26w=madonna%26d=YGiqwZ2uScC6%26icp=1%26.intl=us</Url><Size>68674</Size></Cache>
</Result>

<Result><Title>Madonnalicious</Title><Summary>Pictures, articles, downloads, concert info, news, and more about Madonna.</Summary><Url>http://www.madonnalicious.com/</Url><ClickUrl>http://www.madonnalicious.com/</ClickUrl><DisplayUrl>www.madonnalicious.com/</DisplayUrl><ModificationDate>1231142400</ModificationDate><MimeType>text/html</MimeType>
<Cache><Url>http://uk.wrs.yahoo.com/_ylt=A0WTeemakbhJrSQBGRfdmMwF;_ylu=X3oDMTBwbnBydmMxBGNvbG8DZQRwb3MDOARzZWMDc3IEdnRpZAM-/SIG=15c5juo52/EXP=1236919066/**http%3A//74.6.239.67/search/cache%3Fei=UTF-8%26appid=YahooDemo%26query=Madonna%26u=www.madonnalicious.com/%26w=madonna%26d=QO6U_Z2uScXx%26icp=1%26.intl=us</Url><Size>969</Size></Cache>
</Result>

<Result><Title>Madonna Rehabilitation Hospital</Title><Summary>Catholic facility devoted entirely to physical rehabilitation, serving all faiths.</Summary><Url>http://www.madonna.org/</Url><ClickUrl>http://www.madonna.org/</ClickUrl><DisplayUrl>www.madonna.org/</DisplayUrl><ModificationDate>1236754800</ModificationDate><MimeType>text/html</MimeType>
<Cache><Url>http://uk.wrs.yahoo.com/_ylt=A0WTeemakbhJrSQBHBfdmMwF;_ylu=X3oDMTBwdTQxbTI5BGNvbG8DZQRwb3MDOQRzZWMDc3IEdnRpZAM-/SIG=155utgaj0/EXP=1236919066/**http%3A//74.6.239.67/search/cache%3Fei=UTF-8%26appid=YahooDemo%26query=Madonna%26u=www.madonna.org/%26w=madonna%26d=O0ZJJ52uScY7%26icp=1%26.intl=us</Url><Size>12070</Size></Cache>
</Result>

<Result><Title>All About Madonna</Title><Summary>Fan site featuring bio, latest news, picture gallery, audio-video downloads, and forum for Madonna.</Summary><Url>http://www.allaboutmadonna.com/</Url><ClickUrl>http://www.allaboutmadonna.com/</ClickUrl><DisplayUrl>www.allaboutmadonna.com/</DisplayUrl><ModificationDate>1236668400</ModificationDate><MimeType>text/html</MimeType>

<Cache><Url>http://uk.wrs.yahoo.com/_ylt=A0WTeemakbhJrSQBHxfdmMwF;_ylu=X3oDMTBxcGs5ZDY0BGNvbG8DZQRwb3MDMTAEc2VjA3NyBHZ0aWQD/SIG=15dajdrs6/EXP=1236919066/**http%3A//74.6.239.67/search/cache%3Fei=UTF-8%26appid=YahooDemo%26query=Madonna%26u=www.allaboutmadonna.com/%26w=madonna%26d=cmD2Up2uScEj%26icp=1%26.intl=us</Url><Size>184434</Size></Cache>
</Result>
</ResultSet>
<!-- ws05.search.re2.yahoo.com compressed/chunked Wed Mar 11 21:37:46 PDT 2009 -->
    '''
    
    handler = XMLHandler()
    handler.set_elem('ResultSet')
    handler.set_elems(['totalResultsAvailable'])
    xml.sax.parseString(content, handler)
    
    self_attrs, node_dict, link_dict = [], {}, {}
    for ret in handler.ret_list:
        print str(ret)
