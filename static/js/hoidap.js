function getCookie(name)
{
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});
$(document).ready(function() {
    $('a#edit_mytags').on('click', function(event) {
        event.preventDefault();
        if($(this).text()=='Edit'){
            $(this).text('Done');
            $('ul#mytags li a.remove_tag').fadeIn('fast');        
        }else{            
            $(this).text('Edit');
            $('ul#mytags li a.remove_tag').fadeOut('fast');
        }
    });
    $('a.remove_tag').on('click', function(event) {
        event.preventDefault();
        var li=$(this).parent();
        var a=li.find('a.tagtitle');
        var tagid=a.attr('data');
        data={'tagid':tagid}
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": "/tag/follow/",
            "data": data,
            "success": function(result) {
                if(result.status=='OK'){                    
                    li.remove();
                }                
            },
        });
        /* Act on the event */
    });
    $('button.vote').on('click', function(event) {
        event.preventDefault();
        var button=$(this);
        var div_parent=button.parent();
        div_parent.find('span.message').remove();
        var objectid=$(this).find('input[name="objectid"]').val();
        var votetype=$(this).find('input[name="votetype"]').val();
        var objecttype=$(this).find('input[name="objecttype"]').val();
        var votes_count=$(this).find('span.votes_count');
        var data={
            'objectid':objectid,
            'objecttype':objecttype,
            'votetype':votetype
        }
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": "/question/vote/",
            "data": data,
            "success": function(result) {
                if(result.status=="OK"){
                    votes_count.text(result.votes_count);
                }else{
                    div_parent.append('<span class="text-danger message">'+result.message+'</span>');
                }
            },
        });
    });
});