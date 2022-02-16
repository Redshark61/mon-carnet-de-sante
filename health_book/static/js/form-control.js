const checkboxs = document.querySelectorAll('input[type="checkbox"]');

checkboxs.forEach((checkbox) => {
	checkbox.parentElement.classList.add("form__group--checkbox");
});
