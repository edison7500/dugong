require("./scss/dugong.scss");

import {ImageLazyLoad} from "./src/utils/lazyload";
import {SSbar} from "./src/utils/sticky_sidebar";
import "@fancyapps/fancybox"


new ImageLazyLoad().run();
new SSbar();
