const checkboxs = document.querySelectorAll('input[type="checkbox"]');
const textareas = document.querySelectorAll("textarea");

checkboxs.forEach((checkbox) => {
	checkbox.parentElement.classList.add("form__group--checkbox");
});

textareas.forEach((textarea) => {
	textarea.parentElement.style.width = "auto";
});
