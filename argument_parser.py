import argparse

parser = argparse.ArgumentParser(description = '要看看如果我可以用 argparse 还不能')
parser.add_argument('-a', action = 'store', required = True, help = '要试试 python parser')
parser.add_argument('-b', help = '要看看如果一个东西是不重要在东西你我们有什么')
args = parser.parse_args()
print(args.a)
print(args.b)
if(args.b == None):
	print('argument b是 none如果我不给一个东西')

