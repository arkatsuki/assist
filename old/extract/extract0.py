
import os

reposPath = r'D:\svn\format'

versionNumBegin = input('input begin version number: ')
versionNumEnd = input('input end version number: ')
user_name = input('input user name: ')
# versionNumBegin = 30050   29076
# versionNumEnd = 30125   30750

# user_name = 'duanyaochang'

# user_name = 'lifang'

# svn log -r 30050:30125 -v D:\svn\format

if versionNumBegin and versionNumEnd and user_name:
    svninfo = os.popen("svn log -r %s:%s -v %s --search %s" % (versionNumBegin ,versionNumEnd ,reposPath, user_name)).readlines()
else:
    '''
    versionNumBegin = 30050
    versionNumEnd = 30125
    svninfo = os.popen("svn log -r %s:%s -v %s" % (versionNumBegin, versionNumEnd, reposPath)).readlines()
    '''
    svninfo = []
"""
结果是一个list，需要一行行处理。
-----------  的下一行含有  版本号|提交人 。
Changed paths:  的下一行是文件路径和动作，再下一行是空格表明结束。

"""

filePathList = []   # 存放文件路径
output = []    # 整个输出文件

currentBaseInfo = []   # 保存版本号、提交人信息

logLen = len(svninfo)
j = 0

def writeFilePath(filePathListFun, outputFun, currentBaseInfoFun):
    '''
        filePathListFun  文件路径的list
        outputFun	用于输出的list
        currentBaseInfoFun   版本号、提交人信息
    '''
    '''
    print('begin filePathListFun','\n')
    print(filePathListFun)
    '''

    for pathItem in filePathListFun:
        outputFun.append(currentBaseInfoFun[0])
        outputFun.append('\t')
        outputFun.append(currentBaseInfoFun[1])
        outputFun.append('\t')

        action = pathItem[0]

        pathItemPath = pathItem[1:]
        idxDev = pathItemPath.find('DEV')
        pathItemPath = pathItemPath[idxDev:]

        outputFun.append(action)
        outputFun.append('\t')
        outputFun.append(pathItemPath)
        outputFun.append('\n')



while j < logLen- 1:  # 最后一行--------没有价值，反而会让下面的if越界
    if svninfo[j].startswith('----'):  # 一次提交记录的第一行
        j = j + 1  # 下一行
        svninfoItem = svninfo[j].split('|')
        if len(currentBaseInfo) < 2:
            currentBaseInfo.append(svninfoItem[0].strip()[1:])
            currentBaseInfo.append(svninfoItem[1].strip())
        else:
            currentBaseInfo[0] = svninfoItem[0].strip()[1:]
            currentBaseInfo[1] = svninfoItem[1].strip()

        continue

    if svninfo[j].startswith('Changed paths'):
        j = j + 1  # 下一行
        filePathList.append(svninfo[j].strip())

        while svninfo[j].strip() != '':
            filePathList.append(svninfo[j].strip())
            j = j + 1
        writeFilePath(filePathList, output, currentBaseInfo)
        continue
    j = j + 1

f = open(r'F:\py\lib-svn\outputSvn.txt', 'w')

f.write(''.join(output))  # write的参数需要是字符串，不能是List






