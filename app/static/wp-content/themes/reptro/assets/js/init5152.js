(function($) {
  
  "use strict";
    
  /**
  * Preloader
  */

  $(window).on( "load", function() {
    $("body").removeClass("xt-site-loading");
    $("body").addClass("xt-site-loaded");
    $(".site-content .learn-press-breadcrumb").remove();
  });

  
  /**
   * Add Custom CSS Class
   */

  $('table').addClass('table table-bordered');
    
  /**
   * NAV FIXED ON SCROLL
   */

      
  $(window).on('scroll', function() {
      var scroll = $(window).scrollTop();
      if (scroll >= 400) {
          $(".nav-scroll").addClass("strict");
      } else {
          $(".nav-scroll").removeClass("strict");
      }
  });

  $.fn.touchHover = function() {
    return 'ontouchstart' in document.documentElement ? this.on( 'click', function() {
      $(this).toggleClass('xt-item-touchend');
    }) : this;
  };

  $('.xt-service-inner-2, .xt-project-gallery .grid-item figure').touchHover();

    
  /**
   * Mobile NAv trigger
   */

  
  var trigger = $('.navbar-toggle'),
  overlay     = $('.overlay'),
  active      = false;

  $('.navbar-toggle, #navbar-nav li a, .overlay').on('click', function () {
    $('.navbar-toggle').toggleClass('active')
    $('#js-navbar-menu').toggleClass('active');
    overlay.toggleClass('active');
  });  

  $('.reptro-mobile-menu').each(function() {

    var t       = $(this),
    direction   = t.data("direction") ? !0 : !1,
    closedIcon  = t.data("direction") ? 'left' : 'right';

    $(this).find('.mobile-menu-init').slicknav({
      prependTo: '.mobile-menu-area',
      parentTag: 'span',
      allowParentLinks: true,
      duplicate: false,
      label: '',
      closedSymbol: '<i class="fa fa-angle-'+ closedIcon +'" aria-hidden="true"></i>',
      openedSymbol: '<i class="fa fa-angle-down" aria-hidden="true"></i>',
    });
  });

  var win         = $(window);
  var headerArea  = $('.menu-spacing ');
  var header3     = $('.menu-spacing ');
  var stick       = 'stick';
  var stick2      = 'stick2';

  win.on('scroll',function() {    
    var scroll = win.scrollTop();
    if (scroll < 245) {
      headerArea.removeClass(stick);
    }else{
      headerArea.addClass(stick);
    }
  });

  win.on('scroll',function() {    
    var scroll = win.scrollTop();
    if (scroll < 100) {
      header3.removeClass(stick2);
    }else{
      header3.addClass(stick2);
    }
  });
          
    
    
  /**
   * FancyBox
   */


  if ( $.isFunction($.fn.fancybox) ) {
    $("[data-fancybox]").fancybox({});
  }
      
  
  /**
   * Isotope
   */

  $(window).on( "load", function() {
    var $container = $('.portfolio-container');
    
    if ( $.isFunction($.fn.isotope) ) {
      $container.isotope({
        filter: '*',
        animationOptions: {
          queue: true
        }
      });
    }

    $('.portfolio-nav li').on( 'click', function(){
      $('.portfolio-nav .current').removeClass('current');
      $(this).addClass('current');

      if ( $.isFunction($.fn.isotope) ) {
        var selector = $(this).attr('data-filter');
        $container.isotope({
          filter: selector,
          animationOptions: {
            queue: true
          }
        });
        return false;
      }

    }); 
  });


  /**
   * Course isotope
   */

  $(window).on( "load", function() {
    var $courseContainer = $('.reptro-course-isotope');
    
    if ( $.isFunction($.fn.isotope) ) {
      $courseContainer.isotope({
        filter: '*',
        animationOptions: {
          queue: true
        }
      });
    }

    $('.reptro-category-items li').on( 'click', function(){
      $('.reptro-category-items .active').removeClass('active');
      $(this).addClass('active');

      if ( $.isFunction($.fn.isotope) ) {
        var CourseCatSelector = $(this).attr('data-filter');
        $courseContainer.isotope({
          filter: CourseCatSelector,
          animationOptions: {
            queue: true
          }
        });
        return false;
      }

    }); 
  });


  /**
   * Course Slider
   */
  
  $(".reptro-course-slider, .reptro-course-category-slider, .xt-blog-post-slider").each(function() {
      var t         = $(this),
      auto          = t.data("autoplay") ? !0 : !1,
      loop          = t.data("loop") ? !0 : !1,
      rtl           = t.data("direction") ? !0 : !1,
      items         = t.data("items") ? parseInt(t.data("items")) : '',
      desktopsmall  = t.data("desktopsmall") ? parseInt(t.data("desktopsmall")) : '',
      tablet        = t.data("tablet") ? parseInt(t.data("tablet")) : '',
      mobile        = t.data("mobile") ? parseInt(t.data("mobile")) : '',
      nav           = t.data("navigation") ? !0 : !1,
      pag           = t.data("pagination") ? !0 : !1,
      navTextLeft   = t.data("direction") ? 'right' : 'left',
      navTextRight  = t.data("direction") ? 'left' : 'right';
          
      $(this).owlCarousel({
          autoplay: auto,
          rtl: rtl,
          items: items,
          responsiveClass: true,
          responsive:{
            0:{
              items: mobile,
            },
            480:{
              items: mobile,
            },
            768:{
              items: tablet,
            },
            1170:{
              items: desktopsmall,
            },
            1200:{
              items: items,
            }
          },
          nav: nav,
          navText : ['<i class="fa fa-arrow-'+navTextLeft+'" aria-hidden="true"></i>','<i class="fa fa-arrow-'+navTextRight+'" aria-hidden="true"></i>'],
          dots: pag,
          loop: loop,
          margin: 30,
      });
  });


  /**
   * Main SLIDER
   */
    
  $(window).on('load', function() {      
    $(".theme-main-slider").each(function() {
        var t = $(this),
          auto          = t.data("autoplay") ? !0 : !1,
          loop          = t.data("loop") ? !0 : !1,
          rtl           = t.data("direction") ? !0 : !1,
          nav           = t.data("navigation") ? !0 : !1,
          pag           = t.data("pagination") ? !0 : !1;
            
        $(this).owlCarousel({
            autoHeight: true,
            items: 1,
            loop: loop,
            autoplay: auto,
            dots: pag,
            nav: nav,
            autoplayTimeout: 7000,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            animateIn: 'zoomIn',
            animateOut: 'fadeOut',
            autoplayHoverPause: false,
            touchDrag: true,
            mouseDrag: true,
            rtl: rtl
        });

        $(this).on("translate.owl.carousel", function () {
          $(this).find(".owl-item .slide-text > *").removeClass("fadeInUp animated").css("opacity","0");
          $(this).find(".owl-item .slide-img").removeClass("fadeInRight animated").css("opacity","0");
        });          
        $(this).on("translated.owl.carousel", function () {
          $(this).find(".owl-item.active .slide-text > *").addClass("fadeInUp animated").css("opacity","1");
          $(this).find(".owl-item.active .slide-img").addClass("fadeInRight animated").css("opacity","1");
        });
    });
  });

  /**
   * SLIDER Preloader
   */

  $(window).on('load', function() {
    $('.slider_preloader_status').fadeOut();
    $('.slider_preloader').delay(350).fadeOut('slow');
    $('.header-slider').removeClass("header-slider-preloader");
  })


  /**
   * Back to top
   */
  
  var back_to_top_offset    = 200;
  var back_to_top_duration  = 600;

  $(window).on( "scroll", function() {
    if ($(this).scrollTop() > back_to_top_offset) {
      $('.xt-back-to-top').fadeIn(400);
    } else {
      $('.xt-back-to-top').fadeOut(400);
    }
  });

  $('.xt-back-to-top').on( "click", function(event) {

    event.preventDefault();

    $('html, body').animate({
      scrollTop: 0
    }, back_to_top_duration );

    return false;
  });


  /**
   * off canvas sidebar
   */

  $('#reptro-off-canvas-trigger-button').on( "click", function(event) {
    event.preventDefault();
  });

  if(document.getElementById('reptro-off-canvas-trigger-button') != null) {
    if ( $.isFunction($.fn.offcanvas) ) {
      $('#reptro-off-canvas-sidebar').offcanvas({
        modifiers: 'right,overlay,absolute',
        triggerButton: '#reptro-off-canvas-trigger-button'
      });
    }
  }

}(jQuery));