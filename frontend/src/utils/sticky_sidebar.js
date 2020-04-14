import "sticky-sidebar"


class SSbar {
  constructor() {
    let sidebar = document.getElementById("sidebar");
    if (sidebar) {
      this.initialize(sidebar);
    }
  }

  initialize(sidebar) {
    this.sticky = new StickySidebar(sidebar, {
        topSpacing: 50,
        bottomSpacing: 60,
        // additionalMarginTop: 30,
        resizeSensor: false,
        // minWidth: 300,
        containerSelector: "#main-content",
        // containerSelector: false,
        innerWrapperSelector: ".sidebar__inner",
        stickyClass: "is-affixed",
      }
    );
  }
}

export {SSbar};