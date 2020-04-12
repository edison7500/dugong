import "jquery-colorbox"


class Colorbox {
  constructor() {
    let colorbox = $("a.card").colorbox({
      rel:"gal",
      close: "<i class='fas fa-times'></i>"
    });
  }
}

export {Colorbox}
