var jets = new Jets({
    searchTag: '#jetsSearch',
    contentTag: '.jetsContent',
});

let lis = document.getElementsByTagName("li");

for (let i = 0; i < lis.length; i++) {
    lis[i].setAttribute("data-jets", lis[i].getAttribute("data-jets").replace(/unread/gi, "").replace(/read/gi, "").replace(/,/gi, " ").replace(/read/gi, "").replace(/,/gi, " ").replace(/\./gi, " "))
}