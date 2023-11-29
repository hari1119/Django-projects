(function ($) {
  var body = document.body;
  $('#dark_mode').on('click', function () {
    alert();
    $('body').toggleClass('dark-mode');
    if (body.classList.contains('dark-mode')) {
      $('.dl_icon').css('color','white');
      $('.ddl').find('.ddl-input, .ddl-options').css({
        'color':'white', 
        'background':'#454d55',
        'border':'1px solid #454d55'
      });
      $('.container-fluid').find('.radio_container').css({
        'background':'#454d55',
      })
    }else{
      $('.dl_icon').css('color','');
      $('.ddl').find('.ddl-input, .ddl-options').css({
        'color':'black', 
        'background':'#d7d7d7',
        'border':'1px solid #d7d7d7'
      });
      $('.container-fluid').find('.radio_container').css({
        'background':'',
        
      })
    }
  });
})(jQuery);
