def main():
	f=open('test.txt','r',encoding='utf-8')
	lines=""
	for x in f:
		if ('【' in x) or (x=='\n'):continue
		lines+=x
	f.close()
	f=open('message.txt','w',encoding='utf-8')
	f.write(lines)
	f.close()
main()