// /**
// * Template Name: Bikin - v2.2.0
// * Template URL: https://bootstrapmade.com/bikin-free-simple-landing-page-template/
// * Author: BootstrapMade.com
// * License: https://bootstrapmade.com/license/
// */
!(function ($) {
  "use strict";

  // Init AOS
  function aos_init() {
    AOS.init({
      duration: 1000,
      once: true,
    });
  }
  $(window).on("load", function () {
    aos_init();
  });
})(jQuery);
