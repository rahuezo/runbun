$(document).ready(function() {
    console.log("THIS"); 
    $('a').hover(function(){
        $(this).animate({'z-index':'1','font-size':'30px'},50);
		  },
		  function(){
		  $(this).animate({'z-index':'0','font-size':'15px'},50);
		});
});