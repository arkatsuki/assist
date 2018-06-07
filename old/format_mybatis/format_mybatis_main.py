
import fileinput

with open(r'E:\workplace-eclipse-0706\workplace-dev\mybatis-app\src\main\java\com\sl\preloan\model\TestSsOperationRecord.java',
          'r+', encoding="utf-8") as f:
    for line in f.readlines():
        print(line)  # 把末尾的'\n'删掉

        f.seek(len(line.encode(encoding="utf-8")))
        # f.write('new line')
        # f.writelines()
        f.truncate(20)
        break

    pass
