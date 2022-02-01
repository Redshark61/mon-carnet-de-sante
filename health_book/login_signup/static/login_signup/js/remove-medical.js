// Get the DOM elements
const firstName = document.querySelector("label[for='firstname']");
const lastName = document.querySelector("label[for='lastname']");
let progressionDots = document.querySelectorAll(".progression-dot");
const currentNode = document.querySelector("[data-active='true']");
const links = document.querySelectorAll("a");

// Get url parameters
const urlParams = new URLSearchParams(window.location.search);
const isMedical = urlParams.get("medical");

// If the user is a medical professional, remove the first name and last name fields
if (isMedical) {
	if (firstName && lastName) {
		firstName.parentNode.remove();
		lastName.parentNode.remove();
	}

	// Remove useless progression dots
	for (let i = 1; i <= 4; i++) {
		progressionDots[progressionDots.length - i].remove();
	}

	// Get the new progression dots
	progressionDots = document.querySelectorAll(".progression-dot");

	// Change url
	links.forEach((link) => {
		link.href += "?medical=true";
	});

	// If the current node is the last one, then change the url to redirect to the home page
	if (currentNode == progressionDots[progressionDots.length - 1]) {
		links[0].href = "../../home";
	} else if (currentNode == progressionDots[0]) {
		links[1].href = "../../";
	}
}
