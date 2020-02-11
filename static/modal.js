$(".photo").click(function() {
    console.log(this);
    var modalId = this.id + "-modal";
    var modalImgSrc = this.src;
    console.log(modalId);
    console.log(modalImgSrc);
    $("#" + modalId).css("display", "block");
    $("#" + modalId).find("img").attr("src", modalImgSrc);
})

$(".close").click(function() {
  $(this).parent().css("display", "none");
})