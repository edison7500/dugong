'use strict';

import StickySidebar from "sticky-sidebar";

export class SideBar {
    constructor()
    {
        this.sticky = new StickySidebar('#sidebar', {
            topSpacing: 50,
            bottomSpacing: 50,
            resizeSensor: false,

            minWidth: 300,
            stickyClass: 'is-affixed',
        });
    }

}
