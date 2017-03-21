import requests
r = requests.get('http://www.wise.xmu.edu.cn/people/faculty')
html = r.content
print(html)
