import "jquery-colorbox"


class Colorbox {
  constructor() {
    let colorbox = $("a.card").colorbox({
      transition: "fade",
      fixed: true,
      rel:"gal",
      close: "<i class='fas fa-times'></i>",
    });
  }
}

export {Colorbox}
