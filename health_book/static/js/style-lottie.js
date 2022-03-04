let lottieDoctor = document.querySelector("lottie-player#lottie-doctor");
let lottieList = document.querySelector("lottie-player#lottie-list");
let lottieChat = document.querySelector("lottie-player#lottie-chat");
lottieDoctor.shadowRoot.getElementById("animation").style.width = "40vw";
let animationContainer = lottieDoctor.shadowRoot.getElementById("animation-container");
animationContainer.style.width = "fit-content";
animationContainer.style.marginInline = "auto";

let animationContainerList = lottieList.shadowRoot.getElementById("animation-container");
lottieList.style.width = "15vw";
animationContainerList.style.width = "15vw";

let animationContainerChat = lottieChat.shadowRoot.getElementById("animation-container");
lottieChat.style.width = "15vw";
animationContainerChat.style.width = "15vw";

// detect when screen size is less than 768px
// and change the animation size
window.addEventListener("resize", resize());

resize();

function resize() {
	if (window.innerWidth < 768) {
		// lottieDoctor.shadowRoot.getElementById("animation-container").style.width = "40vw";
		lottieList.shadowRoot.getElementById("animation-container").style.width = "50vw";
		lottieList.style.width = "50vw";
		lottieChat.shadowRoot.getElementById("animation-container").style.width = "50vw";
		lottieChat.style.width = "50vw";
	}
}
