var swiper = new Swiper('.carousel', {
  slidesPerView: 1,
  // spaceBetween: 30,
  slidesPerGroup: 1,
  loop: true,
  centerSlider: "true",
  fade: "true",
  grabCursor: "true",

  // loopFillGrouWithBlank: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  // breakpoints: {
  //   0: {
  //     slidesPerView: 1,
  //   },
  //   520: {
  //     slidesPerView: 2,
  //   },
  //   768: {
  //     slidesPerView: 3,
  //   },
  //   1000: {
  //     slidesPerView: 4,
  //   }

  // },
  autoplay: {
    dalay: 10,
    disableOnInteraction: false,
  }
});

