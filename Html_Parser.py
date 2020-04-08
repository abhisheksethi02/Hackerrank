'''
You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.
'''

import re
from html.parser import HTMLParser
if __name__ == "__main__":
    class MyHTMLParser(HTMLParser):
        def handle_comment(self, data):
                return super().handle_comment(data)
        def handle_starttag(self, tag, attrs):
            print('Start :',tag)
            for name, value in attrs:
                if value is None:
                    print('->',name, '> None')
                else :
                    print('->',name,'>',value)
        def handle_endtag(self, tag):
            print('End   :',tag)
        def handle_startendtag(self, tag, attrs):
            print('Empty :',tag)
    parser = MyHTMLParser()
    for _ in range(int(input())):
        parser.feed(input())