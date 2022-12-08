// Pierwszym krokiem będzie dodanie obsługi zdarzenia click dla przycisku o identyfikatorze show-modal. W tym celu należy użyć metody addEventListener dostępnej dla elementów DOM. Funkcja, która będzie wywoływana po kliknięciu przycisku, powinna sprawdzić, czy popup jest już wyświetlany na stronie, a jeśli nie, to ustawić odpowiednią klasę dla elementu zawierającego popup, która spowoduje jego wyświetlenie.

const button = document.getElementById("show-modal");

button.addEventListener("click", () => {
    const overlay = document.getElementById("overlay");
    if (!overlay.classList.contains("active")) {
        overlay.classList.add("active");
    }
});

// Następnym krokiem będzie dodanie obsługi zdarzenia click dla elementu zawierającego popup. W tym celu należy sprawdzić, czy kliknięcie nastąpiło na element modal (czyli w samym popupie), a jeśli nie, to usunąć klasę odpowiedzialną za wyświetlanie popupu.

const overlay = document.getElementById("overlay");
overlay.addEventListener("click", (event) => {
    if (event.target.id !== "modal") {
        overlay.classList.remove("active");
    }
});

// Kolejnym krokiem będzie dodanie licznika kliknięć w przycisk oraz wyświetlanie tej wartości w popupie. W tym celu należy zapisać wartość licznika w zmiennej globalnej i co kliknięcie przycisku zwiększać ją o 1. Wartość licznika należy wyświetlić w elemencie o identyfikatorze inc w popupie.

// let clickCount = 0;

// const button = document.getElementById("show-modal");

// button.addEventListener("click", () => {
//   clickCount++;
//   const overlay = document.getElementById("overlay");
//   if (!overlay.classList.contains("active")) {
//   overlay.classList.add("active");
//   }
//   const inc = document.getElementById("inc");
//   inc.innerHTML = clickCount;
//   });

  
  
// Ostatnim krokiem będzie dodanie funkcjonalności resetowania licznika kliknięć. Jeśli wartość licznika przekroczy 5, to należy dodać przycisk do resetowania licznika, który będzie wyświetlany w popupie. Kliknięcie na ten przycisk powinno zresetować licznik oraz usunąć przycisk z popupu.

// javascript

let clickCount = 0;

// const button = document.getElementById("show-modal");

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

