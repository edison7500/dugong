import $ from "jquery";
import plugin from "./plugin";

class ScrollToTop {
	constructor(element, options) {
		const $element = $(element);

		$(window).scroll(function () {
			if ($(this).scrollTop() > options.offset) {
				$element.fadeIn();
			} else {
				$element.fadeOut();
			}
		});

		$element.click(function (e) {
			e.preventDefault();

			$("html, body").animate({
				scrollTop: 0
			}, options.speed);
		});
	}
}

ScrollToTop.DEFAULTS = {
	offset: 100,
	speed: 500,
};

plugin("ScrollToTop", ScrollToTop);