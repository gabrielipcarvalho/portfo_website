document.querySelectorAll(".file-panel button").forEach(function (button) {
	button.addEventListener("click", function () {
		var icon = this.querySelector(".fa");
		icon.classList.toggle("fa-chevron-right");
		icon.classList.toggle("fa-chevron-down");

		var fileUrl = this.getAttribute("data-file-url");
		var codeBlockId = this.getAttribute("data-target").substring(1);
		var codeElement = document.getElementById("code-" + codeBlockId);
		var collapseElement = document.getElementById(codeBlockId);

		if (!codeElement.textContent.trim()) {
			// Fetch and load the content if not already loaded
			fetch(fileUrl)
				.then((response) => response.text())
				.then((data) => {
					codeElement.textContent = data;
					Prism.highlightElement(codeElement); // Apply syntax highlighting
				})
				.then(() => {
					Prism.highlightAll(); // Re-apply syntax highlighting globally
				})
				.catch((error) => {
					console.error("Error fetching the file:", error);
					codeElement.textContent = "Error loading file content";
				});
		}

		// Ensure the collapse works correctly by using Bootstrap's collapse toggle
		$(collapseElement).on("hidden.bs.collapse", function () {
			icon.classList.add("fa-chevron-right");
			icon.classList.remove("fa-chevron-down");
		});

		$(collapseElement).on("shown.bs.collapse", function () {
			icon.classList.add("fa-chevron-down");
			icon.classList.remove("fa-chevron-right");
		});

		$(collapseElement).collapse("toggle");
	});
});
