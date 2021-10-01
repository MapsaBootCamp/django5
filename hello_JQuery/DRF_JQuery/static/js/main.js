console.log("hello");



const token = "Bearer " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMzNTE1NjkyLCJqdGkiOiJmNjI1MDkxNWI4NWQ0MjljOTg4MjU3M2U0YmIwN2Q5YSIsInVzZXJfaWQiOjF9.iTginYpbeRd03wtenJ91BlddaMDF2lMBrsmybOgKDzA"



function makeLike(id) {
    const url = `/api/${id}`
    jQuery.ajax({
        url: url,
        type: 'POST',
        contentType: "application/json",
        beforeSend: function(xhr) {
            xhr.setRequestHeader(
                "Authorization", token,
            )
        },
        success: console.log("ba khubio khoshi like shod")
    })
}

function getLike(id) {
    const url = `/api/${id}`
        // fetch().then((data)=>{

    // })
    jQuery.ajax({
        url: url,
        type: 'GET',
        contentType: "application/json",
        beforeSend: function(xhr) {
            xhr.setRequestHeader(
                "Authorization", token,
            )
        },
        success: function(response) {

            // var data = $.parseJSON(response);

            $("#like").html(response.like);

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    })

}
$(document).ready(function() {

    getLike(1);

    $("button").click(() => {

        let old_like = $("#like").text();
        let new_like = parseInt(old_like) + 1;
        $("#like").html(new_like);
        $("#like-span").html(new_like);
        $("p").css("background-color", "yellow");
        makeLike(1)

    })
});