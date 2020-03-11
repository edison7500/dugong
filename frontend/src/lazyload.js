import LazyLoad from "vanilla-lazyload";

// let lazyLoadInstance = new LazyLoad({
//   elements_selector: ".lazy"
// });

export class ImageLazyLoad {
  constructor() {
    this.lazyLoadInstance = new LazyLoad({
      elements_selector: ".lazy"
    });
  }

  run() {
    this.lazyLoadInstance.update();
  }
}

