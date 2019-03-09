$(document).ready(function(){
	'use strick';
	$(window).scroll(function(){

		'use strict';
		if ($(window).scrollTop() < 80 ) {
			$('.navbar').css ({
				'margin-top':'-100px',
				'opacity':'0'
			});

			$('.navbar').css ({
				'background-color':'rgba(59,59,59,0)'
			});


		} else {
			$('.navbar').css ({
				'margin-top':'0px',
				'opacity':'1'
			});

			$('.navbar').css ({
				'background-color':'rgba(59,59,59,0.7)',
				'border-color':'#444'
			});

			$('.navbar-brand img').css({
				'height':'35px',
				'padding-top':'0px'
			});

			$('.navbar .navbar-nav .nav-item .nav-link').css({
				'padding-top':'15px',
				
			});

		}

	});

});


// add smooth scrolling
$(document).ready(function() {
	'use strict';

	$('.nav-link, #scroll-to-top').click(function() {
    // On-page links
    if (
      location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') 
      && 
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
    }
    }
  });

});
// on click
$(document).ready(function(){
	'use strict';
	$('.navbar-nav li a').click(function(){
		'use strict';
		$(".navbar-nav li a").parent().removeClass("active");
		$(this).parent().addClass("active");
	});
	
});
// highlight menu item on scroll

$(document).ready(function(){
	'use strict';
	$(window).scroll(function(){
		'use strict';
		$("section").each(function(){
			'use strict';
			var bb = $(this).attr("id");
			var hei = $(this).outerHeight();
			var grttop = $(this).offset().top - 70;

			if ($(window).scrollTop() > grttop && $(window).scrollTop() < grttop+hei) {
				$(".navbar-nav li a[href='#"+ bb +"']").parent().addClass("active");

			}else {
				$(".navbar-nav li a[href='#"+ bb +"']").parent().removeClass("active");
			}
		});
	});
});
