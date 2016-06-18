import json
def makeHTML(content):
	res = json.loads(content)
	html = '<html><head></head><body width="300px" height="150px">' + \
	 '<h4>URL</h4><p>' + res['url'] + '</p>' + \
	 '<h4>Evil</h4><p>' + res['evil'] + '</p>' + \
	 '<h4>Search num</h4><p>' + res['num'] + '</p>' + \
	 '<h4>Search title</h4><p>' + res['title'] + '</p>' + \
	 '<h4>Search content</h4><p>' + res['content'] + '</p>' + \
	 '<h4>SSL Grade</h4><p>' + res['grade'] + '</p>' + \
	 '</body></html>'
	return html