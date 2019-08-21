import StickySidebar from "sticky-sidebar";

var sidebar = new StickySidebar('#sidebar', {
    topSpacing: 50,
    bottomSpacing: 50,
    resizeSensor: false,

    minWidth: 300,
    stickyClass: 'is-affixed',
});

