const lotties = document.querySelectorAll("lottie-player");

let options = {
	root: null,
	rootMargin: "0px",
	threshold: 0,
};

let observer = new IntersectionObserver(handleIntersect, options);
lotties.forEach((lottie) => {
	observer.observe(lottie);
});

function handleIntersect(entries, observer) {
	entries.forEach((entry) => {
		console.log(entry.isIntersecting);
		if (entry.isIntersecting) {
			entry.target.style.visibility = "visible";
			console.log(entry.target);
		} else {
			entry.target.style.visibility = "hidden";
		}
	});
}
