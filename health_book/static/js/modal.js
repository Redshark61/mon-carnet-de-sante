// Get the DOM elements
const modalBG = document.querySelector(".js-modal-bg");
const modal = document.querySelector(".js-modal");
const modalsClose = document.querySelectorAll(".js-modal-close");
const modalInputs = document.querySelectorAll(".js-modal-input");
const buttonChoices = document.querySelectorAll(".js-modal-choice");

// Add the modal
modalInputs.forEach((modalInput) => {
	modalInput.addEventListener("click", (e) => {
		e.preventDefault();
		modal.classList.add("modal--active");
		modalBG.classList.add("modal-bg--active");

		if (modalInput.id === "login") {
			buttonChoices.forEach((choice) => {
				let value = choice.getAttribute("value");
				value = value.split("&")[0];
				choice.setAttribute("value", `${value}&login`);
			});
		} else if (modalInput.id === "signup") {
			buttonChoices.forEach((choice) => {
				let value = choice.getAttribute("value");
				value = value.split("&")[0];
				choice.setAttribute("value", `${value}&signup`);
			});
		}
	});
});

// Remove the modal
modalsClose.forEach((modalClose) => {
	modalClose.addEventListener("click", (e) => {
		e.preventDefault();
		modal.classList.remove("modal--active");
		modalBG.classList.remove("modal-bg--active");
	});
});
