$(document).ready(function() {
    
    $('.nav-link').hover(function(){
        $(this).animate({'z-index':'1','font-size':'20px'},50);
		  },
		  function(){
		  $(this).animate({'z-index':'0','font-size':'16px'},50);
		});
});