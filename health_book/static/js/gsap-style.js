let tl = gsap.timeline({
	scrollTrigger: {
		trigger: ".list__item",
		start: "top center",
		toggleActions: "play none none play",
	},
});

tl.to(".line-divider", {
	opacity: 1,
	duration: 2,
	x: 0,
	stagger: 1,
	ease: "power2.inOut",
});
