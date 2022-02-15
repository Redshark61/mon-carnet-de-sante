const laterInput = document.querySelectorAll(".js-later-input");
const laterButton = document.querySelector(".js-later-button");

// create an empty array to store all the inputs
let areEmpty = new Array(laterInput.length).fill(true);

laterInput.forEach((input, key) => {
	input.addEventListener("keydown", (e) => {
		// on every keypress, check if the input is empty
		if (e.currentTarget.value == "") {
			areEmpty[key] = true;
		} else {
			areEmpty[key] = false;
		}

		// if all inputs are not empty, enable the button
		if (areEmpty.every((el) => el == false)) {
			laterButton.textContent = "Suivant";
		} else {
			laterButton.textContent = "Plus tard";
		}
	});
});
