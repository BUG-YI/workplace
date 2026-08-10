from lxml import etree

parse = etree.parse('./example.html')
xpath = parse.xpath('//div/ul/li/text()')
print(xpath)
