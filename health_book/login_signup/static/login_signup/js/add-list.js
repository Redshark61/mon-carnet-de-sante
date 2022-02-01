// Get the DOM elements
const add = document.querySelectorAll(".js-add-element");
const list = document.querySelectorAll(".js-list");
const input = document.querySelectorAll(".js-input");
const deleteButton = document.querySelectorAll(".js-delete");
let item = document.querySelectorAll(".js-item");

// Create an eventListener for each add button
add.forEach(function (element, key) {
	element.addEventListener("click", createElement.bind(null, key));
});

function createElement(key) {
	// Get the vlaue of the input
	const inputValue = input[key].value;

	if (inputValue === "") {
		alert("Please enter a value");
	} else {
		// Create a new list item
		const newElement = document.createElement("li");
		const deleteButton = document.createElement("span");
		const content = document.createElement("span");

		newElement.classList.add("form__item");
		newElement.classList.add("js-item");
		content.classList.add("form__element");
		deleteButton.classList.add("form__delete");
		deleteButton.classList.add("js-delete");

		deleteButton.textContent = "❌";
		content.textContent = inputValue;

		newElement.appendChild(content);
		newElement.appendChild(deleteButton);

		// Add the new list item to the list
		list[key].appendChild(newElement);

		// Empty the input
		input[key].value = "";
		// Add the eventListener to the delete button
		deleteButton.addEventListener("click", deleteItem);
	}
}

function deleteItem(e) {
	// Get the parent element of the delete button and remove it
	e.target.parentNode.remove();
}
