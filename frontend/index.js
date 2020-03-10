import StickySidebar from "sticky-sidebar";
import {ImageLazyLoad} from "./src/lazyload";
new ImageLazyLoad().run()

require("./scss/dugong.scss");

new StickySidebar("#sidebar", {
  topSpacing: 50,
  bottomSpacing: 50,
  additionalMarginTop: 30,
  resizeSensor: false,
  // minWidth: 300,
  containerSelector: "#main-content",
  innerWrapperSelector: ".sidebar__inner",
  stickyClass: "is-affixed",
});
