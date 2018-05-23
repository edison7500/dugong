import $ from 'jquery';
// import 'jquery-ui';
// import "../../node_modules/sticky-sidebar/dist/'
import StickySidebar from 'sticky-sidebar'
import plugin from './plugin';

plugin('stickysidebar', StickySidebar);

$(document).ready(function(){
    $("#sidebar").stickysidebar({
        // containerSelector: '.columns',
        // innerWrapperSelector: '.sidebar__inner',
        topSpacing: 50,
        bottomSpacing: 20,
        resizeSensor: false,
        minWidth: 300,
    });
});

// window.$ = $;
// window.jQuery = jQuery;