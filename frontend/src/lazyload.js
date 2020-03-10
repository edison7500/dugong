import LazyLoad from "vanilla-lazyload";

// let lazyLoadInstance = new LazyLoad({
//   elements_selector: ".lazy"
// });

class ImageLazyLoad {
  constructor() {
    this.lazyLoadInstance = new LazyLoad({
      elements_selector: ".lazy"
    });
  }

  run() {
    this.lazyLoadInstance.update();
  }
}

export {ImageLazyLoad}