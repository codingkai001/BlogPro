$(document).ready(function () {
    var kword = location.search;

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


    $.getJSON("/api/blog/get/" + kword.toString(), function (data, status) {
        // alert(kword);
        var content = $("#main");
        var Data = data.data;
        // alert(Data);
        // alert(Data['id']);
        if (Data !== "Invalid parameter") {
            var item = $("<div class='blog-item'></div>");
            var id = Data.id;
            /*markdown*/
            // var converter = new Showdown.converter();
            // let html = converter.makeHtml(Data.body);
            var html = marked(Data.body);
            var Title = $("<a class='title'></a>");
            var Body = $("<div class='body'></div>");
            var Footer = $("<div class='item-footer'></div>");
            var Author = $("<span class='author'></span>");
            var ReadNum = $("<span class='read_num'></span>");
            var AuthorAvatar = $("<img src='/static/imgs/favicon2.ico' alt='' class='author-avatar'/>");
            var Date = $("<span class='date'></span>");
            Date.html(Data.publish_date.substring(0, 10));
            Title.html(Data.title);
            Body.html(html);
            Author.html(Data.author);
            // alert(Data[i].read_nums);
            ReadNum.html(Data.read_nums);
            Footer.append(AuthorAvatar);
            Footer.append(Author);
            Footer.append(Date);
            Footer.append(ReadNum);
            item.append(Title);
            item.append(Footer);
            item.append(Body);

            /*blog块显示动画*/
            item.fadeIn(1000);
            content.append(item);
        }
    })
    // $("#blog-item").show(1000);

});