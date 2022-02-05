const inputsSecurityCode = document.querySelectorAll(".js-security-code");
const telInputs = document.querySelectorAll(".js-tel-input");

inputsSecurityCode.forEach((input) => {
    new Cleave(input, {
        delimiters: ["-", "-", "-", "-", "-", " "],
        blocks: [1, 2, 2, 2, 3, 3, 2],
        numericOnly: true,
    });
});

telInputs.forEach((input) => {
    new Cleave(input, {
        phone: true,
        phoneRegionCode: "FR",
    });
});
