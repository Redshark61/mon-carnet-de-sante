const inputCities = document.querySelector(".js-input-cities");
const inputAdress = document.querySelector(".js-input-address");
const loading = document.querySelector(".js-loader");

getCities().then((value) => {
	inputAdress.line = value;
});

window.addEventListener("keydown", (event) => {
	if (event.key == "Enter") {
		event.preventDefault();
	}
});

// add event listener to input on enter key
inputAdress.addEventListener("keyup", async function (e) {
	if (e.keyCode === 13) {
		// Cancel the default action, if needed
		e.preventDefault();
		// Add the loading animation
		loading.classList.add("active");
		loading.classList.remove("done");
		await validate(e.currentTarget.line);
		loading.classList.remove("active");
		loading.classList.add("done");
	}
});

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

		let postcode = getPostCode(lines);
		console.log(postcode);

		cityElement = document.createElement("input");
		cityElement.type = "hidden";
		cityElement.name = "postal_code";
		cityElement.value = postcode;
		document.querySelector("form").appendChild(cityElement);
		// Use the government API to check if the adress is valid
		const url = `https://api-adresse.data.gouv.fr/search/?q=${value}&postcode=${postcode}&limit=1`;
		fetch(url)
			.then((response) => response.json())
			.then((data) => {
				const p = document.createElement("p");
				let properties = data.features[0].properties;
				resolve();
			});
	});
}

/**
 *
 * @param {Array} lines
 * @returns {int} postcode
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
 * @description Get the cities from the csv api
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
