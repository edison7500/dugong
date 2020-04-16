import "jquery-colorbox"


class Colorbox {
  constructor() {
    this.close = `<i class='fas fa-times'></i>`;
    this.previous = `<i class="fas fa-chevron-left"></i>`;
    this.next = `<i class="fas fa-chevron-right"></i>`;
    this.init();
  }

  init() {
    this.colorbox = $("a.card").colorbox({
      transition: "fade",
      fixed: true,
      rel: "gal",
      current: "",
      className: "modal",
      previous: this.previous,
      next: this.next,
      close: this.close,
      scrolling: false,
      maxWidth: "75%",
      maxHeight: "75%",
    });
  }
}

export {Colorbox}
