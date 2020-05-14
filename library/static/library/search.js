const bookSection = document.getElementById('bookSection');
const authorSection = document.getElementById('authorSection');
const bookRadio = document.getElementById('bookRadio');
const authorRadio = document.getElementById('authorRadio');
let jets = new Jets({searchTag: '#jetsSearch', contentTag: '.jetsContent',});
let lis = document.getElementsByTagName("li");

for (let i = 0; i < lis.length; i++) {
    lis[i].setAttribute("data-jets", lis[i].getAttribute("data-jets").replace(/unread/gi, "").replace(/read/gi, "").replace(/,/gi, " ").replace(/\./gi, " "))
}

bookRadio.addEventListener('change', (event) => {
    bookSection.style.display = "inline";
    authorSection.style.display = "none"
})

authorRadio.addEventListener('change', (event) => {
    authorSection.style.display = "inline";
    bookSection.style.display = "none"
})