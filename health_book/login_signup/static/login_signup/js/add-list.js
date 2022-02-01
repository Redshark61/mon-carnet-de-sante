// Get the DOM elements
const add = document.querySelectorAll(".js-add-element");
const list = document.querySelectorAll(".js-list");
const input = document.querySelectorAll(".js-input");
const deleteButton = document.querySelectorAll(".js-delete");
let item = document.querySelectorAll(".js-item");
let increment = 0;
// Create an eventListener for each add button
add.forEach(function (element, key) {
	element.addEventListener("click", (e) => {
		createElement(e, key);
	});
});

function createElement(e, key) {
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

		// Create an hidden input with the input value as value
		const hiddenInput = document.createElement("input");
		hiddenInput.setAttribute("type", "hidden");
		itemType = e.target.previousElementSibling.id.slice(0, -6);
		hiddenInput.setAttribute("name", itemType + "_" + increment);
		hiddenInput.setAttribute("value", inputValue);
		document.querySelector("form").appendChild(hiddenInput);
		increment++;
		// Add the eventListener to the delete button
		deleteButton.addEventListener("click", deleteItem);
	}
}

function deleteItem(e) {
	// Get the parent element of the delete button and remove it
	e.target.parentNode.remove();
	text = e.target.parentNode.textContent.slice(0, -1);
	console.log(text);
	document.querySelector("form").removeChild(document.querySelector(`input[value="${text}"]`));
}
