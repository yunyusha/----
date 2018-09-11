import re
tt = "Tina is a good girl, she is cool,clever,and so on"
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))  # 查找所有包含'oo'的单词
a = re.search(r'(tina)(fei)haha\2', 'tinafeihahafei tinafeihahatina').group()
print(a)

