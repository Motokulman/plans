$('#likes').click(function(){

    $.get('like_plan', function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});
