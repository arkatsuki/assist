


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

function putDIrToServer(local_dir_path, remote_dir_path){
    let Client = require('ssh2-sftp-client');
    let sftp = new Client();
    sftp.connect({
        host: '192.168.200.238',
        port: 22,
        username: 'dev-sc',
        password : 'hgHHJ?@!#'
    }).then(() => {
        var path = require('path');
        // dirname = path.dirname(local_dir_path)
        // console.log('dirname:' + dirname);

        var filesArr = get_files_from_dir(local_dir_path);
        for(var i=0;i<filesArr.length;i++){
            var local_file_path = filesArr[i];
            // console.log(typeof local_file_path);
            local_file_path = local_file_path.split('\\').join('/');
            // local_file_path = local_file_path.replace('/\\\\/g','/');
            // local_file_path = local_file_path.replace('\\','/');
            console.log('local_file_path:', local_file_path);
            remote_file_path = local_file_path.replace(local_dir_path, remote_dir_path)
            console.log('remote_file_path:', remote_file_path);
            sftp.mkdir(path.dirname(remote_file_path), true);
            sftp.put(local_file_path, remote_file_path);
        }

        
    }).then((data) => {
        // console.log(data, 'the data info');
    }).catch((err) => {
        console.log(err, 'catch error');
    });
    // sftp.end();
}

/**
 * 文件遍历方法
 * @param filePath 需要遍历的文件路径
 */
function fileDisplay(filePath, arr){
    // demo, success
    var fs = require('fs');
    var path = require('path');
    //根据文件路径读取文件，返回文件列表
    var files = fs.readdirSync(filePath);

    //遍历读取到的文件列表
    files.forEach(function(filename){
        //获取当前文件的绝对路径
        var filedir = path.join(filePath,filename);
        //根据文件路径获取文件信息，返回一个fs.Stats对象
        var stats = fs.statSync(filedir);

        var isFile = stats.isFile();//是文件
        var isDir = stats.isDirectory();//是文件夹
        if(isFile){
            // console.log('filedir:' + filedir);
            arr.push(filedir)
        }
        if(isDir){
            fileDisplay(filedir, arr);//递归，如果是文件夹，就继续遍历该文件夹下面的文件
        }
    });
    // return new Promise(function () {});
}

function get_files_from_dir(dir_path_abs){
    var rs = new Array();
    // rs.push('aaa');

    // demo, success
    var fs = require('fs');
    var path = require('path');

    //解析需要遍历的文件夹，我这以E盘根目录为例
    // var filePath = path.resolve('D:/test-sth/test-dir');
    var filePath = path.resolve(dir_path_abs);

    //调用文件遍历方法
    // fileDisplay(filePath, rs).then((data) => {
    //     return rs;
    // });

    fileDisplay(filePath, rs);
    return rs;
}

function sentToServer(){
    // var rs = get_files_from_dir('D:/test-sth/test-dir')
    // console.log('rs:' + rs);

    // local_dir_path = 'D:/test-sth/test-dir/sub/1.txt';
    local_dir_path = 'D:/test-sth/test-dir';
    remote_dir_path = '/app/apache-tomcat-7-sc/temp';
    putDIrToServer(local_dir_path, remote_dir_path);

    // var path = require('path');
    // dirname = path.dirname(local_dir_path)
    // console.log('dirname:' + dirname);
    // remote_file_path = local_dir_path.replace(dirname, remote_dir_path)
    // console.log('remote_file_path:' + remote_file_path);
    // putToServer(local_dir_path, remote_file_path);
    // var filesArr = get_files_from_dir(local_dir_path);
    // for(var i=0;i<filesArr.length;i++){
    //     console.log(filesArr[i]);
    // }

}

function te(){
    var s = '123/2/1/2';
    console.log(s.split('/').join('-'));
}

// te();
sentToServer();



