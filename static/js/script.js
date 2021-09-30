$(document).ready(function() {
     
    $(".fa-search").click(function() {
       $(".search-box").toggle();
       $("input[type='text']").focus();
     });

 });

 $(function () {
  $(document).scroll(function () {
    var $nav = $(".fixed-top");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});