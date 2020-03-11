import LazyLoad from "vanilla-lazyload";

// let lazyLoadInstance = new LazyLoad({
//   elements_selector: ".lazy"
// });

export class ImageLazyLoad {
  constructor() {
    this.lazyLoadInstance = new LazyLoad({
      container: document.getElementById("scrollingPanel"),
      elements_selector: ".lazy"
    });
  }

  run() {
    this.lazyLoadInstance.update();
  }
}

