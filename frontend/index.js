require("./scss/dugong.scss");

// import StickySidebar from "sticky-sidebar";
import {ImageLazyLoad} from "./src/utils/lazyload";
import {SSbar} from "./src/utils/sticky_sidebar";


new ImageLazyLoad().run();
new SSbar();

// let sidebar = document.getElementById("sidebar");
//
// if (sidebar) {
//   new StickySidebar(sidebar, {
//     topSpacing: 20,
//     bottomSpacing: 20,
//     // additionalMarginTop: 30,
//     resizeSensor: true,
//     // minWidth: 300,
//     containerSelector: "#main-content",
//     // containerSelector: false,
//     innerWrapperSelector: ".sidebar__inner",
//     stickyClass: "is-affixed",
//   });
// }


