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

    // alert(123);
    $("#raw_post").on("keyup", function () {
       var preview = $("#preview");
       preview.html(marked($(this).val()));
    });
});