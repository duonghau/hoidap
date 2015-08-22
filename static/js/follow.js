$(document).ready(function() {
    // follow
    $('button.followuser').on('click', function(event) {
        event.preventDefault();
        var button=$(this);
        var div_parent=button.parent();
        div_parent.find('span.message').remove();
        var username=$(this).find('input[name="follow"]').val();
        var follow_label=$(this).find('span.follow_label');
        var followers_count=$(this).find('span.followers_count');                
        var data={'username':username}
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": "/user/follow/",
            "data": data,
            "success": function(result) {
                if(result.status=='OK'){
                    follow_label.html(result.label);
                    followers_count.html(result.followers_count);                    
                }else{                    
                    div_parent.append('<span class="text-danger message">'+result.message+'</span>');
                }
            },
        });
    });
    $("button.followtag").on('click', function(event) {
        event.preventDefault();
        var button=$(this);
        var div_parent=button.parent();
        div_parent.find('span.message').remove();
        var tagid=$(this).find('input[name="follow"]').val();
        var follow_label=$(this).find('span.follow_label');
        var followers_count=$(this).find('span.followers_count');
        var data={'tagid': tagid}
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": "/tag/follow/",
            "data": data,
            "success": function(result) {
                if(result.status=='OK'){
                    follow_label.html(result.label);
                    followers_count.html(result.followers_count);                    
                }else{
                    div_parent.append('<span class="text-danger message">'+result.message+'</span>');
                }                
            },
        });
    });
});
