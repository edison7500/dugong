require("./scss/dugong.scss");

import {ImageLazyLoad} from "./src/utils/lazyload";
import {SSbar} from "./src/utils/sticky_sidebar";
import {Colorbox} from "./src/utils/colorbox";


new ImageLazyLoad().run();
SSbar();
Colorbox();


