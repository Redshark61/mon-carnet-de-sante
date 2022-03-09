// install service worker
self.addEventListener("install", (e) => {
	console.log("Service Worker Installed");
});

// activate service worker
self.addEventListener("activate", (e) => {
	console.log("Service Worker Activated");
});

// fetch event
self.addEventListener("fetch", (e) => {
	console.log("Fetch Event", e);
});
