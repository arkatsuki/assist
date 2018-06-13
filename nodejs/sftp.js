


function te_demo_sftp(){
    // success
    let Client = require('ssh2-sftp-client');
    let sftp = new Client();
    sftp.connect({
        host: '192.168.200.238',
        port: 22,
        username: 'dev-sc',
        password : 'hgHHJ?@!#'
    }).then(() => {
        return sftp.list('/app');
    }).then((data) => {
        console.log(data, 'the data info');
    }).catch((err) => {
        console.log(err, 'catch error');
    });
}


function putToServer(local_path, remote_path){
    let Client = require('ssh2-sftp-client');
    let sftp = new Client();
    sftp.connect({
        host: '192.168.200.238',
        port: 22,
        username: 'dev-sc',
        password : 'hgHHJ?@!#'
    }).then(() => {
        return sftp.put(local_path, remote_path);
    }).then((data) => {
        console.log(data, 'the data info');
    }).catch((err) => {
        console.log(err, 'catch error');
    });
}


function get_files_from_dir_demo(dir_path_abs){
    // demo, success
    var fs = require('fs');
    var path = require('path');

    //解析需要遍历的文件夹，我这以E盘根目录为例
    // var filePath = path.resolve('D:/test-sth/test-dir');
    var filePath = path.resolve(dir_path_abs);

    //调用文件遍历方法
    fileDisplay(filePath);

    /**
     * 文件遍历方法
     * @param filePath 需要遍历的文件路径
     */
    function fileDisplay(filePath){
        //根据文件路径读取文件，返回文件列表
        fs.readdir(filePath,function(err,files){
            if(err){
                console.warn(err)
            }else{
                //遍历读取到的文件列表
                files.forEach(function(filename){
                    //获取当前文件的绝对路径
                    var filedir = path.join(filePath,filename);
                    //根据文件路径获取文件信息，返回一个fs.Stats对象
                    fs.stat(filedir,function(eror,stats){
                        if(eror){
                            console.warn('获取文件stats失败');
                        }else{
                            var isFile = stats.isFile();//是文件
                            var isDir = stats.isDirectory();//是文件夹
                            if(isFile){
                                console.log(filedir);
                            }
                            if(isDir){
                                fileDisplay(filedir);//递归，如果是文件夹，就继续遍历该文件夹下面的文件
                            }
                        }
                    })
                });
            }
        });
    }
}

/**
 * 文件遍历方法
 * @param filePath 需要遍历的文件路径
 */
function fileDisplay(filePath){
    var rs = new Array();
    var fs = require('fs');
    var path = require('path');
    //根据文件路径读取文件，返回文件列表
    fs.readdir(filePath,function(err,files){
        if(err){
            console.warn(err)
        }else{
            //遍历读取到的文件列表
            files.forEach(function(filename){
                //获取当前文件的绝对路径
                var filedir = path.join(filePath,filename);
                //根据文件路径获取文件信息，返回一个fs.Stats对象
                fs.stat(filedir,function(eror,stats){
                    if(eror){
                        console.warn('获取文件stats失败');
                    }else{
                        var isFile = stats.isFile();//是文件
                        var isDir = stats.isDirectory();//是文件夹
                        if(isFile){
                            console.log('filedir:' + filedir);
                            rs.push(filedir);
                        }
                        if(isDir){
                            fileDisplay(filedir);//递归，如果是文件夹，就继续遍历该文件夹下面的文件
                        }
                    }
                })
            });
        }
    });
    return rs;
}

function get_files_from_dir(dir_path_abs){
    
    // var rs = new Array();

    
    var path = require('path');

    //解析需要遍历的文件夹，我这以E盘根目录为例
    var filePath = path.resolve('D:/test-sth/test-dir');
    // var filePath = path.resolve(dir_path_abs);

    //调用文件遍历方法
    return fileDisplay(filePath);    
}

var rs = get_files_from_dir('D:/test-sth/test-dir')
console.log('rs:' + rs);
