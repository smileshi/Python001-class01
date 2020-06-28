学习笔记
1. scrapy crawl xxx(spider name). this command should be run in settings.py path
2. can download the source and then use the source to test your xpath.
	from scrapy.selector import Selector

	body = open('e:/maoyan.html').read()
	#使用scrapy自身的Selector解析文本
	selector = Selector(text=body)
	content = selector.xpath('//div[@class="movie-hover-info"]')
	i = 0
	for item in selector.xpath('//div[@class="movie-hover-info"]').getall()[0:10]:
		i = i + 1
		print("i:" + str(i))
		# print(item)
		film_name = Selector(text=item).xpath('//span[contains(@class, "name ")]/text()').extract_first()
		film_type = Selector(text=item).xpath('//div/div[2]/text()').getall()[1].replace(' ', '').replace("\n", "")
		plan_date = Selector(text=item).xpath('//div/div[4]/text()').getall()[1].replace(' ', '').replace("\n", "")
		print(film_name)
		print(film_type)
		print(plan_date)
		
3. pip install -r required.txt
4. should learn more xpath rules.