from xml.sax.handler import ContentHandler
from xml.sax import parse

class PageMaker(ContentHandler):
    passthrough = False
    def startElement(self, name, attrs):
        if name == 'page':
            self.passthrough = True
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html><head>\n')
            self.out.write('<title>{}</title>'.format(attrs['title']))
            self.out.write('</head></body>\n')
        elif self.passthrough:
            self.out.write('<'+name)
            for key, val in attrs.items():
                self.out.write("{}={}".format(key, val))
            self.out.write('>')
            
    def endElement(self, name):
        if name == 'page':
            self.passthrough = False
            self.out.write('\n</body></html>')
            self.out.close()
        elif self.passthrough:
            self.out.write('</{}>'.format(name))
            
    def characters(self, chars):
        if self.passthrough:
            self.out.write(chars)        
        

class TestHandler(ContentHandler):
    def startElement(self, name, attrs):
        print(name, attrs.keys())
    
class HeadlineHandler(ContentHandler):
    def __init__(self, headlines):
        ContentHandler.__init__(self)
        self.headlines = headlines
        self.in_headlines = False
        self.data = []
        
    def startElement(self, name, attrs):
        if name == 'h1':
            self.in_headlines = True
        
    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data= []
            self.headlines.append(text)
            self.in_headlines = False
            
    def characters(self, string):
        if self.in_headlines:
            self.data.append(string)

parse('website.xml', PageMaker())
"""            
headlines = []
parse('website.xml', HeadlineHandler(headlines))

for h in headlines:
    print h
"""