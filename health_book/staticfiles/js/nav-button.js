const button = document.querySelector(".js-nav-button");
const nav = document.querySelector(".js-nav");

button.addEventListener("click", () => {
	nav.classList.toggle("nav--open");
	button.classList.toggle("nav-button--open");
});
