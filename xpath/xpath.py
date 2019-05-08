from lxml import etree
import requests
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
url = 'https://hr.tencent.com/position.php?lid=2218&start=0#a'
html = requests.get(url=url,headers=headers)# html.text未经过编码的字符串，unicode字符串
etree_obj = etree.HTML(html.text)			# HTML解析的是字符串，所以html.text
result = etree_obj.xpath("//table[@class='tablelist']//tr[position()>1][position()<11]//text()")
print(result,'\n')
# 去除转义字符
result2 = [x.strip() for x in result if x.strip() != '']
print(result2,'\n')
# 输出最终格式
[print(result2[x],result2[x+1],result2[x+2],result2[x+3],result2[x+4]) for x in range(0,len(result2),5)]
