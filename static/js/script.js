function toggleSidebar() {
  var sidebar = document.getElementById("sidebar");
  if (sidebar.style.width === "250px") {
    sidebar.style.width = "0";
  } else {
    sidebar.style.width = "250px";
  }
}

function toggleCart() {
  var cart = document.getElementById("cart");
  if (cart.style.width === "250px") {
    cart.style.width = "0";
  } else {
    cart.style.width = "250px";
  }
}
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 'auto',
        spaceBetween: 20,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });
