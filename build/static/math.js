$(function(){
    var i = 1;
    $(".math").each(function() {
        var katexText = $(this).text();
        element = $(this).get(0);
        if(element.tagName == "DIV"){
            tag = "\\tag{" + i + "}";
            i = i + 1;
            disp = true;
        } else {
            tag = "";
            disp = false;
        }
        console.log(tag + katexText);
        try {
            katex.render(tag + katexText, element, {displayMode: disp});
        }
        catch(err) {
            $(this).html("<span class='err'>" + err);
        }
    });
});