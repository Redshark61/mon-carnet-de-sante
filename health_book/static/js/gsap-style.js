let tl = gsap.timeline({
	scrollTrigger: {
		trigger: ".list__item",
		start: "top center",
		// end: "top top",
		// once: true,
		toggleActions: "play none none play",
	},
});

tl.addLabel("start").to(".line-divider", {
	opacity: 1,
	duration: 2,
	x: 0,
	stagger: 1,
	ease: "power2.inOut",
});
