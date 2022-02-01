const laterInput = document.querySelectorAll(".js-later-input");
const laterButton = document.querySelector(".js-later-button");
let areEmpty = new Array(laterInput.length).fill(true);
console.log(areEmpty);

laterInput.forEach((input, key) => {
    input.addEventListener("keydown", (e) => {
        console.log(areEmpty);
        if (e.currentTarget.value == "") {
            areEmpty[key] = true;
        } else {
            areEmpty[key] = false;
        }

        if (areEmpty.every((el) => el == false)) {
            laterButton.textContent = "Suivant";
            console.log("every");
        } else {
            laterButton.textContent = "Plus tard";
        }
    });
});
