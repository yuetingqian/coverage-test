coverage-test
=============

python coverage test

### 环境要求
* python 2.7
* coverage.py (`sudo pip install coverage`),
    如果没有安装pip,`sudo apt-get install python-pip`

### 参考文档
* [python unintest](http://docs.python.org/2/library/unittest.html)
* [coverage.py](http://nedbatchelder.com/code/coverage/)

### code struct
```
|-- code.py     # 被测代码
|-- test.py     # 测试代码
|-- test.sh     # 执行测试代码的脚本
|-- .travis.yml # travis要用的配置文件，下面再讲
```
### 使用
* unittest only
```
python -m unittest test     # 执行test.py单元测试
```

* coverage unitest
```
./test.sh  # 执行test.sh覆盖率脚本
```

### 详细说明        
* unittest
    例如 `test.py`

    class继承unittest.Testcase
  
    testcase以小写test开头
  
    最后都要有断言，如`assertEqual()`


* coverage
```
coverage run test.py    # 执行test.py
coverage report -m      # 生成简单的report
coverage html           # 生成html report, 默认存在hmtlcov下面，-d可以指定目录
```

* .travis.yml
    如果你把代码push到github上面，访问[travis](https://travis-ci.org/)

    授权登录后点右上角Accounts,在repos里打开要同步的项目。

    每当该项目有commit的时候，travis会自动通过`.travis.yml`自动build

    具体配置方法[build-config](http://about.travis-ci.org/docs/user/build-configuration/#.travis.yml-file%3A-what-it-is-and-how-it-is-used)
