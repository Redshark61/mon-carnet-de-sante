const inputCities = document.querySelector(".js-input-cities");
const inputAdress = document.querySelector(".js-input-address");
const loading = document.querySelector(".js-loader");

getCities().then((value) => {
	// Add the cities dictionary to the input data
	inputAdress.line = value;
});

// Disable the <ENTER> key
window.addEventListener("keydown", (event) => {
	if (event.key == "Enter") {
		event.preventDefault();
	}
});

// add event listener to input on <ENTER> key
inputAdress.addEventListener("keyup", async function (e) {
	if (e.keyCode === 13) {
		// Cancel the default action, if needed
		e.preventDefault();

		// Add the loading animation
		loading.classList.add("active");
		loading.classList.remove("done");
		loading.classList.remove("wrong");
		isCorrect = await validate(e.currentTarget.line);
		loading.classList.remove("active");

		if (isCorrect) {
			// Remove the loading animation
			// Add the class to the input
			loading.classList.add("done");
		} else {
			loading.classList.add("wrong");
		}
	}
});

/**
 *
 * @param {Object} lines The name of cities
 * @returns {Boolean} true if the address is correct in the cities
 */
async function validate(lines) {
	return new Promise(async (resolve) => {
		// replace spaces with +
		value = inputAdress.value.replace(/\s/g, "+");
		// replace apostrophes with +
		value = value.replace(/'/g, "+");
		// replace accents with non-accented letters
		value = value.replace(/[àáâãäå]/g, "a");
		value = value.replace(/[ç]/g, "c");
		value = value.replace(/[éèêë]/g, "e");
		value = value.replace(/[îï]/g, "i");
		value = value.replace(/[ôö]/g, "o");
		value = value.replace(/[ùûü]/g, "u");

		// Get the postcode and pass all the cities
		let postcode = getPostCode(lines);
		console.log(postcode);

		// Create an hidden input to send the postcode to the form
		cityElement = document.createElement("input");
		cityElement.type = "hidden";
		cityElement.name = "postal_code";
		cityElement.value = postcode;
		document.querySelector("form").appendChild(cityElement);

		// Use the government API to check if the adress is valid
		const url = `https://api-adresse.data.gouv.fr/search/?q=${value}&postcode=${postcode}&limit=1`;
		console.log(url);
		console.log(value);
		fetch(url)
			.then((response) => response.json())
			.then((data) => {
				let properties = data.features[0].properties;
				// properties.score is the confidence of the adress : 1 is sure this is the good adress, 0 is not sure
				resolve(true ? properties.score > 0.7 : false);
			});
	});
}

/**
 *
 * @param {Array} lines List of cities
 * @returns {Int} postcode
 */
function getPostCode(lines) {
	let postcode = 0;
	// Loop through the lines of cities in order to get the postcode
	lines.forEach(function (line) {
		const columns = line.split(";");
		if (columns[0].toLowerCase() === inputCities.value.toLowerCase()) {
			postcode = columns[1];
			cityName = columns[0].toLowerCase();
			console.log("postcode " + postcode);

			return;
		}
	});
	return postcode;
}

/**
 *
 * @returns {Promise} lines
 * @description Get the cities name from the csv api
 */
async function getCities() {
	const url =
		"https://raw.githubusercontent.com/Rudloff/french-postal-codes-api/master/insee.csv";

	return new Promise(async (resolve) => {
		fetch(url)
			.then((response) => response.text())
			.then((data) => {
				const lines = data.split("\n");
				const list = document.querySelector("datalist");

				lines.forEach(function (line) {
					const columns = line.split(";");
					const option = document.createElement("option");
					option.value = columns[0];
					option.textContent = columns[1];
					list.appendChild(option);
				});
				resolve(lines);
			});
	});
}
