const staticCacheName = "site-static-v2";
const assets = [
	"/",
	"/static/js/pwa/manifest.json",
	"/static/js/pwa/app.js",
	"/static/js/modal.js",
	"/static/js/intersection.js",
	"/static/js/style-lottie.js",
	"/static/js/nav-button.js",
	"/static/style/main.css",
	"/static/img/icons/icon-96.png",
	"/static/img/close.svg",
	"/static/img/index/hero_img.png",
	"/static/img/index/animation_click.gif",
	"/static/img/index/wave.svg",
	"/static/img/index/clock.svg",
	"/static/img/index/pattern.svg",
	"https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js",
	"https://unpkg.com/aos@2.3.1/dist/aos.js",
	"https://assets7.lottiefiles.com/private_files/lf30_4FGi6N.json",
	"https://assets3.lottiefiles.com/packages/lf20_dn2wyuxu.json",
	"https://assets6.lottiefiles.com/packages/lf20_phdimzuf.json",
	"https://unpkg.com/aos@2.3.1/dist/aos.css",
	"https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap",
	"https://fonts.googleapis.com/css2?family=Heebo:wght@100;200;300;400;500;600;700;800;900&display=swap",
	"https://fonts.gstatic.com/s/heebo/v18/NGSpv5_NC0k9P_v6ZUCbLRAHxK1EiSysdUmm.woff2",
	"https://fonts.gstatic.com/s/merriweather/v28/u-4n0qyriQwlOrhSvowK_l52xwNZWMf6.woff2",
	"https://fonts.gstatic.com/s/merriweather/v28/u-440qyriQwlOrhSvowK_l5-fCZM.woff2",
];

// install service worker
self.addEventListener("install", (e) => {
	e.waitUntil(
		caches.open(staticCacheName).then((cache) => {
			cache.addAll(assets);
		})
	);
});

// activate service worker
self.addEventListener("activate", (e) => {
	e.waitUntil(
		caches.keys().then((keys) => {
			return Promise.all(
				keys.filter((key) => key !== staticCacheName).map((key) => caches.delete(key))
			);
		})
	);
});

// fetch event
self.addEventListener("fetch", (e) => {
	e.respondWith(
		caches.match(e.request).then((cacheRes) => {
			return cacheRes || fetch(e.request);
		})
	);
});
