import "jquery-lazyload";

class ImageLazyLoad {
  constructor() {
    this.lazy = $("img.lazy");
  }

  run() {
    this.lazy.lazyload();
  }
}

export {ImageLazyLoad}