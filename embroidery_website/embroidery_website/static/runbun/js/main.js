$(document).ready(function(){
  console.log("REady");
  // ===== Scroll to Top ====
  $(document).scroll(function() {
      if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
          $('#back-to-top-btn').fadeIn(200);    // Fade in the arrow
      } else {
          $('#back-to-top-btn').fadeOut(200);   // Else fade out the arrow
      }
  });

  $('#back-to-top-btn').click(function() {      // When arrow is clicked
    console.log('clicked');
      $('body,html').animate({
          scrollTop : 0                       // Scroll to top of body
      }, 500);
  });
});
