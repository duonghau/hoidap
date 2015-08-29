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
    $(document).mouseup(function (e){
        var container = $(".Flyout");

        if (!container.is(e.target) // if the target of the click isn't the container...
            && container.has(e.target).length === 0) // ... nor a descendant of the container
        {
            container.fadeOut('fast');
        }
    });

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
    $('a#notificationnew').on('click', function(event) {
        var li_parent=$(this).parent();
        var flyout=li_parent.find('.NotificationsFlyout');
        flyout.fadeIn('slow');
        var result=li_parent.find('.results');
        event.preventDefault();
        $.ajax({
            "type": "GET",            
            "url": "/notification/new/",
            "success": function(results) {
                result.html(results);
            },
        });
    });
    $('a#markallread').on('click', function(event) {
        event.preventDefault();
        var flyout=$(this).parent().parent();        
        flyout.fadeIn('slow');
        var result=flyout.find('.results');
        event.preventDefault();
        $.ajax({
            "type": "GET",        
            "url": "/notification/markallread/",
            "success": function(results) {
                result.html(results);
            },
        });
    });
    $('a#messagenew').on('click', function(event) {
        var li_parent=$(this).parent();
        var flyout=li_parent.find('.MessagesFlyout');
        flyout.fadeIn('slow');
        var result=li_parent.find('.results');
        event.preventDefault();
        $.ajax({
            "type": "GET",            
            "url": "/message/new/",
            "success": function(results) {
                result.html(results);
            }
        });
    });
    //search ajax
    $('#searchtext').keyup(function(event) {
        /* Act on the event */
        var searchtext=$(this);
        var search_results=$('.search-results');
        search_results.fadeIn('fast');
        if (searchtext.val().length >=3){
            var data={'term':searchtext.val()}
            $.ajax({
                url: '/search/ajax/',
                type: 'GET',
                data: data,
                success:function(result) {
                    console.log(result.length);
                    if (result.length >0){
                        search_results.html(result);
                    }else{
                        search_results.html('<span>No results found</span>');
                    }
                }
            })
        }
    });
});