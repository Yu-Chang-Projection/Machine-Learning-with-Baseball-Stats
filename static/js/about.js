$(document).on("mouseenter",".about-block",function(){
    $(this).removeClass("")
    $(this).find(".about-title").addClass("hide")
    $(this).find(".about-text").removeClass("hide")
})

$(document).on("mouseleave",".about-block",function(){
    $(this).find(".about-title").removeClass("hide")
    $(this).find(".about-text").addClass("hide")
})
