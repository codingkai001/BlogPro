$(document).ready(function () {

    marked.setOptions({
        renderer: new marked.Renderer(),
        gfm: true,
        tables: true,
        escaped: true,
        breaks: false,
        pedantic: false,
        sanitize: false,
        smartLists: true,
        smartypants: false,
        highlight: function (code, lang) {
            return hljs.highlightAuto(code).value;
        }
    });

    /*获取博客列表*/
    $.getJSON("/api/blog/get/all/", function (data, status) {
        var content = $("#main");
        var Data = data.data;
        for (var i = 0; i < Data.length; ++i) {
            var item = $("<div class='blog-item'></div>");
            var id = Data[i].id.toString();
            var link = '/post/?bid='+id;
            var Title = $("<a class='title' href="+link+"></a>");
            var Body = $("<div class='body-preview'></div>");
            var Footer = $("<div class='item-footer'></div>");
            var Author = $("<span class='author'></span>");
            var ReadNum = $("<span class='read_num'></span>");
            var AuthorAvatar = $("<img src='/static/imgs/favicon2.ico' alt='' class='author-avatar'/>");
            var Date = $("<span class='date'></span>");
            Date.html(Data[i].publish_date.substring(0, 10));
            var read_logo = $("<span class=\"glyphicon glyphicon-eye-open read-logo\" aria-hidden=\"true\"></span>");
            read_logo.html(Data[i].read_nums);
            Title.html(Data[i].title);
            var body = marked(Data[i].body);
            Body.html(String(body).split('\n').slice(0, 5).join('\n')+'......');
            Author.html(Data[i].author);
            ReadNum.html(Data[i].read_nums);
            Footer.append(AuthorAvatar);
            Footer.append(Author);
            // Footer.append(date_logo);
            Footer.append(Date);
            Footer.append(read_logo);
            item.append(Title);
            item.append(Body);
            item.append(Footer);
            /*blog块显示动画*/
            item.fadeIn(1000);
            content.append(item);
        }
        // alert(data.data[0].title);
    })
    // $("#blog-item").show(1000);

});