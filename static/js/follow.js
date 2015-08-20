$(document).ready(function() {
    // follow
    $("#followuser").click(function(e) {
        e.preventDefault();
        var username=$('#follow').val();
        var data = {
            'username': username
        }
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": "/user/follow/",
            "data": data,
            "success": function(result) {
                if(result.status=='OK'){
                    $('.follow_label').html(result.label);
                    $('.followers_count').html('('+result.followers_count+')');
                    $('.followmessage').html('');
                }else{
                    $('.followmessage').html('<span class="text-danger">'+result.message+'</span>');
                }                
            },
        });
    });
    $("#followtag").click(function(e) {
        e.preventDefault();
        var tagid=$('#tagid').val();
        var data = {
            'tagid': tagid
        }
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": "/tag/follow/",
            "data": data,
            "success": function(result) {
                if(result.status=='OK'){
                    $('.follow_label').html(result.label);
                    $('.followers_count').html('('+result.followers_count+')');
                    $('.followmessage').html('');
                }else{
                    $('.followmessage').html('<span class="text-danger">'+result.message+'</span>');
                }                
            },
        });
    });
});
