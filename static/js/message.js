$(document).ready(function() {
    $('button.send').on('click', function(event) {
        event.preventDefault();
        var div_parent=$(this).parent().parent();
        var textarea=div_parent.find('textarea[name="message"]');
        var conversation=$('#conversation .conversation');
        var username=div_parent.find('input[name="username"]').val();
        var fullname=div_parent.find('input[name="fullname"]').val();
        $.ajax({
            url: '/message/send/'+username+'/',
            type: 'POST',
            dataType: 'json',
            data: {message:textarea.val()},
            success:function(result) {
                if (result.status=="OK"){
                    textchat=$('<div class="message item pull-right send"><div class="author"><span>'+fullname+
                        '</span></div><div class="message-content"><span>'+textarea.val()+
                        '</span></div></div><div class="clear"></div>');
                    textarea.val("");
                    conversation.append(textchat);
                }else{                    
                }
            }
        });        
    });
window.setInterval(function(){
  //check new message
  var conversation=$('#conversation .conversation');
  var username=$('#conversation').find('input[name="username"]').val();
  $.ajax({
        url: '/message/newajax/'+username+'/',
        type: 'GET',
        success:function(result) {
            conversation.append(result);
        }
    });
}, 5000);
});