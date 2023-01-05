const overlay = document.querySelector("#overlay");
const inc = document.getElementById("inc");
const resetButonOne = document.getElementById("ResetButonOne");

let x = 0;
let gate = true;

if (localStorage.number) {
    x = localStorage.number;
}

document.querySelector("#show-modal").addEventListener("click", () => {
  overlay.style.display = "block";
  addCyber();
});

overlay.addEventListener("click", () => {
  overlay.style.display = "none";
});

const addCyber = () => {
  x++;
  inc.innerHTML = `You have clicked <strong>${x} times </strong> to related button.`;
  localStorage.setItem("number", x);

  if (x >= 5 && gate) {
      addElement();
  }
};

function addElement() {
  gate = false;
  const doc = document.createElement('input');
  doc.setAttribute('id', 'ResetButon');
  doc.setAttribute('value', 'Reset Buton');
  doc.setAttribute('onclick', 'ResetButonAll()');
  resetButonOne.appendChild(doc);
};

function ResetButonAll() {
  gate = true;
  const element = document.getElementById('ResetButon');
  element.remove();
  x = 0;
  localStorage.setItem("number", 0);
};
