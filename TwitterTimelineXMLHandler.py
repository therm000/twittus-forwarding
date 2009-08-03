
from XMLHandler import XMLHandler
import xml.sax

class TwitterTimelineXMLHandler(XMLHandler):
    
    def __init__(self):
        self.set_elem('item')
        self.set_elems(['description', 'guid'])
        self.ret_list = []        
        

                
if __name__ == '__main__':
    
    content = open('friends_timeline.rss').read()
    
    handler = TwitterTimelineXMLHandler()
    xml.sax.parseString(content, handler)

    self_attrs, node_dict, link_dict = [], {}, {}
#    for ret in handler.ret_list:
#        print str(ret)

    t_list = [(dic['guid'],dic['description']) for dic in handler.ret_list]
    print [(guid.split('/')[-1],desc) for (guid, desc) in t_list]
