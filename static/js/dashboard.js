$(".head-piece").on("click",function(){
    var new_sort_by = $(this).text()
    const querystring = window.location.search
    const urlParams = new URLSearchParams(querystring)
    var sort_by = urlParams.get("sort_by")
    var dirc = urlParams.get("direction")
    var new_dir = "desc"
    if(dirc=="desc" & sort_by == new_sort_by){
        new_dir = "asc"
    }
    window.location.assign(`/dashboard?sort_by=${new_sort_by}&direction=${new_dir}`)
})

function hightlightColumn(){
    // get sort by
    const querystring = window.location.search
    const urlParams = new URLSearchParams(querystring)
    var sort_by = urlParams.get("sort_by")

    // get cols
    var nth = 0
    var col = 0
    $(".head-piece").each(function(){
        var this_col = $(this).text()
        nth += 1
        if(this_col == sort_by){
            $(this).addClass("hightlight-column")
            col = nth
        }
    })
    $(`tbody>tr>td:nth-child(${col+1})`).each(function(){
        $(this).addClass("hightlight-column")
    })
}

hightlightColumn()