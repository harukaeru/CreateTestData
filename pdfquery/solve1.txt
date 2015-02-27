>>> pdf.extract( [
...      ('with_parent','LTPage[pageid="1"]'), ### HERE ###
...      ('with_formatter', 'text'),
...
...      ('last_name', 'LTTextLineHorizontal:in_bbox("315,680,395,700")'),
...      ('spouse', 'LTTextLineHorizontal:in_bbox("170,650,220,680")'),
...
...      ('with_parent','LTPage[pageid="2"]'), ### AND HERE ###
...
...      ('oath', 'LTTextLineHorizontal:contains("perjury")', lambda match: match.text()[:30]+"..."),
...      ('year', 'LTTextLineHorizontal:contains("Form 1040A (")', lambda match: int(match.text()[-5:-1]))
...  ])
{'last_name': 'Michaels', 'oath': 'Under penalties of perjury, I ...', 'spouse': 'Susan R.', 'year': 2007}
