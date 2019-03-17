$(document).ready(function () {
    $.getJSON("http://127.0.0.1/api/blog/get/all/",function(data,status){
    // alert("数据: " + data['data'] + "\n状态: " + status);
    var source = $("#source");
    var a = eval("("+data.data+")");
    source.html(a[2]['fields']['body']);
    var markdown = $("#markdown");
    var converter = new Showdown.converter();
    var html = converter.makeHtml(source.html());
    markdown.html(html);

  });
});