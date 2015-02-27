>>> pdf.extract( [
...      ('with_parent','LTPage[pageid=1]'),
...      ('with_formatter', 'text'),
...
...      ('last_name', 'LTTextLineHorizontal:in_bbox("315,680,395,700")'),
...      ('spouse', 'LTTextLineHorizontal:in_bbox("170,650,220,680")'),
...
...      ('with_parent','LTPage[pageid=2]'),
...
...      ('oath', 'LTTextLineHorizontal:contains("perjury")', lambda match: match.text()[:30]+"..."),
...      ('year', 'LTTextLineHorizontal:contains("Form 1040A (")', lambda match: int(match.text()[-5:-1]))
...  ])
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
  File "/Users/usrNeko/.virtualenvs/pdfscraping/lib/python2.7/site-packages/pdfquery/pdfquery.py", line 358, in extract
    parent = pq(search) if search else pq
  File "/Users/usrNeko/.virtualenvs/pdfscraping/lib/python2.7/site-packages/pyquery/pyquery.py", line 264, in __call__
    result = self.__class__(*args, parent=self, **kwargs)
  File "/Users/usrNeko/.virtualenvs/pdfscraping/lib/python2.7/site-packages/pyquery/pyquery.py", line 239, in __init__
    xpath = self._css_to_xpath(selector)
  File "/Users/usrNeko/.virtualenvs/pdfscraping/lib/python2.7/site-packages/pyquery/pyquery.py", line 249, in _css_to_xpath
    return self._translator.css_to_xpath(selector, prefix)
  File "/Users/usrNeko/.virtualenvs/pdfscraping/lib/python2.7/site-packages/cssselect/xpath.py", line 192, in css_to_xpath
    for selector in parse(css))
  File "/Users/usrNeko/.virtualenvs/pdfscraping/lib/python2.7/site-packages/cssselect/parser.py", line 355, in parse
    return list(parse_selector_group(stream))
  File "/Users/usrNeko/.virtualenvs/pdfscraping/lib/python2.7/site-packages/cssselect/parser.py", line 370, in parse_selector_group
    yield Selector(*parse_selector(stream))
  File "/Users/usrNeko/.virtualenvs/pdfscraping/lib/python2.7/site-packages/cssselect/parser.py", line 378, in parse_selector
    result, pseudo_element = parse_simple_selector(stream)
  File "/Users/usrNeko/.virtualenvs/pdfscraping/lib/python2.7/site-packages/cssselect/parser.py", line 437, in parse_simple_selector
    result = parse_attrib(result, stream)
  File "/Users/usrNeko/.virtualenvs/pdfscraping/lib/python2.7/site-packages/cssselect/parser.py", line 535, in parse_attrib
    "Expected string or ident, got %s" % (value,))
cssselect.parser.SelectorSyntaxError: Expected string or ident, got <NUMBER '1' at 14>
