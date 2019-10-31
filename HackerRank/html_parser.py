from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        import re
        if re.search('\n', data):
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)

    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)


parser = MyHTMLParser()
parser.feed("<!--[if IE 9]>IE9-specific content\n<![endif]-->\n<div> Welcome to HackerRank</div>\n<!--[if IE 9]>IE9-specific content<![endif]-->")
