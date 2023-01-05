let clickCount = 0;


button.addEventListener("click", () => {
clickCount++;
const overlay = document.getElementById("overlay");
if (!overlay.classList.contains("active")) {
    overlay.classList.add("active");
}
const inc = document.getElementById("inc");
inc.innerHTML = clickCount;

if (clickCount > 5) {
    const resetButton = document.getElementById("reset-button");
    if (!resetButton) {
        const resetButton = document.createElement("button");
        resetButton.id = "reset-button";
        resetButton.innerHTML = "Reset";
        resetButton.addEventListener("click", () => {
            clickCount = 0;
            inc.innerHTML = clickCount;
            resetButton.parentNode.removeChild(resetButton);
        });
        inc.parentNode.appendChild(resetButton);
    }
}
});

