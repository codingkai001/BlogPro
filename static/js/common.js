$(document).ready(function () {
    /*导航栏动画*/
    var nav_width = $("#nav-bar").width();
    $("#toggle").on('click', function () {
        // $("#nav-bar").show().animate({width:nav_width+'px',height:'100%'}, 2000);
        $("#nav-bar").show(1000);
        $(this).hide();
    });
    $("#main").on('click', function () {
        // $("#nav-bar").hide().animate({width:'0'}, 2000);
        $("#nav-bar").hide(1000);
        $("#toggle").show();
    });
    if ($("#nav-bar").length > 0) {
        var nav = $("#nav-bar");
        $.getJSON("/api/category/get/all/", function (data, status) {
            var h = document.createElement("p");
            // var res=eval("("+data.data+")");
            // alert(data.data[1].name);
            // h.innerHTML = eval("("+data.data+")");
            // nav.append(h[0]['name']);
        });
    }

});