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
    if(sort_by==null){
        $(`thead>tr>td:nth-child(10)`).addClass("hightlight-column")
        $(`tbody>tr>td:nth-child(10)`).each(function(){
            $(this).addClass("hightlight-column")
        })
    }
    else{
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
}

// search submit on click actions
$("#search-submit").on("click",function(){
    $(".search-result").empty() //clear dropdown, in case search again
    $(".hightlight-row").removeClass("hightlight-row") // clear previous highlight
    var searchVal = $("#enter").val()
    var players = $("#player-list").text().slice(2,-2).split("\', \'")
    var result_players = players.filter(player => player.includes(searchVal))
    console.log(result_players.length)
    for(var i=0;i<result_players.length;i++){ // add player results to dropdown
        if($(".search-result").text().includes(result_players[i])==false){
            $(".search-result").append(`<p>${result_players[i]}</p>`)
        }
    }
    $(".search-result").css("display","block")
})

// search result dropdown on click actions
$(".search-result").on("click","p",function(){
    $("#enter").val($(this).text())
    var target_player = $(this).text()
    $(".search-result").empty() // clear search dropdown
    $(".player-name").each(function(){
        if(target_player==$(this).text()){
           $(this).parent().addClass("hightlight-row") //highlight row
           console.log(document.getElementsByClassName("hightlight-row")[0]
           .scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"})) // scroll to
        }
    })
})

// show player preview
$(".player-name").on("mouseenter",function(){
    $(".player-preview").empty()
    $(this).addClass("player-onhover")
    var pos = $(this).position()
    console.log(pos["top"],pos["left"])
    $(".player-preview").css("display","flex")
    $(".player-preview").css("top",pos["top"]+window.innerHeight*0.262)
    $(".player-preview").append(
        `
        <div class="preview-title">
            <span class="preview-name">Vinnie Pasquantino</span>
            <span class="preview-age">Age: 23</span>
            <span class="preview-info">KC</span>
            <span class="preview-age">RF/LF</span>
            <span class="preview-info">L/R</span>
        </div>
        <div class="preview-content">
            <p class="preview-stat">xRank: 7</p>
            <p class="preview-stat">xSlashline: 0.299/0.442/0.578</p>
            <p class="preview-stat">Consistency: High</p>
            <p class="preview-stat">Injury Prone: Low</p>
        </div>`
    )
})
// $(".player-name").on("mouseleave",function(){
//     $(this).removeClass("player-onhover")
//     $(".player-preview").empty()
//     $(".player-preview").css("display","none")
// })

hightlightColumn()
